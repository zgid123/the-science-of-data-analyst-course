"""Read-only Milestone 2 structural checks; no cleaning, features, or fitting.

Run: python src/verify_collection.py [--archive /path/to/anonymisedData.zip]
Requires duckdb. Outputs metadata/*.csv and structural_summary.json.
"""
import argparse
import csv
import hashlib
import json
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from zipfile import ZipFile

import duckdb

ROOT = Path(__file__).resolve().parents[1]
KEYS = {
    'courses': ['code_module', 'code_presentation'],
    'assessments': ['id_assessment'],
    'studentInfo': ['code_module', 'code_presentation', 'id_student'],
    'studentRegistration': ['code_module', 'code_presentation', 'id_student'],
    'studentAssessment': ['id_assessment', 'id_student'],
    'vle': ['code_module', 'code_presentation', 'id_site'],
    'studentVle': ['code_module', 'code_presentation', 'id_student', 'id_site', 'date'],
}


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''):
            h.update(b)
    return h.hexdigest()


def write_csv(name, rows):
    with (ROOT / 'metadata' / name).open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--archive', type=Path,
                    default=ROOT.parents[2] / 'datasets' / 'oulad' / 'anonymisedData.zip')
    args = ap.parse_args()
    (ROOT / 'metadata').mkdir(exist_ok=True)
    original = sha(args.archive)
    manifest = []
    shapes = []
    schema = []
    with tempfile.TemporaryDirectory(prefix='milestone2-') as tmp:
        con = duckdb.connect()
        con.execute("SET memory_limit='512MB'")
        con.execute('SET threads=2')
        con.execute('SET temp_directory=?', [tmp])
        with ZipFile(args.archive) as z:
            assert set(z.namelist()) == {t + '.csv' for t in KEYS}, z.namelist()
            for info in z.infolist():
                dest = Path(tmp) / info.filename
                # Reading every member validates the ZIP CRC as well.
                with z.open(info) as src, dest.open('wb') as dst:
                    for b in iter(lambda: src.read(1024 * 1024), b''):
                        dst.write(b)
                manifest.append(dict(file=info.filename, bytes=info.file_size,
                                     sha256=sha(dest), zip_crc32=f'{info.CRC:08x}'))
                name = dest.stem
                relation = con.read_csv(str(dest), header=True, sample_size=100000,
                                        na_values='', strict_mode=True)
                relation.create_view(name)
                fields = con.execute(f'DESCRIBE "{name}"').fetchall()
                cols = [r[0] for r in fields]
                counts = con.execute(f'SELECT count(*), ' + ', '.join(
                    f'count(*) FILTER (WHERE "{c}" IS NULL)' for c in cols)
                    + f' FROM "{name}"').fetchone()
                key = ', '.join('"' + c + '"' for c in KEYS[name])
                dup = con.execute(f'SELECT coalesce(sum(n-1),0) FROM '
                                  f'(SELECT count(*) n FROM "{name}" GROUP BY {key} HAVING count(*)>1)').fetchone()[0]
                null_keys = con.execute(f'SELECT count(*) FROM "{name}" WHERE ' +
                                       ' OR '.join(f'"{c}" IS NULL' for c in KEYS[name])).fetchone()[0]
                shapes.append(dict(file=info.filename, rows=counts[0], columns=len(cols),
                                   key=';'.join(KEYS[name]), duplicate_key_extra_rows=dup,
                                   null_key_rows=null_keys))
                for i, (c, dtype, *_rest) in enumerate(fields):
                    lo = hi = ''
                    if dtype in ('BIGINT', 'DOUBLE'):
                        lo, hi = con.execute(f'SELECT min("{c}"), max("{c}") FROM "{name}"').fetchone()
                    schema.append(dict(file=info.filename, column=c, inferred_type=dtype,
                                       missing=counts[i+1], minimum=lo, maximum=hi))
                print(name, counts[0], 'rows;', dup, 'duplicate key extra rows', flush=True)

        scope = "code_module='BBB' AND code_presentation='2014J'"
        # Only count records to establish structural feasibility of the M1 scope.
        # No features, assessment rates, training labels, or model metrics are produced.
        outcomes = con.execute(f'SELECT final_result, count(*) FROM studentInfo WHERE {scope} GROUP BY 1 ORDER BY 1').fetchall()
        eligible = f"{scope} AND date_registration <= 60 AND (date_unregistration IS NULL OR date_unregistration > 60)"
        eligible_count = con.execute(f'SELECT count(*) FROM studentRegistration WHERE {eligible}').fetchone()[0]
        eligible_outcomes = con.execute(f'SELECT i.final_result, count(*) FROM studentInfo i JOIN studentRegistration r USING (code_module,code_presentation,id_student) WHERE i.code_module=\'BBB\' AND i.code_presentation=\'2014J\' AND r.date_registration<=60 AND (r.date_unregistration IS NULL OR r.date_unregistration>60) GROUP BY 1 ORDER BY 1').fetchall()
        assessments = con.execute(f'SELECT id_assessment, assessment_type, date, weight FROM assessments WHERE {scope} ORDER BY date NULLS LAST,id_assessment').fetchall()
        scope_counts = {}
        for table in ['studentInfo','studentRegistration','studentVle','vle','assessments','courses']:
            scope_counts[table] = con.execute(f'SELECT count(*) FROM "{table}" WHERE {scope}').fetchone()[0]
        scope_counts['studentAssessment'] = con.execute(f'SELECT count(*) FROM studentAssessment s JOIN assessments a USING(id_assessment) WHERE a.{scope}').fetchone()[0]
        foreign_keys = {}
        for label, query in {
            'registration_without_studentInfo': 'SELECT count(*) FROM studentRegistration r ANTI JOIN studentInfo i USING(code_module,code_presentation,id_student)',
            'assessment_record_without_assessment': 'SELECT count(*) FROM studentAssessment s ANTI JOIN assessments a USING(id_assessment)',
            'vle_record_without_material': 'SELECT count(*) FROM studentVle s ANTI JOIN vle v USING(code_module,code_presentation,id_site)',
            'vle_record_without_enrollment': 'SELECT count(*) FROM studentVle s ANTI JOIN studentInfo i USING(code_module,code_presentation,id_student)',
            'submission_without_enrollment': 'SELECT count(*) FROM (SELECT a.code_module,a.code_presentation,s.id_student FROM studentAssessment s JOIN assessments a USING(id_assessment)) s ANTI JOIN studentInfo i USING(code_module,code_presentation,id_student)',
        }.items():
            foreign_keys[label] = con.execute(query).fetchone()[0]
        summary = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
                       archive_sha256=original, archive_bytes=args.archive.stat().st_size,
                       archive_crc='PASS', scope='BBB-2014J', scope_rows=scope_counts,
                       scope_outcomes=dict(outcomes), eligible_day60=eligible_count,
                       eligible_day60_outcomes=dict(eligible_outcomes),
                       scope_assessments=[dict(zip(['id_assessment','assessment_type','date','weight'], r)) for r in assessments],
                       scope_length=con.execute(f'SELECT module_presentation_length FROM courses WHERE {scope}').fetchone()[0],
                       foreign_keys=foreign_keys)
        con.close()
    assert sha(args.archive) == original, 'Raw archive changed'
    summary['archive_unchanged'] = 'PASS'
    write_csv('raw_manifest.csv', manifest)
    write_csv('table_inventory.csv', shapes)
    write_csv('schema_checks.csv', schema)
    (ROOT / 'metadata' / 'structural_summary.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False)+'\n')
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()

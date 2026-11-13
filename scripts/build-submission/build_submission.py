"""Build the course submission: folder N04_Project/ and its ZIP, as the submission instructions ask.

Usage: venv/bin/python scripts/build-submission/build_submission.py [--out submission]

The instructions: five Word reports, one for each milestone; one presentation (.pptx); the source code, if any; every
file named <group code>_<assignment code> (for example N01_MilestoneP1); everything in a folder named
<group code>_Project, zipped for upload. The script writes into OUT (default `submission/` at the repository root):

    N04_Project/
      N04_MilestoneP1.docx … N04_MilestoneP5.docx   the Vietnamese report of each milestone
      N04_Project.pptx                              the Vietnamese 30-slide presentation of the project
      N04_SourceCode/
        N04_MilestoneP2/   Data Collection Package (brief sections 9.1 and 15)
        N04_MilestoneP3/   Prepared Data Package (brief sections 10.1 and 16)
        N04_MilestoneP5/   Final Project Package (brief section 7)
    N04_Project.zip                                 the folder above, zipped
    N04_SelfAssessment_VI.docx                      the self-assessment form, kept outside the ZIP

Raw data and other files a package rebuilds (data/raw, data/interim, fitted models, caches) are left out; each
data/raw folder holds a note on how the package's first step fetches the pinned public download. Machine paths in
run logs are replaced in the copy. OUT is recreated from scratch on every run.
"""
import argparse
import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REP = ROOT / "reports"
SKIP_DIRS = {"__pycache__", ".pytest_cache", ".ipynb_checkpoints", ".cache"}
SKIP_FILES = {".DS_Store"}

RAW_NOTE = """# data/raw

The raw OULAD files are not included in this submission, to keep it small; they are published under CC BY 4.0
(DOI 10.6084/m9.figshare.5081998.v1). The package's first step downloads the archive, checks every table against
its pinned SHA-256 and places the seven CSV tables here: {how}

Dữ liệu gốc OULAD không được đính kèm để bài nộp gọn nhẹ. Bước đầu tiên của gói sẽ tải bộ dữ liệu công khai, đối
chiếu mã SHA-256 đã ghi sẵn và đặt bảy tệp CSV vào thư mục này: {how}
"""
INTERIM_NOTE = """# data/interim

Intermediate files are rebuilt by the pipeline ({how}) and are not included in this submission.

Các tệp trung gian được quy trình dựng lại ({how}) nên không được đính kèm.
"""


def copy_tree(src, dst, skip_rel=()):
    """Copy src to dst, leaving out caches and the relative paths in skip_rel (their folders are kept empty)."""
    for p in sorted(src.rglob("*")):
        rel = p.relative_to(src)
        if any(part in SKIP_DIRS for part in rel.parts) or p.name in SKIP_FILES:
            continue
        if any(rel == Path(s) or Path(s) in rel.parents for s in skip_rel):
            continue
        out = dst / rel
        if p.is_dir():
            out.mkdir(parents=True, exist_ok=True)
        else:
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, out)
    for s in skip_rel:
        (dst / s).mkdir(parents=True, exist_ok=True)


def redact_machine_paths(out):
    """Run logs record the interpreter's absolute path; replace this machine's repository prefix so no home
    folder travels with the submission (the logs in the repository keep their original text)."""
    prefix = str(ROOT)
    pkg_python = re.compile(re.escape(prefix) + r"/reports/milestone-\d/package/(?:\.\./)+venv/bin/python")
    for p in out.rglob("*"):
        if p.is_file() and p.suffix in {".log", ".txt", ".md", ".json", ".csv"}:
            t = p.read_text(errors="strict")
            new = pkg_python.sub("python", t).replace(prefix + "/venv/bin/python", "python").replace(prefix + "/", "")
            if new != t:
                p.write_text(new)


def zip_folder(folder, zip_path):
    """ZIP the folder itself (its name is the top entry), in sorted order."""
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(folder.rglob("*")):
            arc = p.relative_to(folder.parent).as_posix()
            if p.is_dir():
                z.writestr(arc + "/", "")
            else:
                z.write(p, arc)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "submission"))
    out = Path(ap.parse_args().out).resolve()
    if out.exists():
        shutil.rmtree(out)
    proj = out / "N04_Project"
    code = proj / "N04_SourceCode"
    proj.mkdir(parents=True)

    for m in range(1, 6):                                   # five Word reports, renamed N04_MilestoneP<n>.docx
        shutil.copy2(REP / f"milestone-{m}/build/N04_Milestone{m}_VI.docx", proj / f"N04_MilestoneP{m}.docx")
    shutil.copy2(REP / "milestone-5/build/N04_Milestone5_Slides-30_VI.pptx", proj / "N04_Project.pptx")

    p2 = code / "N04_MilestoneP2"
    copy_tree(REP / "milestone-2/package", p2, skip_rel=["data/raw"])
    (p2 / "data/raw/README.md").write_text(RAW_NOTE.format(how="`python src/collect.py`."))

    p3 = code / "N04_MilestoneP3"
    copy_tree(REP / "milestone-3/package", p3, skip_rel=["data/raw", "data/interim"])
    (p3 / "data/raw/README.md").write_text(RAW_NOTE.format(how="`bash src/run_all.sh` (step 00)."))
    (p3 / "data/interim/README.md").write_text(INTERIM_NOTE.format(how="`bash src/run_all.sh`"))

    p5 = code / "N04_MilestoneP5"
    copy_tree(REP / "milestone-5/package", p5, skip_rel=["data/raw", "data/interim"])
    (p5 / "data/raw/README.md").write_text(RAW_NOTE.format(how="`bash run_all.sh` (step 00)."))
    (p5 / "data/interim/README.md").write_text(INTERIM_NOTE.format(how="`bash run_all.sh`"))

    redact_machine_paths(proj)
    zip_path = out / "N04_Project.zip"
    zip_folder(proj, zip_path)
    shutil.copy2(REP / "self-assessment/build/N04_SelfAssessment_VI.docx", out / "N04_SelfAssessment_VI.docx")

    files = sorted(p for p in proj.rglob("*") if p.is_file())
    size = sum(p.stat().st_size for p in files)
    print(f"wrote {proj} : {len(files)} files, {size / 1e6:.1f} MB")
    print(f"wrote {zip_path} : {zip_path.stat().st_size / 1e6:.1f} MB")


if __name__ == "__main__":
    main()

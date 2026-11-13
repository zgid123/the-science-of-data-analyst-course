# build-submission

Builds the course submission as the submission instructions ask: five Word reports, one presentation and the source
code, every file named `<group code>_<assignment code>`, all in the folder `N04_Project/`, zipped as
`N04_Project.zip`. The self-assessment form is copied next to the ZIP, outside it.

```text
submission/
  N04_Project/
    N04_MilestoneP1.docx … N04_MilestoneP5.docx   Vietnamese report of each milestone
    N04_Project.pptx                              Vietnamese 30-slide presentation
    N04_SourceCode/
      N04_MilestoneP2/   Data Collection Package (brief sections 9.1 and 15)
      N04_MilestoneP3/   Prepared Data Package (brief sections 10.1 and 16)
      N04_MilestoneP5/   Final Project Package (brief section 7)
  N04_Project.zip
  N04_SelfAssessment_VI.docx
```

Raw and intermediate data are left out (each package fetches the pinned public download in its first step), and
machine paths in run logs are replaced in the copy.

```bash
venv/bin/python scripts/build-submission/build_submission.py   # -> submission/ (recreated from scratch)
```

`logs/` holds the build log and the clean-copy tests of the three code packages.

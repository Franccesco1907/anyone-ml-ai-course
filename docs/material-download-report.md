# Course material acquisition report

The six courses and all **133 lesson shells** have been reconciled against their resource links. The private library contains **214 verified course and supporting files**, plus **one private learner-submission archive**: **215 unique files, 2,550,322,462 bytes (2.55 GB)**. Acquisition date: October 13, 2026.

The public repository contains the English course structure, sanitized catalogs, study workflow, and templates for original notes, questions, practice, and progress. Course originals and authenticated links are stored in the sibling `anyoneai-private-library/` directory.

## Open a study session

1. Open `../anyoneai-private-library/study-index.md` locally.
2. Choose a lesson and open its local PDF, notebook, dataset, or extracted project. Use the separate editable copy when available.
3. Record your attempt and questions with the [study templates](../templates/README.md). Publish your own explanation and practice in the matching course folder.

The index retains academy links for streaming resources and assessment pages. Downloading and format validation do not establish understanding or a runnable notebook environment.

## Verified files

| Format | Unique files |
|--------|-------------:|
| Jupyter notebooks | 109 |
| PDFs | 51 |
| CSV datasets | 33 |
| ZIP archives | 10 |
| TAR.GZ archive | 1 |
| SQLite databases | 2 |
| Text files | 3 |
| JPEG images | 3 |
| DOCX template | 1 |
| SQL example | 1 |
| JSON collection | 1 |

The ZIP count includes the learner-submission archive, which remains private and separate from starter materials. Slide presentations supplied as PDF are labeled PDF; no native PPTX is claimed.

| Course | Lessons checked | Verified files accessible from its lessons |
|--------|----------------:|------------------------------------------:|
| Career prep | 13 | 25 |
| ML Foundations | 36 | 61 |
| Data Science | 40 | 50 |
| Deep Learning and GenAI | 26 | 70 |
| Job preparation | 7 | 4 |
| Technical challenge | 11 | 6 |

These course counts overlap: the same Black Friday dataset serves Data Science and ML Foundations. The library stores one canonical copy. Six duplicate resource records retain their lesson associations through verified canonical files; the catalog has **230 lesson-to-file references**.

## Coverage and exceptions

[materials.csv](../resources/materials.csv) contains **349 resource outcomes**: 215 unique verified files, 36 retained HTML page snapshots, six canonical aliases, 21 online-only resources, 70 reference-only resources, and one failed transfer. [material-coverage.csv](../resources/material-coverage.csv) covers all 133 lessons, including read-only assessment attachment checks. Plain-text captures for all 133 lesson shells are also retained privately and are counted separately from downloaded originals.

- **One supporting illustration remains unavailable:** the Requests logo linked from a Data Science notebook returned HTTP 429 on two attempts. The private manifest retains its source and retry action. The notebook itself is verified.
- **Online-only resources:** streaming videos and interactive services remain linked. The inspected players offered no download or caption controls; no offline video copy is claimed.
- **Runtime dependencies:** static scans recorded dataset/model loaders and external APIs. Explicit downloadable course dependencies were collected except the illustration above. Model caches, runtime-managed datasets, Python environments, and credentials were not installed or provisioned; notebooks were not executed.
- **Shared personal documents:** a cohort resume folder is recorded as a reference. Only the existing submission offered to the signed-in learner was retained privately; other learners' resumes and submissions were excluded.

**Accounting is complete for discovered resources. Download acquisition has one documented exception, and the library is not fully offline.** Refresh these point-in-time records when the course changes.

## Integrity and working copies

Verified files have byte counts, SHA-256 checksums, source associations, and retrieval/verification timestamps in the private manifests. Provider sizes or HTTP transfer lengths were checked when exposed. PDFs, notebook JSON, CSVs, document containers, SQLite databases, images, and archives received format-appropriate checks. Original CSV encoding was preserved, including one CP1252 file.

Separate working copies contain **109 notebooks and one DOCX**. **Eleven archives** were safely extracted into separate project directories: **65,544 extracted files, 1,919,288,631 expanded bytes**. Extraction rejected unsafe paths, links, and special files; no extracted files retain executable permissions. A repeat run reused all 121 working resources without overwriting edits. No downloaded code was executed.

A video player automatically completed one Data Science lesson during inspection. Its original incomplete marker was restored; a fresh course view matched all 40 original markers (26 completed, 65%). The dashboard summary still showed 67% at the subsequent check, so the restored lesson markers are the verification evidence. No assessments were answered or submitted.

Existing assignment and Airflow work was preserved. The existing Airflow ZIP matches the downloaded original by checksum; the existing sprint submission differs from the supplied project archive and remains separate.

The public catalog checker validates asset IDs, canonical references, lesson mappings, and allowed public fields:

```sh
python3 scripts/check_material_catalog.py
```

The private index links to originals, editable notebooks, extracted projects, and academy pages. Public fields omit original filenames, private paths, authenticated URLs, and course content. The [download plan](material-download-plan.md) documents the refresh procedure.

## Backup and remaining work

**Backup was deferred by the user and has not been configured.** GitHub stores the public study workspace; it does not back up the private originals. NotebookLM ingestion has not been configured.

The remaining acquisition action is to retry the rate-limited supporting illustration later. Before studying a notebook, review its recorded dependencies and prepare its environment in a separate session. Record learning evidence after doing the work, rather than treating archive coverage as course completion.

# Download and organize the course materials

Status: **planned, not executed**. Prepared October 13, 2026.

The course hierarchy, page snapshots, and private lesson links are already organized. Original course assets have not been downloaded by this workflow. The existing local assignment and Airflow files predate the inventory and remain in their original locations.

The goal is a verified private library of every available, permitted course asset, with each file connected to its lesson. Publish original study notes and progress in GitHub; keep the downloaded course library outside the public repository.

## 1. Enumerate individual assets

Start from the private `study-index.md` and the six verified syllabuses. Revisit each lesson's resource area to enumerate individual PDFs, slide decks, notebooks, recordings, datasets, archives, templates, and supporting files. Include all files in explicitly linked course folders and paginated download lists. Record external background references separately rather than treating the entire linked website as course material.

Follow folder shortcuts once and track visited provider IDs to avoid loops. Existing captures already contain repeated notebook references, including the same file linked from different lessons. Treat those as duplicate candidates until source identity and downloaded bytes are checked.

The 133 lessons are not 133 files: one lesson can contain many assets, and several lessons can reference the same file. The nine assessment entries with sidebar-only coverage need an attachment check where accessible, without answering or submitting anything. Record a lesson with no downloadable assets explicitly.

Create a private asset manifest with these fields:

| Field group | Required information |
|-------------|----------------------|
| Identity | Stable `resource_id`, all referring lesson `source_id` values, original title and filename. |
| Retrieval | Private lesson/resource URL, provider file ID when available, retrieval method, source revision or modified date when exposed. |
| Storage | Relative local path, observed format, byte count, SHA-256 checksum, download and verification timestamps. |
| Outcome | Status, attempt count, exception reason, next action, and any known download/reuse constraints. |

Use `queued`, `downloading`, `downloaded`, `verified`, `linked-to-existing`, `online-only`, `reference-only`, `access-blocked`, and `failed` as explicit states. `Downloaded` means a file exists; only `verified` means the format checks passed. A reference to an existing file must point to a verified canonical file and retain every lesson association.

## 2. Pilot one Data Science module

Begin with the current Descriptive Statistics and Data Visualization module. Download its available assets, test naming and validation, and update the private lesson index with local-file links. Include one video and one archive from another module if the pilot lacks those formats.

Check that the archive can be reopened through the local index, that notebook dependencies are recorded, and that the manifest can resume interrupted work. Measure actual file sizes and available disk space before scaling; total storage and duration are unknown until asset enumeration, especially for videos.

## 3. Acquire each format correctly

| Resource | Acquisition and organization |
|----------|------------------------------|
| PDF | Use the source's download control or available original PDF link. Preserve the PDF; a page screenshot is not a replacement. |
| PowerPoint or Google Slides | Preserve the original PPTX when offered. Use the provider's permitted export options for cloud slides. Label a PDF export as a derivative; do not call it the native deck. |
| Jupyter, Colab, or Drive notebook | Download the actual `.ipynb` using the provider's download/export option. Record paired datasets, dependency files, and supporting modules. Keep a separate working copy for later study. |
| Video or audio | Use an available permitted download option and retain offered captions/transcripts alongside it. If only streaming access is available, record `online-only` with its lesson link and any available authorized transcript. Do not promise an offline video copy. |
| ZIP or project bundle | Preserve the original archive; create a separate extracted working copy after archive validation. Record the connection between the archive and its contents. |
| DOCX or other document | Preserve the supplied file. For native cloud documents, use available DOCX/PDF exports and label their origin. Keep personal resume edits in a separate private working copy. |
| Dataset, code, or repository | Retain required course files, attribution, and supplied dependency instructions. Record a repository revision where relevant. Register large or separately licensed data as a distinct dependency. |
| Web lesson or external reference | Retain an allowed export or the existing private page snapshot with its source URL. Treat external references without an offline asset as `reference-only`. |

Use the existing authenticated browser session for download flows that require it. Refresh expired links from their lesson rather than repeatedly retrying a stale URL. Do not store browser cookies or credentials in the manifest. Do not execute downloaded notebooks or installation scripts during acquisition.

## 4. Organize and deduplicate

Use this proposed layout inside the existing private library; these download directories do not exist as a completed archive yet:

```text
anyoneai-private-library/
├── README.md
├── study-index.md
├── inventory/                       # Existing inspection evidence
├── assets.csv                       # Asset manifest to create
├── staging/                         # Incomplete transfers, grouped by worker
├── originals/
│   └── <course-slug>/
│       └── <module-slug>/
│           └── <lesson-source-id>/
│               └── <resource-id>--<readable-name>.<ext>
├── working/                         # Editable copies and extracted projects
├── derivatives/                     # Explicit exports and study conversions
└── reports/                         # Coverage, failures, integrity, and backup results
```

Reuse the repository's actual course/module slugs and lesson IDs. Preserve original filenames in the manifest, use readable local names, and distinguish revised files instead of overwriting an earlier version silently. Keep the archive originals unchanged when editing or converting material.

Deduplicate source references by provider file ID first and downloaded bytes by checksum second. Keep one canonical file with all its referring lessons. A changed revision or a different export format is a separate version or derivative, not an automatic duplicate.

Compare the existing `assignment-09-01/`, `dags/`, and their duplicate ZIP archives before downloading matching resources again. Reuse a local file only after checking its identity and version; do not delete or overwrite the existing work.

## 5. Download in resumable batches

After the pilot, finish Data Science, then ML Foundations and Deep Learning/GenAI. Collect prep, career preparation, and technical-challenge materials in additional batches. This is an acquisition priority, not a required learning sequence.

Use up to three course workers with separate browser tabs, staging folders, and worker manifests. Start with one transfer per worker and only one large video transfer at a time. The coordinator merges manifest updates and resolves duplicates, so workers never write the same destination or shared manifest concurrently.

Save progress after every verified asset. Skip verified files only when their expected source version and local checksum still match. Retry transient failures a bounded number of times; preserve failed items and their next actions for a separate pass. Continue independent downloads when one resource needs access or user action.

## 6. Verify files and reconcile coverage

Check that each response is the intended file rather than a login/error page with a misleading extension. Validate PDFs by opening/parsing them and recording page counts; notebooks by parsing their JSON and notebook structure; DOCX/PPTX and archives by checking their containers; and video/audio by checking decodable tracks and duration. These checks establish file integrity, not that a notebook's code is correct or its environment is ready.

Compute size and checksum after the transfer finishes and compare reliable source byte counts or checksums when available; a locally computed hash alone does not prove that a transfer is complete. Then move the verified file out of staging. Check every local-file link in the private study index. Reconcile the final asset manifest against the lesson inventory so a lesson with several attachments cannot be mistaken for complete after downloading just one.

Report unique verified files, lesson-to-file references, bytes stored, reused duplicates, online-only resources, reference-only items, access blocks, and failures separately. A complete accounting is not the same as a complete offline archive. Do not label the download job complete while downloadable assets remain queued, failed, or blocked.

Use separate outcome labels: **accounting complete** means every discovered resource has a verified file or a documented exception; **downloadable archive complete** means all permitted downloadable assets are verified with no unresolved transfers; **fully offline** additionally means no required course material remains available only online. Optional external background references do not count as required course assets.

## 7. Connect the library to study and backup

Add local-file links beside academy links in the private study index. Keep [GitHub notes and questions](../templates/README.md) connected through the same source IDs. Publish only sanitized counts and original learning evidence; private URLs and course originals remain local.

Prepare NotebookLM sources only from materials permitted for upload. Keep conversions under `derivatives/`, retain originals, and start with the current module. NotebookLM ingestion is a separate follow-up, not a substitute for downloading and backing up the files.

Choose a private backup destination with enough capacity, copy the library and manifests, and verify a sample restore plus checksum comparisons. No backup destination has been selected or configured by this plan.

## Delivery checklist

- [ ] Every lesson is reconciled against its individual assets or an explicit no-assets record.
- [ ] Every downloadable asset is verified or has a visible unresolved exception and next action.
- [ ] Duplicate references resolve to verified canonical files; revisions and derivatives remain distinguishable.
- [ ] The private index opens local originals and retains the corresponding academy references.
- [ ] Existing local work is preserved, and original files are separate from editable working copies.
- [ ] Counts distinguish verified files, online-only resources, blocked assets, and failed downloads.
- [ ] Backup and restore checks are recorded before claiming the archive is backed up.

The next execution step is asset enumeration and the Data Science pilot. This document creates the plan only; it does not start downloads, upload files to NotebookLM, or configure a backup.

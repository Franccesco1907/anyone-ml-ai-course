# Observed course resources

[sources.csv](sources.csv) combines the six course syllabuses. Each row identifies a lesson page; it is not a downloaded lesson or an individual attachment. Use its stable `source_id` in your notes and questions to connect public learning evidence to the private source index.

| Field | Meaning |
|-------|---------|
| `source_id` | Stable reference based on the platform lesson ID. |
| `course_slug` | Folder under `courses/`. |
| `module_order`, `module_title` | Observed module position and title. |
| `lesson_order`, `lesson_title` | Observed lesson position within its module and title. |
| `title`, `kind`, `language` | Lesson title, normalized platform content kind, and course language. Original kind labels remain in each course syllabus. |
| `platform_status` | Completion state observed during the inventory, separate from understanding. |
| `resource_formats` | Formats or link types observed for that lesson; a notebook link does not prove its contents were downloaded or executed. |
| `inspection_status` | Whether the lesson was indexed only or its resource page was inspected. |
| `public_url`, `access`, `reuse_permission` | Access metadata. Authenticated URLs are omitted; an empty permission field grants no redistribution rights. |
| `notes` | Brief context about the reference. |

The per-course `syllabus.csv` files are the editable source of this catalog. After updating them from observed platform information, run this command from the repository root:

```sh
python3 scripts/rebuild_source_index.py
```

The script uses only Python's standard library. It does not contact the academy, download files, or change platform progress. It rebuilds the combined CSV and checks required columns and unique source IDs.

Keep authenticated links, full page captures, filenames containing personal information, and original course files in the [private library](../docs/private-library.md). The public catalog contains metadata; actual reading and practice belong in your lesson notes and learning evidence.

## Downloaded material catalog

[materials.csv](materials.csv) records individual resource outcomes using opaque asset IDs. [material-coverage.csv](material-coverage.csv) reconciles every lesson against its verified file references. Neither table contains authenticated URLs, original filenames, private paths, or course content. `linked-to-existing` points to a checksum-identical canonical asset. Page captures are labeled separately and do not count as downloaded originals. See the [acquisition report](../docs/material-download-report.md) for totals and exceptions.

Validate the public asset IDs, canonical references, privacy fields, and lesson coverage with `python3 scripts/check_material_catalog.py` from the repository root. This checks catalog consistency; private file integrity is checked separately against the local manifest.

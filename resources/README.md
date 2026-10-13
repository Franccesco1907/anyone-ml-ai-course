# Source inventory

[sources.csv](sources.csv) is an empty inventory for safe references to observed course resources, including those not yet studied. One row describes one source; use the same `source_id` in lesson and question notes.

| Field | What to record |
|-------|----------------|
| `source_id` | Stable ID you assign, for example `mlf-001`. |
| `course_slug` | Folder name under `courses/`. |
| `module_order`, `lesson_order` | Order actually shown in the platform; leave blank if unknown. |
| `module_title`, `lesson_title` | Actual platform names; leave blank if not yet observed. |
| `title` | Source title without copied lesson content. |
| `kind`, `language` | Video, slides, notebook, article, etc.; actual source language. |
| `public_url` | Only a publicly accessible URL without tokens or private access details. |
| `access` | Public or restricted. |
| `reuse_permission` | Known license or permission; leave blank if unknown. |
| `notes` | Brief reference context without restricted content or personal data. |

Keep private paths and restricted URLs in the separate private library index. Cite external sources used in your own work, and verify reuse rights before adding any source file to GitHub.

"""Rebuild the public source catalog from the observed course syllabuses."""

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIELDS = [
    "source_id", "course_slug", "module_order", "module_title", "lesson_order",
    "lesson_title", "title", "kind", "language", "public_url", "access",
    "reuse_permission", "notes", "platform_status", "resource_formats",
    "inspection_status",
]
REQUIRED = {
    "source_id", "module_order", "module_title", "lesson_order", "lesson_title",
    "content_kind", "platform_status", "resource_formats", "inspection_status",
}
KINDS = {
    "text": "Text", "text/resource page": "Text", "pdf": "PDF",
    "pdf presentation page": "PDF", "video": "Video",
    "recorded session": "Video", "quiz": "Quiz", "download": "Download",
    "survey": "Survey", "assignment upload": "Assignment",
}


def main():
    rows = []
    seen = set()
    syllabuses = sorted((ROOT / "courses").glob("*/syllabus.csv"))
    if not syllabuses:
        raise ValueError("No course syllabuses found; the existing catalog was preserved.")
    for syllabus in syllabuses:
        with syllabus.open(newline="", encoding="utf-8") as source:
            reader = csv.DictReader(source)
            missing = REQUIRED - set(reader.fieldnames or [])
            if missing:
                raise ValueError(f"{syllabus}: missing fields {sorted(missing)}")
            for lesson in reader:
                source_id = lesson["source_id"]
                if not source_id or source_id in seen:
                    raise ValueError(f"Missing or repeated source ID: {source_id!r}")
                seen.add(source_id)
                row = {field: lesson.get(field, "") for field in FIELDS}
                row.update(
                    course_slug=syllabus.parent.name,
                    title=lesson["lesson_title"],
                    kind=KINDS.get(lesson["content_kind"].lower(), lesson["content_kind"]),
                    language="en",
                    public_url="",
                    access="restricted",
                    reuse_permission="",
                    notes="Lesson reference only; resource links are in the private inventory.",
                )
                if row["platform_status"] == "not completed":
                    row["platform_status"] = "not marked completed"
                rows.append(row)
    destination = ROOT / "resources" / "sources.csv"
    with destination.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"Indexed {len(rows)} lessons from {len(syllabuses)} courses.")


if __name__ == "__main__":
    main()

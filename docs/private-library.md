# Keep a private source library

Store authorized course originals in a separate directory outside this repository, such as `../anyoneai-private-library/`. Organize it by the same course slugs, then by the module and lesson names shown in the platform. That directory is a private reference library, not a GitHub artifact.

## Connect references to notes

1. Download only materials you are allowed to access and retain.
2. Use the lesson's existing source ID from [sources.csv](../resources/sources.csv), such as `ds-45289394`. For a newly observed lesson, update its course syllabus and rebuild the catalog using the [inventory instructions](../resources/README.md).
3. Keep filenames, private paths, authenticated URLs, and access details in a private index outside this repository.
4. In your public note, cite the source ID and a page, timestamp, or section. Write an original explanation rather than copying source text.

The public source inventory contains the observed course hierarchy and stable lesson IDs. The sibling private library's `inventory/` directory holds authenticated page captures and resource links from the inspection. Those captures remain inspection evidence. Downloaded originals, their checksums, separate working copies, and individual resource outcomes are now recorded in the private `assets.json` and `assets.csv` manifests. See the [acquisition report](material-download-report.md); file validation does not establish that notebook environments are runnable. Match the numeric lesson ID in a public source ID to the private lesson URL when locating a resource.

Open `../anyoneai-private-library/study-index.md` locally for a clickable course and lesson index. It connects all observed lessons to local originals, private text captures, online references, the same source IDs, and the public learning folders. That private file is deliberately outside this repository.

Keep a separate copy or backup of this private library in your own storage. GitHub backs up only the public repository. Review and update the inventory after course content changes; it is not automatically synchronized with the academy.

## Use NotebookLM as a private study aid

If you choose to use NotebookLM, create a separate private notebook for each course and add only sources you are permitted to upload. Keep notebook access and original course materials private. Uploading to a service is a separate choice from keeping a local copy; check the material's sharing permissions first.

Ask a focused question tied to a source locator: “Explain this step, state its assumptions, and show a new small example.” Use the answer to inform your own notes, verify its citations against the source, and test your understanding unaided. Save your own verified explanation and practice evidence in GitHub.

Do not publish course originals or bulk exports of source text or generated summaries. Keep personal information and credentials out of both public notes and uploaded sources.

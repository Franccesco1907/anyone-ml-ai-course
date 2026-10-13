# Turn the course inventory into study evidence

Start with the current Data Science Sprint. Use its observed lesson order to choose work, and use your own exercises to check understanding. A platform completion check and a demonstrated skill are separate records.

## First session

1. Open the Data Science course index and locate Exploratory Data Analysis, the resume point observed during the inventory.
2. Try to explain the concepts from that section before opening the material. Record one specific uncertainty in a question note.
3. Work through a small original example with synthetic or appropriately licensed data. Keep assessment answers private.
4. Verify the result, write an explanation in English, and link it from the lesson and progress records.
5. Choose the next unfinished lesson using the current platform state. The inventory is a snapshot, not a live synchronization.

## Suggested study sequence

| Stage | Focus | Evidence to produce |
|-------|-------|---------------------|
| Continue Data Science | Finish the current section, then follow the remaining feature engineering and project work in platform order. | An original analysis with clearly defined metrics, a reproducible pipeline, and explanations of important decisions. |
| Study ML Foundations | Follow the observed supervised and unsupervised learning modules. Revisit prep material when a prerequisite blocks you. | A baseline, justified evaluation choices, and an explanation of errors and limitations. |
| Study Deep Learning and GenAI | Follow the verified course index and its prerequisites after the relevant foundations. | Small original experiments with recorded configurations, comparisons, and limitations. |
| Maintain career materials | Revisit the job-preparation course when a project becomes ready to present. | Accurate project descriptions and a portfolio reflecting work you can explain. |

Follow scheduled sessions and instructor requirements when they differ from this personal study sequence. Completed prep and technical-challenge items remain available for targeted review.

## A repeatable session

Spend about five minutes recalling previous work, twenty studying a focused section, twenty practicing, ten checking an explanation or asking for help, and five recording the result. Shorten the scope when less time is available. Finish one useful learning loop before adding more tools.

Copy the [session template](../templates/session.md), the [lesson template](../templates/lesson.md), and, when needed, the [question template](../templates/question.md). Keep one clear next action in each active record.

## Record a resolved doubt

Write your initial belief, attempt, and source locator before asking for help. Treat the AI answer as an explanation to verify. Resolve the question only after a fresh example or explanation from memory demonstrates the missing step. Keep unresolved questions visible; they are useful study targets.

At the next session, recall the previous idea before opening notes. Revisit it later and record the outcome, rather than assuming a finished video means lasting understanding.

## Publish a useful learning update

Choose a small piece of original work: a notebook experiment, a corrected misconception, or an explanation with a reproducible example. Preserve concise, safe outputs that support the result. State what you checked and what remains uncertain.

Review your changes with `git status` and `git diff`, stage only the files intended for publication, inspect `git diff --cached`, then commit and push. Use a message describing the learning outcome, such as `docs: explain duplicate rows after a join`. Course submissions and private source files belong in the private library.

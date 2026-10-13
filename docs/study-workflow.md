# Learn, check, and record

Use one lesson, one small practice task, and one observable result per session. Keep notes, explanations, and tutor prompts in English. Ask for plain-English explanations and then restate the idea yourself.

## Session loop

1. **Orient:** open the actual lesson, record its module/order and source ID, and choose a question to answer.
2. **Learn:** read or watch a short section. Write the idea in your own words, including assumptions and a worked example.
3. **Practice:** attempt a small analogous problem without looking at the solution. Save your code or reasoning.
4. **Check:** compare against an allowed reference or test. Record what worked and what failed.
5. **Close:** update the session and progress records, then choose one specific next action.

Name notes `notes/lesson-slug.md` and doubts `questions/question-slug.md` inside the relevant `courses/<course>/modules/<module>/` folder. Create `exercises/` there for your own practice code. Use source IDs from [the inventory](../resources/README.md), and link artifacts with relative paths.

## Resolve a doubt

Capture the exact source locator (page, slide, timestamp, section, or notebook cell), your understanding, and your attempt in [a question note](../templates/question.md). Ask an assistant or mentor to explain the smallest confusing step. Preserve English technical terms and ask for an analogous example.

Check the explanation against the source and solve a fresh example unaided. Mark the question resolved only when you can show that result; otherwise, write what remains unclear and the next experiment. Treat generated explanations as claims to verify.

## Review understanding

At the next session, try to explain or reproduce the previous idea before opening your notes. Schedule a later review if recall is weak. Keep activity status (`not recorded`, `in progress`, `completed`) separate from understanding (`not assessed`, `needs practice`, `demonstrated`).

For an understanding claim, link a concrete result: an explanation from memory, a solved exercise, a tested implementation, or a project evaluation. Platform completion alone is not enough.

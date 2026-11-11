# Project instructions

## Purpose

Build an evidence-backed understanding of Andrej Karpathy's public work and how his thinking develops. Preserve the distinction between his statements, our interpretation, user decisions, and completed work. Cite original sources and timestamps where available; do not imply exhaustive coverage or verified claims from discovery alone.

## System design and architecture decisions

For changes to systems, workflows, AI agents, prompts, context files, or software architecture, evaluate both paths:

1. **Incremental improvement:** inspect current tools and capabilities, files and workflows, migration cost, maintenance burden, adoption friction, and the immediate bottleneck. Propose the smallest material improvement. Prefer it when the system works, the problem is local, or redesign benefits are uncertain.
2. **Optimal architecture:** separately explain the ideal long-term design, why it is better, problems it solves, additional complexity, and when migration is justified. Do not assume it should be implemented now.

Optimize expected value: improvement benefit minus implementation cost minus complexity cost. Avoid both ignoring structural problems and building unvalidated abstractions. State the recommended next action, why now, why not the larger redesign yet, and the future migration signal.

Maintain a coherent mental model rather than maximizing file count. Split information only for meaningful differences in update frequency, ownership, context conflict, multi-agent use, or retrieval accuracy.

## Session startup

1. Read `project-management/STATUS.md` before substantive project work.
2. Read its linked latest session log for a new session or after losing context. In an ongoing session, do not repeatedly reread unchanged logs.
3. Search older logs only when the current task depends on a prior decision, rationale, unresolved question, or conflicting state. Read the relevant matches, not the entire history.
4. Verify the relevant actual artifacts before relying on historical completion claims. Logs provide context, not proof of current source coverage or file state.

## Automatic session logging

- Maintain one log per continuous conversation/session under `project-management/sessions/`. Reuse the same log across turns, topic changes, and context compaction. A genuinely separate conversation gets a new log.
- Name new logs `YYYY-MM-DD-NN-short-topic.md`, using Asia/Shanghai dates and the next unused daily sequence. Do not overwrite a different session's log.
- Write a checkpoint after meaningful work and before each substantive final response, without asking the user to remind or approve routine logging. Discussion-only sessions count: record reasoning and proposals without inventing implementation progress.
- Update the same log as the conversation continues. Preserve important earlier decisions and record later corrections or superseding decisions explicitly.
- Update `STATUS.md` with current stage, confirmed decisions, outstanding work, recommended next action, and a link to the latest checkpoint. Keep it concise; detailed history belongs in session logs.
- At an explicit session close, write a final handoff and mark the log closed. Otherwise mark it checkpointed, not closed. If interrupted, resume from the latest saved checkpoint and verify unfinished work.
- This is instruction-driven agent behavior, not a background service or shutdown hook. It cannot guarantee a final write after a crash, abrupt closure, tool failure, or a session that does not load these instructions. Report any failed log write.

## Session log contents

Use these sections in each log (no separate template required):

- Date/timezone, session state, and objective.
- Work performed: distinguish discussion, research, implementation, and verification.
- Project contribution: area improved, before/after, and supporting artifact or evidence. If no substantive improvement occurred, say so.
- Decisions: user-confirmed versus proposed; retain reasons and important rejected alternatives.
- Files changed: relative links and purposes.
- Verification and limitations: checks actually performed, missing evidence, interruptions.
- Handoff: remaining work, open questions, and a concrete next action.

Keep logs factual and concise. Do not copy full chat transcripts, credentials, or unrelated private information. Keep research content in research artifacts when they exist; link it from logs.

## Filing explanations

When the user asks what a term, idea or question means, save the answer as one file in `notes/` (private, gitignored) and add a row to `notes/README.md`. Include his dated sources and keep explanation separate from the user's beliefs, which go in `LEARNING.md`.

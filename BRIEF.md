# Project brief

The working brief for this project: purpose, scope, evidence rules and file design. Moved here from README.md on 2026-11-11 so the README can introduce the site.

## Purpose

This project builds an independent, evidence-based understanding of AI: its capabilities, limits, human purpose, and implications for building products alone. The owner's personal motivation is kept in a private learning record. It is not a verified summary of Karpathy's beliefs. Research should preserve disagreement, uncertainty, and counterexamples rather than validate a predetermined conclusion.

## Primary deliverable

A readable, evidence-backed chronicle of how Karpathy's publicly expressed understanding and practice developed over recent years. Explain continuity as well as change: what he said, demonstrated, revised, or left unresolved, and what evidence supports each interpretation.

The chronicle should connect four recurring threads:

1. Understanding AI fundamentals, capabilities, and limitations.
2. Philosophy of using AI and the role of human judgment and agency.
3. Coding with AI: problem decomposition, organizing thinking, implementation, testing, and review.
4. Engineering and project practices: choosing projects, managing scope, iterating, and learning through personally useful work.

These are research lenses, not claims that he has a formal framework for each. Distinguish frameworks he explicitly names from patterns we infer. Public communication reveals expressed understanding; it cannot establish exactly when he privately learned something or prove that every later statement represents deeper knowledge.

## Scope

- His own YouTube material, interviews on other channels, recorded speeches/talks and associated Q&A, and official X posts, threads, and substantive replies across recent years.
- Aim for broad inventory and review of the specified corpus. The earlier 3–5 and 10–15 source pilot proposals are not collection limits or prerequisites for the project.
- Use older foundational material and linked writing or project artifacts where necessary to explain origins or verify an interpretation. Do not silently expand into exhaustive collection of all repositories or publications.
- Working date assumption, still unconfirmed: 2022 onward, with earlier foundational sources where needed. Establish actual source counts and access gaps during inventory; do not assume the corpus is either trivial or impractical before inspecting it.
- Record inaccessible, partial, duplicate, and unreviewed items. Coverage claims must be bounded by channel, period, and discovery method.

## Chronicle format and evidence

Organize the primary narrative chronologically, with periods derived from evidence rather than an invented progression. Within each period explain: context and problems; public statements and demonstrated work; reasoning and practices; continuity or change relative to earlier evidence; uncertainties; implications for the user's own thinking.

Support substantive claims with original links and timestamps or post references. Separate exact quotation, paraphrase, our inference, and personal takeaways. Preserve event versus publication dates where different. Repeated claims and reuploaded clips are not independent evidence of development. A later public explanation alone does not establish a new private discovery or the cause of a changed view.

## Personal development

The longer-term aim is the user's capacity to create and maintain a one-person AI product or business. The chronicle supplies conceptual grounding and practices to examine; it does not itself prove entrepreneurial capability. Personal beliefs, disagreements, and optional experiments belong in `LEARNING.md`, linked back to evidence. Practical exercises should support, not replace, the requested chronicle.

## Success criteria

- The user can follow the development of his publicly expressed ideas over time and find the evidence for important transitions.
- The four research threads remain connected within a coherent narrative rather than becoming isolated summaries.
- Stable principles, new tools, changed practices, and revised beliefs are distinguished.
- The reader can tell his statements from our interpretations, and evaluate where the user's own beliefs align or diverge.
- Coverage and uncertainty are visible; neither completeness nor a steadily deepening worldview is fabricated.

Failure would be a collection of disconnected summaries, an uncritical endorsement of a role model, a chronology supported only by publication dates, or project administration that displaces research.

## Minimal file design

| Path | Purpose | State |
|---|---|---|
| `README.md` | Product brief, scope, and acceptance criteria | Created |
| `AGENTS.md` | Evidence rules and session continuity instructions | Created |
| `sources.jsonl` | Source inventory and processing/coverage status | Initial inventory created; incomplete |
| `CHRONICLE.md` | Main chronological narrative, with thematic navigation | Provisional evidence-backed outline; replaces proposed `SYNTHESIS.md` |
| `LEARNING.md` | User's evolving beliefs, disagreements, and applications | Started (2022 discussion) |
| `sources/` | Source archives, provenance and coverage notes | X archive plus video catalogue and 22 recording-related texts |
| `materials/` | Captions, transcripts, slides where useful and accessible | Optional |
| `project-management/STATUS.md` | Current project state and next action | Created |
| `project-management/sessions/` | One log per continuous session | Created |

## Next work and architecture decision

Replanned 2026-11-06 following inspection of the X archive. The following is the assistant's recommended research sequence, not a claim of completed review or user-approved interpretations.

Collection update: the user explicitly requested full video/talk/interview discovery rather than sample-first work. The [video catalogue](sources/videos/README.md) now records current channel/playlist enumeration, external appearances, 22 saved texts, and outstanding gaps. The register has 77 records, including older context and non-speech artifacts; these are not 77 reviewed works.

The earlier 36 items were initial mixed-source candidates (12 official videos, 9 external interviews/talks, 8 X posts, 7 writings), never the intended corpus limit. The eight X candidates overlap the 1,012-post archive. There are 868 archived posts from 2022 onward and 144 earlier context posts; the remaining 28 registered non-X candidates are not yet a complete inventory or a fully retrieved collection.

1. **Read across the archive before fixing the story.** First-pass all 868 posts from 2022 onward in chronological batches; screen the 144 older posts for explanatory context. Record reviewed IDs/ranges and unresolved items in the existing evidence note so skipped or unread items remain visible. Capture relevant statements under the four research lenses, allowing additional themes to emerge. Give brief disposition reasons for off-topic, duplicate, or context-only material; keyword search is an aid, not a substitute for reading. Batch size is operational, not a scope limit.
2. **Deepen the evidence where it matters.** Closely examine substantive claims, qualifications, contradictions, recurring principles, and descriptions of actual practice. Trace thread parents, quoted material and linked projects when needed to understand a claim. Retain original post IDs, dates, exact wording versus paraphrase, and interpretation separately. Do not equate likes or length with significance. Distinguish changed tools, changed practices and changed beliefs.
3. **Integrate other channels by period.** Continue broad video/interview/talk inventory and retrieve available original transcripts/captions. Read full relevant sources, preserving review extent and timestamps; compare them with contemporaneous X evidence. Avoid treating crossposts as independent corroboration. Missing transcripts, replies or media remain explicit gaps rather than grounds to infer silence.
4. **Rewrite the chronicle from evidence.** Revise provisional period boundaries and arguments in CHRONICLE.md after the broad X pass and period-level cross-channel checks. Each period connects context, expressed ideas, demonstrated practice, continuity/change, counterevidence and unresolved questions. Produce a readable narrative rather than 1,012 disconnected summaries. Partial drafts are allowed when their coverage is stated.
5. **Develop personal takeaways through discussion.** Use the narrative to examine alignment, disagreement and possible applications to independent product building. Create LEARNING.md when there is actual user belief/application content; assistant proposals must remain distinct from user decisions.

**Recommended next action:** begin the chronological X first pass with 2022, continuing across all years before treating any proposed intellectual progression as settled. Retrieve early video/interview evidence alongside the broader research sequence. Immediate bottleneck: reading and connecting evidence, with non-X retrieval still incomplete.

**Incremental path (recommended now):** retain the archive and current Markdown/JSONL structure. Keep post-level coverage and evidence locators in the existing inventory/evidence note; keep selected narrative anchors in sources.jsonl and cite archived posts directly by stable ID. Do not duplicate every post body in the top-level register or create one file per post. Existing tools can parse/search the archive; this has low migration cost, little adoption friction and modest maintenance burden.

**Long-term architecture:** a linked source/claim store with full-text search, explicit source relationships and review history would make retrieval, contradiction checks and citation updates easier. It adds schema design, ingestion, synchronization and maintenance costs. Migrate when repeated missed evidence, conflicting review states, frequent corpus updates or multiple reviewers make those costs lower than continuing with files. The current corpus size alone does not establish that need.


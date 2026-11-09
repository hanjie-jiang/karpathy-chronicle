# Source inventory and first evidence notes

Checked: 2026-11-06, Asia/Shanghai. Register: [sources.jsonl](../sources.jsonl). Narrative: [CHRONICLE.md](../CHRONICLE.md).

## Scope and counting

The agreed corpus remains official YouTube, external interviews, recorded talks and Q&A, and official X posts, threads and substantive replies. January 2022 onward is a working assumption, not a confirmed cutoff. Older writing and linked project artifacts are supporting context, not a new exhaustive collection obligation. This discovery batch is neither a source cap nor a completed inventory.

39 records: **36 substantive source candidates + 3 discovery hubs**. The 36 comprise 12 official videos, 5 external interviews, 4 talks, 8 X posts and 7 supporting writings. Six writings have body-text review; two interviews have excerpt review; 28 substantive candidates remain unreviewed. No complete video/audio review has occurred. Index inspection is not content review. No independent second review has occurred.

| Working year | Official videos | Interviews/talks | X candidates | Supporting writings | Total |
|---|---:|---:|---:|---:|---:|
| 2019, context only | 0 | 0 | 0 | 1 | 1 |
| 2022 | 6 | 1 | 0 | 0 | 7 |
| 2023 | 2 | 1 | 1 | 0 | 4 |
| 2024 | 2 | 3 | 1 | 1 | 7 |
| 2025 | 2 | 2 | 4 | 4 | 12 |
| 2026 through Nov 6 | 0 | 2 | 2 | 1 | 5 |

Year placement is partly provisional; see each record's `date_basis` and `year_status`. Zero means no candidate registered in this pass, not no publication. These are register counts, not corpus totals or coverage percentages.

## Discovery methods and actual gaps

- Read [official homepage](https://karpathy.ai/), [course syllabus](https://karpathy.ai/zero-to-hero.html), and [Bear blog index](https://karpathy.bearblog.dev/blog/). Extracted homepage HTML links to recover featured recordings omitted by the text renderer. The syllabus yielded eight lecture links; homepage and search added four official videos. The homepage is curated and acknowledges outdated sections.
- Opened the [official channel Videos page](https://www.youtube.com/@AndrejKarpathy/videos): extraction returned a shell, with a stale crawl indicator. Full upload, Shorts, live and playlist enumeration remains undone. A [secondary channel index](https://prepublish.ai/youtube-channel/andrejkarpathy) aided year placement only; its claimed 17 uploads is not a verified denominator.
- Featured interviews/talks were mapped for 2022–2025; search and the author's blog identified two 2026 interviews. External appearances beyond featured links remain open. Dates, recording boundaries, Q&A, clips and repeated appearances need reconciliation.
- X search pass used `site.x.com/karpathy/status/` with 2022/Copilot, 2023/English, 2024/Eureka, 2025/vibe coding and 2026 terms, then followed links from original articles and secondary discovery pages. No identifiable 2022 post was registered; this is a gap. Search results were noisy and often secondary.
- The X profile and six registered post URLs returned 403; two other registered URLs were discovery-only. No account pagination, annual completeness, thread reconstruction, or substantive reply sweep was achieved. **Zero X bodies reviewed.** Crosslinked blog bodies do not establish complete X content or comments.
- Lex's episode page loaded, but attempted transcript URLs failed. State of GPT's linked PDF unexpectedly rendered as the homepage, and an attempted Microsoft Learn endpoint failed. These failures do not show that the originals are unavailable to a human reader.
- The 2026-10-31 HackerTube entry demonstrates recent publication activity; its body has not been reviewed. No inference that the period after April is empty is warranted.

## Register semantics and deduplication

`metadata_status` distinguishes an original link confirmed on a primary page from a secondary lead. `retrieval_status` distinguishes body access, partial text, metadata, blocked and not attempted. `review_status` records unreviewed, reviewed excerpt, reviewed text, or index inspection. `review_extent` bounds the actual reading. Text review does not independently verify the truth of an author's claims.

Unknown dates are null. `publication_date` records the available primary publication/release date, with its basis; it is not automatically the event date. `inventory_year` is a sorting aid. T09 has a companion article date separate from unknown video/event dates. Retrieval used both search-engine cached text and direct official HTML; not every page was fetched live from origin.

Canonical video IDs collapse URL variants. T07 host transcript and YouTube are one appearance; T09 video and author-edited companion text are one appearance. The official homepage and syllabus are discovery hubs, not new corroboration for every link. X02/A02, X04/A04 and X05/A05 are related crossposts; keep their identities but do not treat them as independent confirmations. No exact duplicate URL remains among the 39 canonical records; this does not establish complete semantic deduplication of the corpus.

No Priors 2024 has conflicting episode numbering (YouTube 80; podcast metadata 77); use the appearance identity rather than episode number. GPU Mode links to 00:54:06 within a combined recording; Berkeley links to 00:04:05 within an awards recording. End times and Q&A remain unreviewed.

## Evidence notes

### A01

[A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/), 2019-04-25. Full rendered article read; code not executed.

Paraphrase: the opening identifies leaky abstractions and silent failures. “The recipe,” steps 1–2, recommends inspecting data and establishing a simple, trustworthy evaluation skeleton before adding complexity. Step 2 also describes implementing a specific case before generalizing it.

Interpretation: this supplies an earlier engineering baseline against which later AI-assisted work can be compared. It does not establish an unchanged philosophy across all domains. The 2019 recommendations on supervised learning are historically situated, not timeless advice.

### Y01 / Y07 / H02

[Syllabus](https://karpathy.ai/zero-to-hero.html); [micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0); [build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY). Originally metadata/description only. Update 2026-11-06: machine transcripts are now saved locally. Y07 has one reviewed passage (Copilot, about 00:59:03–00:59:46); Y01 remains unread. See [review ledger](review-ledger.md).

Paraphrase of official descriptions: the course develops neural networks through implementation; the GPT lesson explicitly includes Copilot assistance. Micrograd's publisher chapter list locates a shared-node backprop bug at 01:22:28 and PyTorch comparison at 01:39:31. These are review targets, not watched segments. Publication dates were found in indexed original YouTube metadata: 2022-08-16 and 2023-01-17.

Interpretation to test: mechanism-level teaching and AI coding assistance may coexist already in early 2023. This is a course-design observation, not a demonstrated intellectual turning point.

### A02

[Introducing Eureka Labs](https://eurekalabs.ai/), dated 2024-07-16. Entire announcement body read.

Paraphrase: the stated plan couples teacher-designed material with an AI assistant guiding learners, and names LLM101n as the first intended product. Locate paragraphs beginning “However” and “Our first product.”

Boundary: this is an organization's announced design and aspiration, not evidence that the platform shipped or improved learning outcomes. It supports researching human/AI division of labor; it does not prove every Karpathy project follows this model.

### A03

[The append-and-review note](https://karpathy.bearblog.dev/the-append-and-review-note/), 2025-03-19. Entire body read.

Paraphrase: he describes one note with new items placed at the top and periodic review that promotes or combines material. See “Data structure,” “Append,” and “Review.” He says he has used this approach for years.

Boundary: publication in March 2025 is not the method's invention date. This is a personal thought-management practice; the article does not make it an AI-memory architecture or prove universal superiority.

### A04

[Power to the people](https://karpathy.bearblog.dev/power-to-the-people/), 2025-04-07. Entire body read.

Paraphrase: he argues accessible, broad but fallible capabilities can expand individuals' reach, while organizational coordination and reliability constrain adoption. Final substantive paragraphs ask whether expensive intelligence could later concentrate benefits.

Boundary: this is a dated distributional thesis, not independently verified economic measurement. It provides specific evidence relevant to the user's interest in empowerment, including a countervailing possibility; it does not warrant declaring complete value alignment.

### A05

[Vibe coding MenuGen](https://karpathy.bearblog.dev/vibe-coding-menugen/), 2025-04-27. Entire body read; app, code and finances not tested.

Paraphrase: a personal need led to a fast local prototype, followed by integration and deployment difficulties. The “Stripe payments” paragraph reports catching an email-based identity-matching mistake. “Database? Work queues?” leaves further infrastructure unfinished; the conclusion limits suitability for important uses.

Interpretation: this case separates generation speed from delivery quality and continuing human judgment. A working paid interface and markup intention do not establish actual revenue or a sustainable one-person business.

### T07

[Dwarkesh host transcript](https://www.dwarkesh.com/p/andrej-karpathy), 2025-10-17. Reviewed opening through 00:23:59 only, without audio comparison.

Paraphrase: at 00:00:07–00:02:57 he distinguishes useful current agents from dependable employee-like systems and calls the decade estimate intuition. At 00:17:46 he contrasts compressed training knowledge with directly available context; at 00:22:07 he discusses missing experience consolidation.

Boundary: these are his judgments and analogies, not verified capability measurements or a measured forecast. Later RL, economics and education sections remain unreviewed. Current-agent usefulness and broader skepticism coexist in the opening; “he rejected agents” would misrepresent it.

### A06

[2025 LLM Year in Review](https://karpathy.bearblog.dev/year-in-review-2025/), 2025-12-19. Entire article body read; linked projects not audited.

Paraphrase: sections 1–2 connect verifiable-reward training with uneven capabilities and express distrust of benchmark interpretation. Sections 3–4 discuss application orchestration and agents integrated with the user's working environment. He frames these as personally notable developments.

Boundary: his retrospective is evidence of an explicitly stated assessment. It does not independently verify the industry-wide claims. Its linkage to his YC talk is useful for follow-up but does not replace reviewing that recording.

### T09

[Sequoia companion text](https://karpathy.bearblog.dev/sequoia-ascent-2026/), 2026-04-30; [original video](https://www.youtube.com/watch?v=96jN2OCOfLs). Partial review only.

Provenance: Karpathy says an LLM used recent writing plus the transcript to produce a summary and cleaned transcript, which he read. Therefore summary wording may synthesize other sources. Under the edited transcript's “The December 2025 Agentic Inflection,” he reports growing trust in larger coding actions around December. The “Software 3.0” segment describes programming through context and reconsiders MenuGen as a direct model transformation.

Boundary: author-published AI-edited text, not verbatim speech. No timestamps or audio verification yet. Treat December as a retrospective self-report, not a precisely dated universal capability change.

## Next acquisition batch, without shrinking scope

1. Resolve full official-channel enumeration and exact original dates; retrieve captions for Y01/Y07, T01/T02, then review selected passages with original timestamps.
2. Recover original X bodies and reply/thread context by year, including the empty 2022 slice; preserve inaccessible items rather than substituting reposts as primary evidence.
3. Review T04/T05 and T06 recordings, segment speaker/Q&A boundaries, then compare the 2025–2026 coding accounts against original T08/T09 audio.
4. Continue external-appearance discovery through November 2026 and inspect A07. Update this matrix as counts grow; do not infer absence from today's misses.

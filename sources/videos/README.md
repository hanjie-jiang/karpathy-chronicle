# Videos, talks and interviews: collection catalogue

Checked 2026-11-06 (Asia/Shanghai). This is a broad collection pass, not a selected-source pilot. It is an inventory and text archive, not a completed interpretive review or a claim that every public appearance has been found.

## Coverage established

- Official current Videos tab: 17 visible uploads, parsed from the actual YouTube channel response; no continuation item. All 12 educational videos plus all five Stable Diffusion demonstrations are accounted for.
- Official Zero to Hero playlist: 10 entries, reconciled against the register. It contains nine official-channel lessons plus the external Microsoft State of GPT talk; it does not add ten independent sources.
- Recent external appearances: 11 identified recordings from 2022 onward. Two missing from the old register were found: Stanford CS25 (2023), and Sequoia AI Ascent (2024). These counts describe identified appearances, not guaranteed exhaustive lifetime coverage.
- Readable text saved for all 12 educational videos (25h 20m 46s combined recording duration) and 10 of the 11 identified recent external recordings. GPU Mode is the remaining transcript gap. Text quality differs substantially; see below.
- Older context: all 15 pre-2022 featured appearances on the author homepage are recorded. The linked CS231n 2016 playlist contains 15 entries: 14 course-recording candidates retained with individual lecturer attribution unverified; the Jeff Dean guest lecture is excluded as a Karpathy appearance.
- One additional author-linked generated-video artifact, Y18, was found in the saved X corpus. It is absent from the current Videos tab and is not a recording of Karpathy speaking.

The main register is [sources.jsonl](../../sources.jsonl). [Collection checks](collection-checks.jsonl) retain enumerated lists, individual access outcomes, and saved-text SHA-256 hashes. Original X files were not changed.

## What the saved text means

- Y01-Y12, T01, T10, T11: third-party Whisper transcripts; all available timestamped segments extracted. For each of the 12 lessons, the text begins at 00:00:00 and its last segment begins within 1.4-6.48 seconds of the listed recording end. This supports endpoint coverage, not word-for-word accuracy or absence of internal omissions.
- T07 Dwarkesh: publisher transcript through the closing exchange at 02:24:51. The full displayed text is saved, but only the previously documented excerpt has interpretive review.
- T02 State of GPT: third-party text through 41:27; recording is 42:40. Tail beyond the last timestamp remains unverified. Do not call this audio-verified completeness.
- T04 No Priors 2024: third-party machine text through the closing at 44:06, including obvious recognition errors and imperfect speaker labelling.
- T05 Berkeley: entire displayed ceremony transcript through 01:31:56, including other speakers and winner pitches. Karpathy's segment begins near 04:05 by his homepage link and ends near 22:10 per transcript; boundaries are provisional pending playback.
- T06 YC: archived third-party transcript explicitly warns that Karpathy found errors. Use for finding passages, not as verified quotation evidence. Its page metadata also mislabels the year as 2024; the event is 2025.
- T08 No Priors 2026: auto-generated, cleaned third-party transcript, with opening and closing; not timestamped or audio-checked.
- T09 Sequoia 2026: author-published AI summary and cleaned transcript, including the provenance preface. Additional blog/X context was supplied to the model; do not attribute summary-only language to the spoken recording.

No recordings were fully watched or listened to during this collection pass. None of the newly archived transcripts has been marked interpretively reviewed. Visual/code demonstrations still require original-video inspection where a claim depends on the screen.

## Recent educational videos

| ID | Recording | Duration | Local text |
|---|---|---|---|
| Y01 | [The spelled-out intro to neural networks and backpropagation: building micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0) | 2:25:52 | [machine transcript](transcripts/Y01.md) |
| Y02 | [The spelled-out intro to language modeling: building makemore](https://www.youtube.com/watch?v=PaCmpygFfXo) | 1:57:45 | [machine transcript](transcripts/Y02.md) |
| Y03 | [Building makemore Part 2: MLP](https://www.youtube.com/watch?v=TCH_1BHY58I) | 1:15:40 | [machine transcript](transcripts/Y03.md) |
| Y04 | [Building makemore Part 3: Activations & Gradients, BatchNorm](https://www.youtube.com/watch?v=P6sfmUTpUmc) | 1:55:58 | [machine transcript](transcripts/Y04.md) |
| Y05 | [Building makemore Part 4: Becoming a Backprop Ninja](https://www.youtube.com/watch?v=q8SA3rM6ckI) | 1:55:24 | [machine transcript](transcripts/Y05.md) |
| Y06 | [Building makemore Part 5: Building a WaveNet](https://www.youtube.com/watch?v=t3YJ5hKiMQ0) | 56:22 | [machine transcript](transcripts/Y06.md) |
| Y07 | [Let's build GPT: from scratch, in code, spelled out.](https://www.youtube.com/watch?v=kCc8FmEb1nY) | 1:56:20 | [machine transcript](transcripts/Y07.md) |
| Y08 | [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) | 2:13:35 | [machine transcript](transcripts/Y08.md) |
| Y09 | [Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU) | 4:01:26 | [machine transcript](transcripts/Y09.md) |
| Y10 | [[1hr Talk] Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) | 59:48 | [machine transcript](transcripts/Y10.md) |
| Y11 | [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) | 3:31:24 | [machine transcript](transcripts/Y11.md) |
| Y12 | [How I use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw) | 2:11:12 | [machine transcript](transcripts/Y12.md) |

## Recent talks and interviews

| ID | Year | Recording | Text status |
|---|---|---|---|
| T01 | 2022 | [Lex Fridman Podcast #333: Tesla AI, Self-Driving, Optimus, Aliens, and AGI](https://www.youtube.com/watch?v=cdiD-9MMpb0) | [saved text](transcripts/T01.md) - third_party_whisper |
| T02 | 2023 | [State of GPT](https://www.youtube.com/watch?v=bZQun8Y4L2A) | [saved text](transcripts/T02.md) - third_party_transcript |
| T03 | 2024 | [GPU Mode 2024 (homepage label)](https://www.youtube.com/watch?v=FH5wiwOyPX4) | Transcript not retrieved |
| T04 | 2024 | [No Priors: The Road to Autonomous Intelligence](https://www.youtube.com/watch?v=hM_h0UA7upI) | [saved text](transcripts/T04.md) - third_party_machine_transcript |
| T05 | 2024 | [UC Berkeley AI Hackathon 2024 keynote and winner pitches](https://www.youtube.com/watch?v=tsTeEkzO9xc) | [saved text](transcripts/T05.md) - third_party_transcript |
| T06 | 2025 | [Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ) | [saved text](transcripts/T06.md) - third_party_transcript_with_explicit_error_warning |
| T07 | 2025 | [Dwarkesh Podcast: AGI is still a decade away](https://www.dwarkesh.com/p/andrej-karpathy) | [saved text](transcripts/T07.md) - publisher_transcript |
| T08 | 2026 | [No Priors: Skill Issue — Code Agents, AutoResearch, and the Loopy Era of AI](https://www.youtube.com/watch?v=kwSVtQ7dziU) | [saved text](transcripts/T08.md) - third_party_auto_generated_and_cleaned_transcript |
| T09 | 2026 | [Sequoia Ascent 2026: From Vibe Coding to Agentic Engineering](https://www.youtube.com/watch?v=96jN2OCOfLs) | [saved text](transcripts/T09.md) - author_published_AI_edited_summary_and_transcript |
| T10 | 2023 | [Stanford CS25: V2 / Introduction to Transformers with Andrej Karpathy](https://www.youtube.com/watch?v=XfpMkf4rD6E) | [saved text](transcripts/T10.md) - third_party_whisper |
| T11 | 2024 | [Making AI accessible with Andrej Karpathy and Stephanie Zhan](https://www.youtube.com/watch?v=c3b-JASoPi0) | [saved text](transcripts/T11.md) - third_party_whisper |

## Other author uploads and linked generated material

These are retained in the inventory rather than silently filtered out. They are not lecture transcripts or spoken explanations.

| ID | Source | Duration |
|---|---|---|
| Y13 | [Stable diffusion dreams of psychedelic faces](https://www.youtube.com/watch?v=kVpDARqZdrQ) | 4:02 |
| Y14 | [Stable diffusion dreams of steampunk brains](https://www.youtube.com/watch?v=2oKjtvYslMY) | 19:26 |
| Y15 | [Stable diffusion dreams of tattoos](https://www.youtube.com/watch?v=sM9bozW295Q) | 1:46 |
| Y16 | [Stable diffusion dreams of "blueberry spaghetti" for one night](https://www.youtube.com/watch?v=vEnetcj_728) | 5:03 |
| Y17 | [Stable diffusion dreams of steam punk neural networks](https://www.youtube.com/watch?v=Jv1ayv-04H4) | 2:35 |
| Y18 | [Founding fathers on contemporary America - a treatise by o1-pro (announcement label)](https://www.youtube.com/watch?v=1qTa9cJ7cjk) |  |

## Older context inventory

These links are not a claim of exhaustive pre-2022 coverage. Old course entries are playlist-enumerated only; lecturer attribution and transcripts remain open.

| ID | Recording | Scope |
|---|---|---|
| C01 | [Robot Brains podcast with Pieter Abbeel 2021](https://www.therobotbrains.ai/who-is-andrej-karpathy) | pre_2022_context |
| C02 | [Tesla AI Day 2021](https://youtu.be/j0z4FweCy4M?t=2900) | pre_2022_context |
| C03 | [AI for Full Self-Driving @ CVPR 2021](https://www.youtube.com/watch?v=g6bOwQdCJrc) | pre_2022_context |
| C04 | [AI for Full Self-Driving @ ScaledML 2020](https://www.youtube.com/watch?v=hx7BXih7zx8) | pre_2022_context |
| C05 | [Tesla Autonomy Day 2019](https://www.youtube.com/watch?v=Ucp0TTmvqOE&feature=youtu.be&t=6678) | pre_2022_context |
| C06 | [Multi-Task Learning in the Wilderness @ ICML 2019](https://slideslive.com/38917690/multitask-learning-in-the-wilderness) | pre_2022_context |
| C07 | [PyTorch at Tesla @ PyTorch DevCon 2019](https://www.youtube.com/watch?v=oBklltKXtDE) | pre_2022_context |
| C08 | [Building the Software 2.0 stack @ Spark-AI 2018](https://www.youtube.com/watch?v=y57wwucbXR8) | pre_2022_context |
| C09 | [2017 RE•WORK Summit with Nathan Benaich](http://videos.re-work.co/videos/344-interview-with-andrej-karpathy-openai) | pre_2022_context |
| C10 | [2017 "Heroes of Deep Learning" with Andrew Ng](https://www.youtube.com/watch?v=xxu4IqwKw0w) | pre_2022_context |
| C11 | [2017 Deep RL Bootcamp with Pieter Abbeel et al](https://www.youtube.com/watch?v=tqrcjHuNdmQ) | pre_2022_context |
| C12 | [2016 Bay Area Deep Learning School: CNNs](https://www.youtube.com/watch?v=u6aEYuemt0M) | pre_2022_context |
| C13 | [Deep Learning Workshop @ CVPR 2016](https://www.youtube.com/watch?v=CYwK8bQprBY) | pre_2022_context |
| C14 | [RE•WORK Deep Learning Summit 2016](https://www.youtube.com/watch?v=qPcCk1V1JO8) | pre_2022_context |
| C15 | [NVIDIA GTC Keynote 2015 with Jensen Huang](https://www.youtube.com/watch?v=8AnV7xAvpLQ&feature=youtu.be&t=4m15s) | pre_2022_context |
| L01 | [CS231n Winter 2016: Lecture1: Introduction and Historical Context](https://www.youtube.com/watch?v=NfnWJUyUJYU) | pre_2022_context_speaker_unverified |
| L02 | [CS231n Winter 2016: Lecture 2: Data-driven approach, kNN, Linear Classification 1](https://www.youtube.com/watch?v=8inugqHkfvE) | pre_2022_context_speaker_unverified |
| L03 | [CS231n Winter 2016: Lecture 3: Linear Classification 2, Optimization](https://www.youtube.com/watch?v=qlLChbHhbg4) | pre_2022_context_speaker_unverified |
| L04 | [CS231n Winter 2016: Lecture 4: Backpropagation, Neural Networks 1](https://www.youtube.com/watch?v=i94OvYb6noo) | pre_2022_context_speaker_unverified |
| L05 | [CS231n Winter 2016: Lecture 5: Neural Networks Part 2](https://www.youtube.com/watch?v=gYpoJMlgyXA) | pre_2022_context_speaker_unverified |
| L06 | [CS231n Winter 2016: Lecture 6: Neural Networks Part 3 / Intro to ConvNets](https://www.youtube.com/watch?v=hd_KFJ5ktUc) | pre_2022_context_speaker_unverified |
| L07 | [CS231n Winter 2016: Lecture 7: Convolutional Neural Networks](https://www.youtube.com/watch?v=LxfUGhug-iQ) | pre_2022_context_speaker_unverified |
| L08 | [CS231n Winter 2016: Lecture 8: Localization and Detection](https://www.youtube.com/watch?v=GxZrEKZfW2o) | pre_2022_context_speaker_unverified |
| L09 | [CS231n Winter 2016: Lecture 9: Visualization, Deep Dream, Neural Style, Adversarial Examples](https://www.youtube.com/watch?v=ta5fdaqDT3M) | pre_2022_context_speaker_unverified |
| L10 | [CS231n Winter 2016: Lecture 10: Recurrent Neural Networks, Image Captioning, LSTM](https://www.youtube.com/watch?v=yCC09vCHzF8) | pre_2022_context_speaker_unverified |
| L11 | [CS231n Winter 2016: Lecture 11: ConvNets in practice](https://www.youtube.com/watch?v=pA4BsUK3oP4) | pre_2022_context_speaker_unverified |
| L12 | [CS231n Winter 2016: Lecture 12: Deep Learning libraries](https://www.youtube.com/watch?v=Vf_-OkqbwPo) | pre_2022_context_speaker_unverified |
| L13 | [CS231n Winter 2016: Lecture 14: Videos and Unsupervised Learning](https://www.youtube.com/watch?v=ekyBklxwQMU) | pre_2022_context_speaker_unverified |
| L14 | [CS231n Winter 2016: Lecture 13: Segmentation, soft attention, spatial transformers](https://www.youtube.com/watch?v=ByjaPdWXKJ4) | pre_2022_context_speaker_unverified |

## Discovery, duplicates and exclusions

Discovery combined the author's homepage, actual official channel response, both author-linked lecture playlists, the Stanford recordings index, searches by year (2022-2026) and format (talk, keynote, interview, podcast), host-specific follow-ups, secondary appearance directories, and a keyword/link scan across all 1,012 locally saved X records. Secondary sites supplied leads, not independent verification of spoken claims. The X scan is a discovery aid, not interpretive review of every post; quoted posts and shortened/missing links can still hide appearances.

Primary discovery anchors:
- https://karpathy.ai/
- https://www.youtube.com/@AndrejKarpathy/videos
- https://karpathy.ai/zero-to-hero.html
- https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ
- https://www.youtube.com/playlist?list=PLkt2uSq6rBVctENoVBg1TpCC7OQi31AlC
- https://web.stanford.edu/class/cs25/recordings/
- https://www.accel.com/news/6-keynotes-from-the-first-cuda-mode-irl-hackathon

Examples of exclusions/relationships checked:
- The Artificial Intelligence Show, 2024-09-10, “ProblemsGPT ... Andrej Karpathy ...”: the publisher description identifies hosts discussing his podcast, not a Karpathy guest appearance. https://podcasts.apple.com/us/podcast/problemsgpt-the-roi-of-generative-ai-andrej-karpathy/id1548733275?i=1000669007489
- Super Data Science PT970 similarly discusses his posts; not counted as his interview. https://www.superdatascience.com/wp-content/uploads/PT970-Transcript.pdf
- State of GPT in Zero to Hero is the same T02 recording, not an extra lecture.
- Podcast audio, video, companion writing, translated reuploads and clips are alternate representations of an appearance unless evidence establishes a distinct event.
- CS231n “Lecture 15: Invited Talk by Jeff Dean” is not attributed to Karpathy. https://www.youtube.com/watch?v=T7YkPWpwFD4
- Older Clubhouse Deep Learning Deep Dive, historical unlisted talks and the author's older academic-site talks are additional leads, not enumerated series coverage. https://podcasts.apple.com/us/podcast/deep-learning-deep-dive/id1555309024 and https://cs.stanford.edu/people/karpathy/
- The 2023 intro-to-LLMs announcement says it was based on an earlier 30-minute talk. No separate original event recording was verified; do not silently equate the two. https://x.com/karpathy/status/1727731541781152035
- Personal speedcubing/hobby videos and recordings by other people that he merely recommends are outside this AI research corpus.

## Access and unresolved work

Direct HTTP checks on all 28 identified recent YouTube recordings (17 current uploads plus 11 external appearances) returned LOGIN_REQUIRED / “Sign in to confirm you're not a bot”; caption availability therefore remains unknown, not absent. The browser automation host was unavailable. Public channel/playlist enumeration and public text sources did work. All 15 older featured links were also attempted: 12 YouTube playback checks were blocked, Robot Brains and SlidesLive pages returned HTTP 200 without playback verification, and the RE-WORK link returned HTTP 530. Course videos were enumerated from the playlist, not individually played.

GPU Mode: Karpathy's segment is 30:50-54:06 according to his own speaker list, https://x.com/karpathy/status/1841536806405472616. His homepage currently links t=3246 (54:06), which is the next speaker; use the author post's start, not that homepage offset. Transcript retrieval remains open despite direct-video, public-mirror and targeted-search checks.

The next collection work is closing the GPU Mode text gap and replacing uncertain transcripts with original captions/audio checks across the corpus. This is not a sample-first gate. Full chronological reading and synthesis can proceed using available text, with provenance and unresolved passages retained. Broader external appearance discovery remains open; no search can establish that undiscovered or deleted recordings never existed.

Keep the existing Markdown/JSONL approach: new text belongs beside its sources, and the register holds provenance. A database is only justified after recurring retrieval or consistency failures; it is not needed to complete this collection pass.

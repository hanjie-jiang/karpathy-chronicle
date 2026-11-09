# Karpathy: provisional chronological outline

Updated 2026-11-09 (Asia/Shanghai). **Initial outline, not a completed intellectual history.** The 2022, 2023 and 2024 sections are written from a full read of each year's X posts. Later sections are still outline-level. Full agreed source scope remains in [README.md](README.md). The working period is 2022 onward, with older explanatory context. Source identities and separate access/review states are in [sources.jsonl](sources.jsonl); [coverage and evidence notes](sources/2026-11-06-inventory-and-evidence.md) explain gaps and review extents.

The headings below organize dated public artifacts. They do not claim private learning stages, steady intellectual progress, or first-ever expression. “Observation” refers to accessible material; “interpretation” is ours; questions remain unresolved. No user belief or practical decision has been inferred.

## 2019 contextual baseline: making training trustworthy

**Observation — reviewed writing, A01.** The [training recipe](https://karpathy.github.io/2019/04/25/recipe/) emphasizes data inspection, simple baselines and incremental validation in response to silent failures.

**Interpretation to test:** later coding-agent practices can be compared with this concern for trustworthy feedback. We have not established that they descend from this article. This older context does not expand the project into a full career archive.

## 2022: leaving management, returning to building and teaching, as LLMs start to look general

**Coverage.** All 251 main-timeline X posts from 2022 were read in full on 2026-11-06. Replies, reposts and image contents are not in the archive. The [Lex interview](https://www.youtube.com/watch?v=cdiD-9MMpb0) (T01, published 2022-10-29) was checked only at keyword-located passages in a third-party machine transcript; it was not read in full. The 2022 lectures Y01–Y06 were not read. Details are in the [review ledger](sources/review-ledger.md). Post dates below are Beijing time, as stored in the archive. Engagement counts were not used as a measure of importance.

### Context

In March he announced time off "after almost 5 years at Tesla", wanting "to re-sharpen my technical edge and train some neural nets" ([post](https://x.com/karpathy/status/1508148604149587972)). On July 14 he announced he was leaving Tesla, with "no concrete plans", intending to spend "more time revisiting my long-term passions around technical work in AI, open source and education" ([post](https://x.com/karpathy/status/1547332301519851520)). In the Lex interview (T01 ≈01:47:49–01:48:00, machine transcript) he gives the reason as: "I built the team, it felt autonomous and I became a manager and I wanted to do a lot more technical stuff. I wanted to learn stuff, I wanted to teach stuff."

From August to October he published a lecture series that builds neural networks from scratch: micrograd, then makemore parts 1–4. He called micrograd "the culmination of about 8 years of obsessing about the best way to explain neural nets and backprop" ([post](https://x.com/karpathy/status/1559672719414681601)).

### AI fundamentals and limits

- **Models as unfamiliar objects, not brains.** He referred to LLMs as "alien artifacts"; "Obviously powerful, especially if you poke it just right" ([May 26](https://x.com/karpathy/status/1529514197121384448)). In T01 (≈00:06:33–00:06:51) he explains this: the trained network is "a very complicated alien artifact" produced by a compression objective, and "I do not make analogies to the brain".
- **Expecting scale to keep paying off.** "Things are about to get a lot weirder because models appear to follow smooth scaling laws and data+model size can still plenty grow" ([Jun 13](https://x.com/karpathy/status/1536061913376776192)). He also passed on the Bitter Lesson as a "gut check" for ideas ([Apr 2](https://x.com/karpathy/status/1509962678319595523)). He found it "highly amusing" that math could be handled by feeding raw text into a big transformer rather than by formal engines ([Jul 1](https://x.com/karpathy/status/1542886366073171968)).
- **The Transformer as a general computer.** It is "a general-purpose differentiable computer… expressive… optimizable… efficient" ([Oct 20](https://x.com/karpathy/status/1582807367988654081); repeated in T01 ≈00:35:58).
- **Limits stated as open questions, not settled.** He asked "how much can an AI learn from internet text alone?… do we have to reach all the way to embodied agents?" ([Sep 7](https://x.com/karpathy/status/1567233122252750848)). He contrasted LLM training with how humans learn: people skim what they already know, ignore noise, and revisit material that is learnable but not yet learned ([Nov 16](https://x.com/karpathy/status/1592715504841809926)). On ChatGPT: "it doesn't get 'time to think'… Asking them to produce more text is giving them more time to think" ([Dec 5](https://x.com/karpathy/status/1599488637422694400)).
- **Practical rather than philosophical.** "I am so bored of fighting over definitions, chinese rooms and qualias… Let's measure, characterize and focus on that" ([May 23](https://x.com/karpathy/status/1528407022873346049)). Also: "AGI is a feeling. Like love. Stop trying to define it." ([Jun 4](https://x.com/karpathy/status/1532894698439774208)).
- **LLMs as the core of a larger system.** The "quickly growing stack around/above a single large language model" ([Jul 23](https://x.com/karpathy/status/1550590818041311232)). The LLM as a "cognitive engine" orchestrating calculators, interpreters and search through text ([Nov 17](https://x.com/karpathy/status/1593081701454204930)). AI using the same keyboard-and-mouse "APIs" as humans, because "the world is built for humans" ([Feb 17](https://x.com/karpathy/status/1494166717269823492), [Apr 27](https://x.com/karpathy/status/1519010171376521216)).

### Human agency and empowerment

- **Open tools seen as a gain for creativity.** He called the Stable Diffusion release "a day of historic proportion for human creativity… an era of human+AI art collab" ([Aug 23](https://x.com/karpathy/status/1561818955966058500)). He stressed that "_Dramatically_ greater creativity… is possible when the model weights are available" ([Aug 17](https://x.com/karpathy/status/1559589334449152000)).
- **At the same time, warnings about technology that exploits attention.** TikTok: "First time I feel attacked by AI in the brain" ([Mar 27](https://x.com/karpathy/status/1507893647341142016)). AI art "may converge to wire-heading" ([Aug 31](https://x.com/karpathy/status/1564698516164730880)). He wanted a "clean" certification for apps without dark patterns ([Apr 20](https://x.com/karpathy/status/1516725875550879748)) and hoped for products that brag about being "dumb" ([May 30](https://x.com/karpathy/status/1531296768243077120)). On concentration: "How long until we measure wealth inequality in FLOPS" ([Dec 6](https://x.com/karpathy/status/1600012576825360384)).
- **Human checking in interfaces.** In a text-to-SQL demo, the decoded SQL being visible for verification is "imo necessary for higher stake applications" ([Dec 17](https://x.com/karpathy/status/1603835488443330560)).

### Coding and thought organization

- **Prompting as programming.** "Programming turns into a kind of applied psychology of neural nets, biological or synthetic" ([Feb 27](https://x.com/karpathy/status/1497652099701620738)); also "a new form of programming" ([May 17](https://x.com/karpathy/status/1526303528360128512)). T01 (≈01:05:24–01:05:42): "natural language prompt is how we program humans. And we're starting to program computers directly in that interface."
- **Coding assistants in his own work by year-end.** Copilot "already writes ~80% of my code, ~80% accuracy. I don't even really code, I prompt. & edit." ([Dec 31](https://x.com/karpathy/status/1608895189078380544)). Without it, he "felt a sense of dread… alone in the text editor" ([Dec 31](https://x.com/karpathy/status/1608895190672211968)). He also observed that code comments now "are there to help the copilot" ([Dec 26](https://x.com/karpathy/status/1607104323175211008)).
- **A note-taking practice already in place.** He described keeping one note where ideas go "one per line to the top", periodically moving interesting items up while most sink, and forgetting "75% of what's on there" ([Jun 4](https://x.com/karpathy/status/1532852924212072448)). This is the same practice as the March 2025 append-and-review post (A03), which supports that post's description of it as longstanding.
- **Communication style that affects how we read him.** "It would be best if people made strong statements that are understood to be only 90% true, and ignore the counterexample police" ([Sep 28](https://x.com/karpathy/status/1574906895453675521)). His short claims should be read as deliberately strong, not as carefully qualified positions.

### Engineering and project practice

- **Deployment realities over benchmarks.** He valued "deployment-time simplicity" when choosing model components ([Jan 14](https://x.com/karpathy/status/1481724509795221505)): "Everybody gangsta until real-world deployment in production." ([Jan 26](https://x.com/karpathy/status/1486215976559398915)).
- **The data engine as the competitive advantage.** Advantage goes "not so much to those with data but those with a data engine: iterated data aquisition, re-training, evaluation, deployment, telemetry. And whoever can spin it fastest." ([Dec 6](https://x.com/karpathy/status/1599852921541128194); also discussed in T01 ≈01:23:59).
- **Avoiding bug-prone abstractions.** He argued for counting training iterations rather than epochs ([Mar 28](https://x.com/karpathy/status/1508437725514510336)) and complained about how experiment configs are managed ([May 24](https://x.com/karpathy/status/1528808361558306817)).
- **Teaching and performance as separate goals.** He split minGPT because "I can't properly simultaneously satisfy both 1) educational and 2) efficient in one repo" ([Dec 28](https://x.com/karpathy/status/1607791539258003457)).
- **Building small tools for his own needs.** Lexicap transcribed ~322 podcast episodes with Whisper ([Sep 27](https://x.com/karpathy/status/1574474950416617472)). He "mostly built Lexicap so I could share a few snippets" ([Sep 27](https://x.com/karpathy/status/1574501715990102016)).
- **Easy to verify, hard to solve.** "Most real-world problems… hard to solve but easy to verify a solution to. It's this asymmetry that makes progress possible" ([Aug 15](https://x.com/karpathy/status/1558863432023126020)).
- **Interest in AI products.** As an AI Grant advisor: "great timing to start an AI-native product company" ([Sep 28](https://x.com/karpathy/status/1574841955405553664)).

### Interpretation (ours, provisional)

1. **"Role change" is better supported than "belief change".** The best-evidenced shift in 2022 is in his work, not his views. In his own words, he moved from manager to builder and teacher. His views on scaling, Transformers and data engines continue his earlier Tesla-era framing ("Software 2.0" and data engines appear as established ideas in T01), so they don't look like new discoveries.
2. **Mechanism-level understanding and delegation coexisted.** In the same year he built from-scratch lectures and reported Copilot writing most of his code. He still described himself as someone who prompts *and edits*. That oversight is a baseline for comparing with February 2025, when he described "vibe coding" with diffs no longer read.
3. **Verification is a recurring concern.** It appears in the 2019 recipe (data inspection), in "hard to solve, easy to verify" (August 2022), in visible SQL for high-stakes uses (December 2022), and later in the 2025 year review. This is a candidate continuous thread. It is our pattern, not a framework he named.
4. **Optimism and caution held together.** Open models expand creativity, while attention-optimizing AI and compute concentration are named risks. This matches the 2025 "Power to the people" argument in form; whether the content shifted is unverified.

### Uncertainties and gaps

- The December 7 "observations on applications of ChatGPT to society" ([post](https://x.com/karpathy/status/1600214083206193153)) and the Whisper notes (September 23) are images. Their text is not in the archive.
- Replies may contain substantive positions; none were collected.
- T01 is a 3.5-hour interview. Only the cited passages were read, and they are in an unverified machine transcript.
- The lectures were not reviewed for what they teach about debugging or judgment.

### Questions for the user

1. In 2022 he wrote "I prompt & edit". In 2025 he described not reading diffs. Where is your own practice on that line, and where do you think it should be for code you need to maintain?
2. He advocates "strong statements understood to be only 90% true". Does that make him a better or worse role model to learn from? How would you discount his strong claims?
3. The 2022 cautions (attention exploitation, "wealth inequality in FLOPS") sit beside excitement about open tools. Which of these matters most for the kind of product you'd want to build alone?

## 2023: back at OpenAI, and building a vocabulary for using LLMs

**Coverage.** All 186 main-timeline X posts from 2023 were read in full. For the long-form sources:
- [State of GPT](https://www.youtube.com/watch?v=bZQun8Y4L2A) (T02, May 2023): only the recommendations section (≈37:11–40:11) was read, in a third-party transcript.
- [Intro to LLMs](https://www.youtube.com/watch?v=zjkBMFhNj_g) (Y10): only the tool-use and LLM OS passages were read. It is now dated by his own announcement, [Nov 24, 2023](https://x.com/karpathy/status/1727731541781152035), which resolves the earlier provisional placement.
- Build GPT (Y07): one passage. Stanford CS25 (T10): not read.

Details are in the [review ledger](sources/review-ledger.md).

### Context

He released nanoGPT (January), aiming to be the "simplest, fastest repo for training/finetuning medium-sized GPTs" ([Jan 12](https://x.com/karpathy/status/1613250487838707712)), and the build-GPT lesson. On February 9 he announced he was joining OpenAI again, having "personally benefited greatly from" its work ([post](https://x.com/karpathy/status/1623476659369443328)). The posts don't describe his role there. Side projects continued: a movie search site built on embeddings ([Apr 16](https://x.com/karpathy/status/1647372603907280896)), and llama2.c, which runs Llama 2 from one 500-line C file ([Jul 23](https://x.com/karpathy/status/1683143097604243456)). Compared with 2022, the posts shift from model internals toward how to *use* LLMs and build on top of them.

### AI fundamentals and limits

- **The LLM as a new kind of computer, and later an operating system.** "The hottest new programming language is English" ([Jan 25](https://x.com/karpathy/status/1617979122625712128)). "GPT is a new kind of computer architecture that runs on text" ([Mar 24](https://x.com/karpathy/status/1638983034522460162)). In April he worked through a detailed comparison with early CPUs, describing the context window as RAM ([Apr 7](https://x.com/karpathy/status/1644183721405464576)). By September: "LLMs not as a chatbot, but the kernel process of a new Operating System… looking at LLMs as chatbots is the same as looking at early computers as calculators" ([Sep 29](https://x.com/karpathy/status/1707437820045062561)). This was followed by an "LLM OS" diagram ([Nov 11](https://x.com/karpathy/status/1723140519554105733)) and its use in Y10 (≈00:42:34–00:44:50). This dates the operating-system analogy, at the latest, to September 2023 on X.
- **Simulators and "dream machines".** "A pretrained LLM is not an AI but a simulator" of internet documents ([Mar 7](https://x.com/karpathy/status/1632800081622761472)). His sharpest framing came in December: "hallucination is all LLMs do. They are dream machines… The LLM has no 'hallucination problem'… The LLM Assistant has a hallucination problem, and we should fix it". The fixes he lists are retrieval, comparing multiple samples, verification chains and tools ([Dec 9](https://x.com/karpathy/status/1733299213503787018)).
- **Limits stated concretely.**
  - LLMs "are completely unaware of their own strengths and limitations" ([Apr 3](https://x.com/karpathy/status/1642600116837298178)).
  - Their knowledge is "a lot more 'patchy' than you'd expect. I still don't have great intuition for it" ([Sep 23](https://x.com/karpathy/status/1705322159588208782)).
  - Fine-tuning can make a model's confidence miscalibrated ([Mar 19](https://x.com/karpathy/status/1637147822482165760)).
  - Tokenization has "many subtle sharp edges" ([May 15](https://x.com/karpathy/status/1657949234535211009)).
- **Why scale dominates.** Asked what to do with a 10X bigger computer, ten years ago the answer was unclear. "Now: Not only do I know exactly what to do with it but I can predict the metrics… Algorithmic progress was necessity, now bonus" ([Aug 4](https://x.com/karpathy/status/1687248476508487681)).

### Human agency and empowerment

- **Open-weights ecosystem.** He described the "cambrian explosion" of open-source LLMs: cheap fine-tuning made wide experimentation possible, "but only conditioned on" expensive base models being available. He also noted LLaMA's awkward "open but not really" status ([May 7](https://x.com/karpathy/status/1654892810590650376)). He welcomed Llama 2 as "the most capable LLM available directly as weights to anyone" ([Jul 19](https://x.com/karpathy/status/1681356674635034625)). He preferred "open weights" to "open source" when training code and data aren't released ([Dec 12](https://x.com/karpathy/status/1734251375163511203)). He framed local LLM hardware as "What would someone need a personal LLM node for?" ([Aug 17](https://x.com/karpathy/status/1691849237900992580)).
- **AI as augmentation.** Reading Licklider's 1960 "Man-Computer Symbiosis", he noted the argument that "intelligence augmentation" may be a transient stage before full automation, "but still long enough to be worth thinking through" ([Dec 28](https://x.com/karpathy/status/1740078732562636929)). He proposed an LLM-powered filter that blurs "ads, viral, triggering" content, "Protecting your brain at 60Hz", and called it part of a "programmable exocortex" ([Oct 22](https://x.com/karpathy/status/1715806187663585287)).
- **The 2022 concern about attention continues.** "Most apps are actively adversarial to users. Need much stronger permissions protections" ([Jun 27](https://x.com/karpathy/status/1673450276999815170)). He also endorsed "The Tyranny of the Marginal User" on why consumer software gets worse ([Oct 6](https://x.com/karpathy/status/1710071106022052127)).
- **Centralization, stated without explanation.** "Thinking a lot about centralization and decentralization these few days" ([Nov 22](https://x.com/karpathy/status/1727033766252798272)). The post gives no context, so we should not infer what prompted it.

### Coding and thought organization

- **Learning to work with assistants.** On Copilot or a similar assistant: "many programmers still 1) haven't tried, or 2) quit too fast. It takes some time to adapt your programming habits to it and to develop internal models around when/how it is likely to work" ([Mar 19](https://x.com/karpathy/status/1637151779757621250)). He wrote "A file… 80% Python and 20% English" that mixes code with GPT calls ([Mar 4](https://x.com/karpathy/status/1631812072668553218)). He thanked GPT-4 for help with his "very rusty C" in llama2.c ([Jul 23](https://x.com/karpathy/status/1683143099361660929)). On data analysis code: "It's too easy and feels like cheating. It should have taken hours" ([Jul 21](https://x.com/karpathy/status/1682109479255678978)). On making diagrams: "sit back, and iterate in English… needing to touch no code" ([Nov 5](https://x.com/karpathy/status/1720939313112945057)).
- **His explicit advice, May 2023 (T02 ≈37:11–40:11, third-party transcript).**
  - Write detailed prompts, as if for "a task contractor [who] can't email you back".
  - Show examples, and use tools and chains of calls.
  - Stay with prompting for a while before fine-tuning.
  - Then: "use LLMs in low-stakes applications. Combine them always with human oversight… think co-pilots, instead of completely autonomous agents… It's just not clear that the models are there right now."
- **A prediction in tension with that advice, November 2023.** Coding tools go from tab-completion to whole chunks of code, to pull requests written from issues, to writing the issues themselves. "Human input and oversight gradually ascends in abstraction and contributes less, until it is ~pass-through" ([Nov 9](https://x.com/karpathy/status/1722359332116062491)).
- **Code readability.** He favours a "minimal design aesthetic" over nested indirection that makes reading code "an exhausting treasure hunt" ([Jan 31](https://x.com/karpathy/status/1620103414490468352)). On comments: "Coding is a team sport. Use comments. Not too much. Mostly the unobvious." ([Sep 30](https://x.com/karpathy/status/1707920583219167731)).
- **A thinking habit.** Every January 22 he writes predictions for 1, 3, 5, 10 and 20 years ahead and revisits past ones. "for any prediction for +x years I first consider -x year delta" ([Jan 23](https://x.com/karpathy/status/1617265772631588865)).

### Engineering and project practice

- **A new role: building with models rather than training them.** "Expectation: I need more deep learning engineers… Reality: You need prompt engineers and LLM Ops" ([Apr 4](https://x.com/karpathy/status/1642920043423088640)). In July he endorsed the "AI Engineer" framing: "One can be quite successful in this role without ever training anything", and "AI Engineers simultaneously program in all 3 paradigms" (Software 1.0, 2.0 and 3.0, the last being "~prompting LLMs") ([Jul 1](https://x.com/karpathy/status/1674873002314563584)).
- **Practical techniques for builders.** Few-shot classification with base models ([Mar 19](https://x.com/karpathy/status/1637147821311918083)). SVMs instead of kNN for searching embeddings ([Apr 15](https://x.com/karpathy/status/1647025230546886658)). Tuning API embeddings with a small set of example pairs ([Jul 13](https://x.com/karpathy/status/1679463907344146438)). A recommendation to learn Streamlit for rapid prototyping ([Jun 21](https://x.com/karpathy/status/1671253733328719872)). Enthusiasm for evals ([Mar 17](https://x.com/karpathy/status/1636459245184106497)).
- **Experimenting as the way to make progress.** "It's not so much 'here's how you can improve' but 'here's the 10 things you should try'. And why high experimental throughput is necessary" ([Jan 30](https://x.com/karpathy/status/1619749146340237313)).
- **Demos versus real products.** Looking back on his first self-driving demo drive in 2013: "How long it takes to make demos *real*…" ([Aug 11](https://x.com/karpathy/status/1689819017610227712)).

### Interpretation (ours, provisional)

1. **His focus moved from how models are built to how they are used.** 2022 was mostly about internals and training. 2023 adds a vocabulary for *users and builders*: English as a programming language, the LLM OS, the AI Engineer role, dream machine versus assistant. This fits his return to OpenAI and the post-ChatGPT ecosystem, but the posts don't say which caused which.
2. **His advice and his prediction diverge within the same year.** In May the advice was low stakes, human oversight, co-pilots not agents. In November the prediction was oversight rising until it becomes "~pass-through". We read the first as advice for current models and the second as a forecast; he doesn't reconcile them himself. The February 2025 vibe coding post (limited to throwaway projects) should be read against both.
3. **The verification thread continues and gets more specific.** It shows up in verification chains, comparing samples and retrieval for assistants (December), and in the State of GPT advice to keep humans overseeing.
4. **Concern about empowerment continues.** Open weights, personal LLM hardware, augmentation and the brain-protecting filter all point toward individual control. Adversarial apps remain the counterweight.

### Uncertainties and gaps

- Image-only content isn't in the archive, for example the LLM OS diagram (Nov 11) and the SFT diagrams (Nov 5).
- Only the advice section of T02 was read, and the transcript stops before the end of the recording. Y10's training and security sections, the rest of Y07, and all of T10 are unread.
- The posts say nothing about his day-to-day work at OpenAI.

### Questions for the user

1. In May he advised co-pilots with human oversight for low-stakes uses. By November he predicted oversight would become "~pass-through". You said you read the logic rather than the code. What would make you comfortable letting oversight drop further, and for which parts of a product would you refuse to?
2. He says it's the assistant, not the model, that has the hallucination problem, and that the product should fix it with retrieval and checking. For something you'd build alone, which checks would you build in?
3. He says "One can be quite successful in this role without ever training anything." Does the "AI Engineer" path (building on models rather than training them) match what you want to become?

## 2024: independent again, naming the limits, and putting empowerment first

**Coverage.** All 203 main-timeline X posts from 2024 were read in full on 2026-11-09. Long-form sources:
- [Sequoia AI Ascent conversation](https://www.youtube.com/watch?v=c3b-JASoPi0) (T11, March 2024): read in full, in a third-party machine transcript.
- [No Priors interview](https://www.youtube.com/watch?v=hM_h0UA7upI) (T04, September 2024): read in full, in a third-party machine transcript with recognition errors.
- [Berkeley AI Hackathon keynote](https://www.youtube.com/watch?v=tsTeEkzO9xc) (T05, posted July 2024): his segment (≈04:04–22:10) read in a third-party transcript.
- The tokenizer (Y08) and GPT-2 (Y09) lectures were not read; his posts announcing them were. The GPU Mode talk transcript is still missing.

Timestamps below refer to those transcripts and are not audio-checked. Details are in the [review ledger](sources/review-ledger.md).

### Context

On February 14 he announced he had left OpenAI: "nothing 'happened'… My immediate plan is to work on my personal projects" ([post](https://x.com/karpathy/status/1757600075281547344)). The rest of the year was public building and teaching:
- a 2h13m tokenizer lecture ([Feb 21](https://x.com/karpathy/status/1759996549109776702));
- llm.c, GPT-2 training "in pure C without 245MB of PyTorch" ([Apr 9](https://x.com/karpathy/status/1777427944971083809));
- reproducing GPT-2 (124M) "in 90 minutes for $20" ([May 28](https://x.com/karpathy/status/1795484547267834137)), then the 1.6B model for about $672 ([Jul 12](https://x.com/karpathy/status/1811467135279104217));
- a 4-hour "Let's reproduce GPT-2" lecture ([Jun 10](https://x.com/karpathy/status/1799949853289804266)).

On July 17 he announced Eureka Labs, "a new kind of school that is AI native", in which "The teacher still designs the course materials, but they are supported, leveraged and scaled with an AI Teaching Assistant" ([post](https://x.com/karpathy/status/1813263734707790301)). He called it "the culmination of my passion in both AI and education over ~2 decades".

### AI fundamentals and limits

- **"Jagged Intelligence".** He coined the term for models that "can both perform extremely impressive tasks (e.g. solve complex math problems) while simultaneously struggle with some very dumb problems", such as comparing 9.11 and 9.9. He contrasted this with humans, whose abilities "are all highly correlated and improve linearly all together". His advice: "Use LLMs for the tasks they are good at but be on a lookout for jagged edges, and keep a human in the loop" ([Jul 26](https://x.com/karpathy/status/1816531576228053133)).
- **What you are actually talking to.**
  - Asking an LLM a factual question is like asking someone who "read about the topic previously, but they are not allowed to reference any material": "their best attempt at a lossy recollection" ([Jun 22](https://x.com/karpathy/status/1804208334033371213)).
  - In November: "you're not asking some magical AI. You're asking a human data labeler. Whose average essence was lossily distilled into statistical token tumblers" ([Nov 30](https://x.com/karpathy/status/1862565643436138619)).
- **"RLHF is just barely RL".** The reward model is "just a vibe check… a proxy objective of what looks good to humans", and optimizing against it for long finds adversarial examples. Real RL, as in AlphaGo, needs actual rewards, which are "really difficult in the open-ended problem solving tasks" ([Aug 8](https://x.com/karpathy/status/1821277264996352246)). He gave the same AlphaGo framing at Sequoia in March: "we've done step one of AlphaGo… the imitation learning part… people haven't done" the RL step (T11 ≈00:25:21).
- **Benchmarks versus usefulness.**
  - "GPT-4 is not 67% on coding (HumanEval)" ([Mar 5](https://x.com/karpathy/status/1764731169109872952)).
  - Good evals are "unintuitively difficult": at Tesla he spent "1/3 of my time on data, 1/3 on evals" ([May 30](https://x.com/karpathy/status/1795873666481402010)).
  - Moravec's paradox: models do well on hard closed problems, but "you wouldn't hire them over a person for the most menial jobs" ([Nov 11](https://x.com/karpathy/status/1855659091877937385)).
  - The capability he is watching for is "whether you'd hire it as a junior intern" ([Dec 15](https://x.com/karpathy/status/1868061331355840704)).
  - On AGI, he endorsed OpenAI's definition, "a highly autonomous system that outperforms humans at most economically valuable work", and said it "has clearly not been reached" ([Sep 14](https://x.com/karpathy/status/1834641096905048165)).
- **Where improvement will come from.**
  - Models are big because "we're asking them to memorize the internet". "the models have to first get larger before they can get smaller", helping to build cleaner training data in a "staircase of improvement" ([Jul 19](https://x.com/karpathy/status/1814038096218083497)).
  - In No Priors he put a "cognitive core" at perhaps a billion parameters (T04 ≈27:21). He warned that synthetic data is risky because models are "silently collapsed": ChatGPT "only knows like three jokes" (T04 ≈18:46).
- **The computer analogy continues.**
  - "The history of computing is repeating in an echo, except replace computers that do precise arithmetic on bytes with computers that do statistical arithmetic on tokens" ([Apr 18](https://x.com/karpathy/status/1780692023970038259)).
  - LLMs "have little to do with language"; they are "highly general purpose technology for statistical modeling of token streams" ([Sep 15](https://x.com/karpathy/status/1835024197506187617)).
  - The LLM OS framing returns at Sequoia (T11 ≈00:04:01) and Berkeley (T05 ≈06:28).
- **Security as a limit.**
  - "sleeper agent" data poisoning ([Jan 13](https://x.com/karpathy/status/1745921205020799433)).
  - Special-token parsing as an injection attack: "User input strings are untrusted data" ([Aug 14](https://x.com/karpathy/status/1823418177197646104)).

### Human agency and empowerment

- **Intelligence amplification, for everyone.** He tried calling today's technology "IA (intelligence amplification) instead of AI", because it needs "human interaction" ([Jan 8](https://x.com/karpathy/status/1744062845426532473)). His "e/ia" list: "Does not seek to build superintelligent God entity that replaces humans… Builds 'bicycle for the mind' tools… Of all humans, not a top percentile" ([Jan 8](https://x.com/karpathy/status/1744179910347039080)).
- **"Team human".** On why he moved to education: "most of it is to kind of like replace or displace people… I'm always more interested in anything that kind of empowers people… I'm kind of on a high level like team human" (T04 ≈30:36–31:04, machine transcript).
- **Concentration and ownership.**
  - He wants a "coral reef" of startups and is "hesitant about five megacorps taking over… Especially with AGI being such a magnifier of power" (T11 ≈00:21:24–00:22:05).
  - On AI as an exocortex, he agreed with the line "not your weights, not your brain". He also admitted the tradeoff: asked whether he would "give up ownership and control to rent a better brain", he answered "Because I am", and proposed open models as a fallback (T04 ≈25:42–26:58).
  - He welcomed Llama 3.1 405B as "the first time that a frontier-capability LLM is available to everyone to work with and build on" ([Jul 24](https://x.com/karpathy/status/1815842603377779140)). He praised DeepSeek-V3 as a frontier-grade open-weights model "trained on a joke of a budget" ([Dec 27](https://x.com/karpathy/status/1872362712958906460)).
  - He recommended a history of information technologies that "starts decentralized, open and idealistic and then progresses towards centralization", with "Quite a few connections to draw on for LLMs" ([Dec 9](https://x.com/karpathy/status/1865924776214327360)).
- **Protecting attention and ownership.**
  - "Reading a tweet is a bit like downloading an (attacker-controlled) executable that you instantly run on your brain" ([Mar 10](https://x.com/karpathy/status/1766509149297189274)).
  - He praised Obsidian's "File over app" philosophy: "free of dark patterns, fully aligned with the user" ([Feb 25](https://x.com/karpathy/status/1761467904737067456)).
  - He called subscriptions "a user-hostile dark pattern… revenue from unintended forgetfulness" ([Oct 18](https://x.com/karpathy/status/1847164046216159421)).
- **Learning takes effort.** "Learning is not supposed to be fun… the primary feeling should be that of effort." Short-form educational content "is a trap" ([Feb 11](https://x.com/karpathy/status/1756380066580455557)). He repeated the gym comparison in No Priors (T04 ≈40:23).
- **Individual reach.**
  - "Cloud+AI is increasingly making the @levelsio -style model of a scrappy solo serial micro-entrepreneur viable" ([Aug 27](https://x.com/karpathy/status/1828210213620748655)).
  - On a podcast he made with AI tools: "as a single person in 2 hours, curate (not create, but curate) a podcast". He acknowledged "the potential and immediate critique here, of AI generated slop" ([Oct 3](https://x.com/karpathy/status/1841594123381571863)).
  - On AI video: "The future is already here it's just unevenly distributed and unnecessarily difficult" ([Jul 30](https://x.com/karpathy/status/1818141090790375462)).

### Coding and thought organization

- **Oversight rises in abstraction but stays.** Using the self-driving progression as a model, he predicted software engineering will look "a lot more like supervising the automation". He then asked: "How does a human provide oversight? What are they looking at?… It is very likely that we will have to change up the code editor" ([Mar 13](https://x.com/karpathy/status/1767598414945292695)). At Sequoia: "it's quite autonomous, but not fully autonomous. So what does the oversight look like?" (T11 ≈00:07:01).
- **His own practice by August.** With Cursor and Sonnet 3.5: "most of my 'programming' is now writing English (prompting and then reviewing and editing the generated diffs)", plus "half-coding". Also: "I basically can't imagine going back to 'unassisted' coding" ([Aug 24](https://x.com/karpathy/status/1827143768459637073)). He wrote a small tool that drafts git commit messages, which you accept, edit or regenerate ([Aug 26](https://x.com/karpathy/status/1827810695658029262)).
- **Wanting proof, not trust.** "One built-in UI/UX feature of LLM interfaces I'd love is proof." He manually checks commands against the docs because "I want to double check the LLM's recollection" ([Jun 22](https://x.com/karpathy/status/1804187473167421798)). When Claude 3 turned his lecture into a chapter, it looked good, but "there are a number of subtle issues / hallucinations" ([Mar 5](https://x.com/karpathy/status/1764731169109872952)). On an AI-written treatise in December he said he was "not versed enough to… spot hallucinations (if any)" ([Dec 17](https://x.com/karpathy/status/1868903650451767322)).
- **LLMs as compilers.**
  - In a world where "very custom programs are 'free', LLMs might end up being a kind of compiler" ([Apr 13](https://x.com/karpathy/status/1778841713605525889)).
  - He set rewriting llm.c as a challenge for agents: "The current models are not there" ([Apr 9](https://x.com/karpathy/status/1777493157485437009)).
  - In his GPU Mode talk: software abstractions "exist only because humans are finite in knowledge, IQ and attention" ([Oct 3](https://x.com/karpathy/status/1841536804073439268)).
- **Code taste.** He criticised "The if-then-else monster. Bloated functions that take dozens of kwargs" ([Jul 11](https://x.com/karpathy/status/1811140282559385758)). He endorsed "Cognitive load is what matters" as "Probably the most true, least practiced viewpoint" ([Dec 26](https://x.com/karpathy/status/1872038630405054853)).

### Engineering and project practice

- **Build the ramp.** micrograd's code did not change, but a video about it "almost 100X'd" engagement. "Step 1 build the thing. Step 2 build the ramp" ([Feb 22](https://x.com/karpathy/status/1760388761349927356)). He repeated it at Sequoia (T11 ≈00:32:36).
- **Demo versus product.**
  - Waymo took about ten years from a "basically perfect" demo drive to a paid product, and "the demo is near, but the product is far" (T04 ≈01:13–01:34, ≈36:11).
  - "making actual apps is a lot more than code, you have to set up the entire environment, deploy it, etc." ([Sep 6](https://x.com/karpathy/status/1831776835388285347)).
  - AI capability "is getting way ahead of the UIUX of packaging it into products" ([Sep 29](https://x.com/karpathy/status/1840112692910272898)).
  - "Don't ask your users for input… We have AI - predict the input!" ([Oct 3](https://x.com/karpathy/status/1841512260784816329)).
- **Advice for builders.**
  - "Go after performance first. And then you make it cheaper later", including distilling a working expensive system into a cheaper one (T11 ≈00:29:40–00:30:12).
  - He warned against products "too ahead of what's available, or maybe not ambitious enough" (T04 ≈33:39).
- **Projects as the engine.** At Berkeley: "snowball" small projects, count your "10,000 hours", and publish projects because others seeing your work "increases the bar for your own work" (T05 ≈11:20–21:45). His summary post: "While True: build and publish projects. Accumulate 10,000 hours. Snowball your work" ([Jul 27](https://x.com/karpathy/status/1816953700403065162)).
- **Paranoia about silent bugs continues.** He quoted his 2019 recipe ("patience and attention to detail") and added "I exist in a perpetually terrified state of the remaining 20 silent bugs" ([Mar 7](https://x.com/karpathy/status/1765473722985771335)).
- **Organizing work.** Some work is best "run on a CPU" (one highly competent person). Other work is best run "on a GPU" (many people in parallel). "The most common stumbling point here is trying to parallelize something that was supposed to run on the CPU" ([Apr 18](https://x.com/karpathy/status/1780684098773876941)).

### Interpretation (ours, provisional)

1. **2024 is his most explicit year on empowerment so far.** The 2022–2023 concerns about attention and concentration become a stated position: "IA" rather than AI, "Of all humans, not a top percentile", "team human", and AGI as "a magnifier of power". Eureka Labs is how he acts on it. He also admits the tension: he would rent a better closed brain, with open models as a fallback.
2. **He names the limits more precisely.** "Jagged intelligence", "lossy recollection", the "average data labeler", RLHF as a "vibe check" and the junior-intern test form a working vocabulary for what models are and aren't. In each case the practical conclusion is human oversight or verification, not withdrawal.
3. **Oversight moves up a level but does not vanish.** The 2023 forecast of "~pass-through" oversight is not repeated as a description of his own work. In August 2024 he still reviews and edits the diffs, and in March he asks what oversight interfaces should look like. Compare with February 2025 "vibe coding", which he limits to throwaway projects.
4. **The distance from demo to product becomes a theme.** Waymo's decade, "making actual apps is a lot more than code", and UI/UX lagging behind capability anticipate the 2025 MenuGen account. This is the most directly useful thread for building a product alone.
5. **The verification thread continues.** His proof feature, the checking against docs, the hallucinations he caught, and the evals ("1/3 of my time") connect to the 2019 recipe and the 2023 "dream machines" post.

### Uncertainties and gaps

- T04, T05 and T11 are third-party machine transcripts. The quotes above are approximate wording until checked against the audio.
- The tokenizer and GPT-2 lectures (about 6 hours together) were not read. They may show more of how he debugs and checks his own work.
- The GPU Mode talk transcript is missing. Only his post summarizing it was read.
- Image-only content is not in the archive, for example the e/ia list image and the jagged-intelligence screenshots. Their accompanying text was read.

### Questions for the user

1. He says "the demo is near, but the product is far" and that "making actual apps is a lot more than code". In your own projects, where has that gap shown up, and how would you plan for it in a product you build alone?
2. "Not your weights, not your brain", yet he would rent a better brain. For a product of yours, would you build on closed models with an open-model fallback, or prioritize owning the stack?
3. He says learning should feel like effort, and also says "build the ramp". Our public site is for general readers. How should it balance easy entry with real depth?

## 2025: vibe coding, building for agents, and a theory of what models lack

**Coverage.** All 158 main-timeline X posts from 2025 were read in full on 2026-11-09. Long-form sources:
- [Dwarkesh Podcast interview](https://www.dwarkesh.com/p/andrej-karpathy) (T07, October 17): read in full, in the publisher's transcript.
- [YC AI Startup School talk, "Software Is Changing (Again)"](https://www.youtube.com/watch?v=LCEmiRjPEtQ) (T06, June 17): read in a third-party transcript that its publisher warns contains errors. It is used here only to locate content. Claims about the talk rely on his own chapter summary post.
- Blog posts [Power to the people](https://karpathy.bearblog.dev/power-to-the-people/) (A04, April 7), [Vibe coding MenuGen](https://karpathy.bearblog.dev/vibe-coding-menugen/) (A05, April 27) and [2025 LLM Year in Review](https://karpathy.bearblog.dev/year-in-review-2025/) (A06, December 19): re-read live on 2026-11-09. A03 (append-and-review) is quoted in full in an archived post.
- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) (Y11) and [How I use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw) (Y12): only the closing advice of Y11 and the deep-research section of Y12, located by keyword in machine transcripts. Neither was read in full.

Interview timestamps refer to the transcript and are not audio-checked. Details are in the [review ledger](sources/review-ledger.md).

### Context

He stayed independent all year. His public output was general-audience teaching, small personal projects, and one large educational codebase:
- Two long general-audience videos: a 3h31m "Deep Dive into LLMs like ChatGPT" ([Feb 6](https://x.com/karpathy/status/1887211193099825254)) and a 2h11m "How I Use LLMs" ([Feb 28](https://x.com/karpathy/status/1895242932095209667)). He said part of the reason was "to inspire others to make equivalents in their own domains of expertise" ([Feb 8](https://x.com/karpathy/status/1887980449550758121)).
- A new blog, started in March with "Digital Hygiene" ([Mar 19](https://x.com/karpathy/status/1902046003567718810)) and "The append-and-review note" ([Mar 20](https://x.com/karpathy/status/1902503836067229803)).
- Vibe-coded projects: an iOS app in Swift ([Mar 23](https://x.com/karpathy/status/1903671737780498883)), MenuGen ([May 1](https://x.com/karpathy/status/1917961248031080455)), reader3 ([Nov 18](https://x.com/karpathy/status/1990612045700739548)), llm-council ([Nov 23](https://x.com/karpathy/status/1992381094667411768)) and a hindsight grader for old Hacker News threads ([Dec 11](https://x.com/karpathy/status/1998803709468487877)).
- nanochat, "a minimal, from scratch, full-stack training/inference pipeline of a simple ChatGPT clone" in about 8,000 lines. It is meant as the capstone of the LLM101n course ([Oct 13](https://x.com/karpathy/status/1977755427569111362)).
- Talks and interviews: YC AI Startup School in June ([chapter summary](https://x.com/karpathy/status/1935518272667217925)) and the Dwarkesh Podcast in October ([his notes](https://x.com/karpathy/status/1979644538185752935)).

### AI fundamentals and limits

- **Imitation versus trial and error.** After DeepSeek-R1 he distinguished "1) imitation learning (watch and repeat…)" from "2) trial-and-error learning (reinforcement learning)". He said "2 is significantly significantly more powerful", and that the thinking strategies of reasoning models are "*emergent*" because "the cognition of the model and the cognition of the human labeler is different" ([Jan 28](https://x.com/karpathy/status/1883941452738355376)). He named these "cognitive strategies" and asked when LLMs would produce a "Move 37" ([Jan 29](https://x.com/karpathy/status/1884336943321997800)). He mapped training onto a textbook: exposition is pretraining, worked problems are supervised finetuning, and practice problems are reinforcement learning ([Jan 31](https://x.com/karpathy/status/1885026028428681698)).
- **Then a growing doubt about RL itself.**
  - In May he proposed a missing paradigm, "system prompt learning": a lot of human learning "feels more like a change in system prompt", as in "taking notes for yourself" ([May 11](https://x.com/karpathy/status/1921368644069765486)).
  - In July: "I'm fairly certain RL will continue to yield more intermediate gains, but I also don't expect it to be the full story". The reason is that you do hours of work "just to learn a single scalar outcome at the very end", whereas humans learn through a "review/reflect stage" ([Jul 14](https://x.com/karpathy/status/1944435412489171119)).
  - In August: "I am bullish on environments and agentic interactions but I am bearish on reinforcement learning specifically… reward functions are super sus" ([Aug 28](https://x.com/karpathy/status/1960803117689397543)).
  - On Dwarkesh: "Reinforcement learning is terrible. It just so happens that everything that we had before it is much worse". It is "sucking supervision through a straw". LLM judges used as rewards are "gameable", for example a nonsense string that scored 100% (T07 ≈00:40:47–00:48:22).
- **Ghosts, not animals.** Responding to Richard Sutton: "Pretraining is our crappy evolution… today's frontier LLM research is not about building animals. It is about summoning ghosts" ([Oct 2](https://x.com/karpathy/status/1973435013875314729)). In November he described the "space of intelligences": LLMs are "shaped a lot less by biological evolution and a lot more by commercial evolution", and "increasingly selected by at-scale A/B tests for DAU => deeply craves an upvote from the average user, sycophancy" ([Nov 22](https://x.com/karpathy/status/1991910395720925418)).
- **Simulators, not entities.** "Don't think of LLMs as entities but as simulators… There is no 'you'". Ask instead what a good group of people would say ([Dec 8](https://x.com/karpathy/status/1997731268969304070)). This repeats his 2023 point that a base model is "not an AI but a simulator" ([Mar 7, 2023](https://x.com/karpathy/status/1632800081622761472)), now applied to how to prompt.
- **Verifiability explains jaggedness.** "Software 1.0 easily automates what you can specify. Software 2.0 easily automates what you can verify." Tasks that can be practised, with an environment that is resettable, efficient and rewardable, "progress rapidly", while others lag ([Nov 17](https://x.com/karpathy/status/1990116666194456651)). The year review adds the downside: "benchmarks are almost by construction verifiable environments and are therefore immediately susceptible to RLVR", so "Training on the test set is a new art form" (A06).
- **The cognitive core.** He described "a few billion param model that maximally sacrifices encyclopedic knowledge for capability". It runs on every computer, looks things up, and offers "sovereignty ('not your weights not your brain')" ([Jun 27](https://x.com/karpathy/status/1938626382248149433)). On Dwarkesh he said memorization is "probably holding back the neural networks" and that a billion parameters may be enough. He added "Some basic curriculum needs to be there for knowledge" (T07 ≈00:12:42, ≈01:02:22). See LEARNING.md 2b for the user's reframing.
- **Benchmarks versus real use.**
  - Humanity's Last Exam: tasks "served neatly packaged on a platter" will be solved, but jobs needing "long, multimodal, coherent, error-correcting sequences of tasks" will take longer ([Jan 24](https://x.com/karpathy/status/1882498281089241545)).
  - On the leaderboard paper: "When the data and the anecdotes disagree, the anecdotes are usually right". He proposed OpenRouter usage as a harder-to-game eval ([Apr 30](https://x.com/karpathy/status/1917546757929722115)).
  - On Gemini 3: "Go talk to the model", and look for "an ensemble over private evals" ([Nov 19](https://x.com/karpathy/status/1990854771058913347)).
  - "I always learn a lot more from in-depth analysis of few random cases over dashboards of aggregate statistics" ([Jul 15](https://x.com/karpathy/status/1944885371957031005)).
- **Timelines.** "2025-2035 is the decade of agents", with "a huge amount of work across the board to make it actually work. But it *should* work" ([Jan 24](https://x.com/karpathy/status/1882544526033924438)). After Dwarkesh: "my AI timelines are about 5-10X pessimistic" compared with SF house parties, "but still quite optimistic w.r.t. a rising tide of AI deniers" ([Oct 19](https://x.com/karpathy/status/1979644538185752935)). In the interview he expected AI to stay on the same roughly 2% GDP growth trend as earlier computing: "my expectation is that it stays in the same pattern" (T07 ≈01:22:01–01:25:53). On jobs, radiology is "doing great and is growing". The jobs that change first look "like repetition of one rote task", and even there he expected "AI adopted as a tool at first" ([Sep 25](https://x.com/karpathy/status/1971220449515516391)).

### Human agency and empowerment

- **Benefits flowing to individuals first.** LLMs "generate disproportionate benefit for regular people", because their capability is "simultaneously versatile but also shallow and fallible", and organizations face complexity and inertia. For now "Money can't buy better ChatGPT", but "the moment money can buy dramatically better ChatGPT, things change" (A04, April 7). The year review extends this to vibe coding: "regular people benefit a lot more from LLMs compared to professionals, corporations and governments" (A06).
- **Agency as the scarce trait.** "Agency > Intelligence… Agency is significantly more powerful and significantly more scarce. Are you hiring for agency? Are we educating for agency?" ([Feb 25](https://x.com/karpathy/status/1894099637218545984)).
- **"Team human", made concrete.** He redirected his X payout to a challenge: "It is imperative that humanity not fall while AI ascends… Create something that is specifically designed to uplift team human" ([Aug 4](https://x.com/karpathy/status/1952076108565991588)). The winner worked through hard problems with AI on video. He judged AI "better than what was, but also so far from what could be" ([Aug 19](https://x.com/karpathy/status/1957561075744010253)).
- **His stated reason for working on education.** "My personal big fear is that a lot of this stuff happens on the side of humanity, and that humanity gets disempowered by it." He fears a "WALL-E or Idiocracy" future and calls education the lever. He also said: "pre-AGI education is useful. Post-AGI education is fun", like going to the gym (T07 ≈01:56:33–02:08:00). He called the current AI-tutor capability insufficient: "I'm waiting for that capability" (T07 ≈02:01:03).
- **Risks he names.**
  - Generated video is "directly optimizable" against engagement: "TikTok is nothing compared to what is possible. And I'm not so sure that we will like what 'optimal' looks like" ([Jun 3](https://x.com/karpathy/status/1929634696474120576)).
  - On creative culture and slop: does AI help reach a "height of culture… Or harder, when quick wins are tempting and ~free, and an independent ability to create is stifled" ([Aug 17](https://x.com/karpathy/status/1956765908078387382)).
  - On agents and security: "Conflicted because I want to be an early adopter of LLM agents in my personal computing but the wild west of possibility is holding me back" ([Jun 17](https://x.com/karpathy/status/1934651657444528277)).
  - On Dwarkesh, his most likely bad outcome is "a gradual loss of control and understanding" (T07 ≈01:18:51).
- **Keeping human ability under AI.** To a school board: "You will never be able to detect the use of AI in homework", so grading should move into class. Students should be "proficient in the use of AI, but can also exist without it". Like calculators, they should know enough to "notice it, gut check it, verify it" ([Nov 25](https://x.com/karpathy/status/1993010584175141038)).
- **Ownership in daily life.** His digital hygiene guide: "I prefer to be the customer, not the product in my digital life". He also admitted he keeps Gmail and X, "trading off sovereignty for convenience" ([Mar 19](https://x.com/karpathy/status/1902046003567718810)).

### Coding and thought organization

- **Vibe coding, named and limited.** "There's a new kind of coding I call 'vibe coding'… I 'Accept All' always, I don't read the diffs anymore". He limited it: "It's not too bad for throwaway weekend projects" ([Feb 3](https://x.com/karpathy/status/1886192184808149383)). A Swift app ran on his phone after about an hour: "I didn't even read any docs at all" ([Mar 23](https://x.com/karpathy/status/1903672057327452290)).
- **"Real coding" on a tight leash.** For "code I actually and professionally care about, contrast to vibe code", his loop was: stuff the relevant context in, ask for high-level approaches before code, pick one, review with the API docs open, test, commit. "The emphasis is on keeping a very tight leash on this new over-eager junior intern savant… who also bullshits you all the time", and on "being slow, defensive, careful, paranoid, and on always taking the inline learning opportunity, not delegating" ([Apr 25](https://x.com/karpathy/status/1915581920022585597)).
- **Verification is the work.** "In coding LLMs have collapsed (1) to ~instant, but have done very little to address (2)". "the biggest misunderstanding non-coders have about coding… They think that coding is about writing the code (1). It's not. It's about staring at the code (2)." So the LLM "has to anticipate the computational work of (2) and reduce it as much as possible" ([Jun 5](https://x.com/karpathy/status/1930305209747812559)).
- **A layered toolset by August.** About 75% of his LLM help is still tab completion, because typing code in place is "a high bandwidth way of communicating 'task specification'". He uses agents like Claude Code for larger, easy-to-specify chunks, but "I don't run in YOLO mode" and "they basically don't have a sense of taste". He calls GPT-5 Pro the "final layer of defense" for the hardest bugs. And: "It's the code post-scarcity era - you can just create and then delete thousands of lines of super custom, super ephemeral code now" ([Aug 25](https://x.com/karpathy/status/1959703967694545296)). He also found models "a little too agentic by default" for in-the-loop work ([Aug 10](https://x.com/karpathy/status/1954224651443544436)).
- **Where agents failed him.** For nanochat, agents were "not net useful": the code is "intellectually intense" and the models "kept misunderstanding the code because they have too much memory from all the typical ways of doing things". "For now, autocomplete is my sweet spot". Agents helped with boilerplate and with Rust, where he had a Python reference and tests (T07 ≈00:29:53–00:36:53). His stated preference: "I'd like to go in chunks that I can keep in my head… I want to learn along the way and become better as a programmer, not just get served mountains of code that I'm told works" ([Oct 19](https://x.com/karpathy/status/1979644538185752935)).
- **The tone changes at year end.** "I've never felt this much behind as a programmer… I have a sense that I could be 10X more powerful if I just properly string together what has become available over the last ~year". He described "a new programmable layer of abstraction to master" made of agents, prompts, memory, tools and skills ([Dec 27](https://x.com/karpathy/status/2004607146781278521)). The next day Claude Code found and controlled his home automation system on his local network ([Dec 28](https://x.com/karpathy/status/2005067301511630926)). The 2026 section picks this up.
- **Thinking and reading with LLMs.**
  - His note practice: one Apple Note, append at the top, review by scrolling, "rescue it towards the top". "When I note something down, I feel that I can immediately move on" ([Mar 20](https://x.com/karpathy/status/1902503836067229803)). He had described it in 2022.
  - On "One Thread" versus a new conversation, he listed limits of giant contexts (speed, attention, signal to noise, train–test mismatch) and wanted "active, agentic context management" ([Mar 20](https://x.com/karpathy/status/1902737525900525657)).
  - Reading: "pass 1 is manual, then pass 2 'explain/summarize', pass 3 Q&A" ([Nov 18](https://x.com/karpathy/status/1990577951671509438)).
  - On learning from code: rebuild nanochat yourself with no copy-paste, "If I can't build it, I don't understand it" (T07 ≈00:28:10–00:29:45). On explaining: "if I don't really understand something, I can't explain it" (T07 ≈02:23:20).
- **What "context engineering" means.** "+1 for 'context engineering' over 'prompt engineering'". He sees a "thick layer of non-trivial software" around model calls, including "generation-verification UIUX flows", so "The term 'ChatGPT wrapper' is tired and really, really wrong" ([Jun 25](https://x.com/karpathy/status/1937902205765607626)).

### Engineering and project practice

- **MenuGen: the demo-to-product gap, lived.** He built it with a vibe-coding approach: "I wrote none of the code directly… and I don't really know how the app works". The local demo was quick, "but a bit of a painful slog as a deployed, real app". Most of the work was in the browser configuring services, and "All of this work and state is not even accessible or manipulatable by an LLM" ([May 1](https://x.com/karpathy/status/1917961248031080455)). In the blog post: "I felt like I was 80% done but (foreshadowing...) it was a bit closer to 20%" (A05). A month earlier he had compared modern web apps to "assembling IKEA furniture": "It's not even code, it's... configurations, plumbing, orchestration" ([Mar 27](https://x.com/karpathy/status/1905051558783418370)).
- **Build for agents.**
  - "99.9% of attention is about to be LLM attention, not human attention". Docs should be "a single your_project.md text file" ([Mar 13](https://x.com/karpathy/status/1899876370492383450)).
  - "The primary audience of your thing (product, service, library, …) is now an LLM, not a human… LLMs don’t like to click, they like to curl" ([Apr 22](https://x.com/karpathy/status/1914494203696177444)). "adding a Supabase db to your Vervel app shouldn’t be clicks but curls" ([Apr 22](https://x.com/karpathy/status/1914489538006933770)).
  - Products with rich UIs and opaque binary formats "are ngmi in the era of heavy human+AI collaboration", because an LLM must be able to read and script them ([Jun 5](https://x.com/karpathy/status/1930354382106964079)).
  - In MenuGen: "Don't talk to a developer… Instruct and empower their LLM" (A05).
- **Partial autonomy, not flashy agents.** His YC chapter summary: LLMs are a new OS "fabbed by labs, and distributed like utilities". They are "people spirits", so the opportunity is "partially autonomous products", plus software that is "highly accessible" and built "for agents" ([Jun 19](https://x.com/karpathy/status/1935518272667217925)). The year review describes the app layer the same way: "LLM apps like Cursor bundle and orchestrate LLM calls for specific verticals" (A06).
- **The interface after chat.** "Chatting" with an LLM "feels like using an 80s computer terminal". The GUI will be visual and "generated on-demand, specifically for your prompt" ([May 1](https://x.com/karpathy/status/1917920257257459899)). In November: "The GUI is an intelligent canvas" ([Nov 24](https://x.com/karpathy/status/1992657223785586864)). In the year review: "People actually dislike reading text - it is slow and effortful" (A06).
- **The march of nines.** Demos reach the first nine, "Then you need the second nine, a third nine". "I'm very unimpressed by demos". In production software "it's almost unbounded how terrible something could be" (T07 ≈01:43:11–01:46:25). After driving a new Tesla he reported "Perfect drive, no notes", while adding "there's still more work for the team in the long march of 9s" ([Nov 13](https://x.com/karpathy/status/1988705360723763242)).
- **Code built to be copied.** Write code like bacteria: "small, modular, self-contained and trivial to copy-and-paste". "Build a eukaryotic monorepo backbone if you have to, but maximize bacterial DNA" ([Jul 6](https://x.com/karpathy/status/1941616674094170287)). nanochat's goal is "one cohesive, minimal, readable, hackable, maximally forkable repo" ([Oct 13](https://x.com/karpathy/status/1977755427569111362)).
- **Bugs and skepticism of the defaults.** A train/test split bug in nanochat came from Python's `random.seed` treating 5 and -5 as the same seed. He traced it into the CPython source: "no guarantee is made that different seeds produce different sequences" ([Dec 9](https://x.com/karpathy/status/1998236299862659485)). On RL-trained models: "they are mortally terrified of exceptions" ([Oct 9](https://x.com/karpathy/status/1976077806443569355)).
- **When to finetune.** "finetuning isn't so much about 'stylizing' an LLM, instead, it's a lot more about narrowing the scope". Production apps are "larger pipelines where a bunch of LLMs collaborate in DAGs and flows" ([Oct 2](https://x.com/karpathy/status/1973468610917179630)).
- **What his undergrad missed.** "too little on physical lens - energy/heat of state change, data locality, parallelism, computer architecture. The former is interesting; The latter bestows power" ([May 6](https://x.com/karpathy/status/1919647115099451892)).

### Interpretation (ours, provisional)

1. **Coding advice is sorted by stakes, not a single trend.** In one year he coined vibe coding for throwaway projects, kept a "tight leash" for code he cares about, and for nanochat used mostly autocomplete. The rule underneath is verification cost: his June statement that coding "is about staring at the code" explains all three modes. The December "never felt this much behind" is the first sign of a change in his own practice. It is a statement of feeling, not yet a described new workflow. 2026 should be read against it.
2. **He builds a theory of what models lack.** Jagged intelligence (2024) gets a cause in 2025: what is verifiable gets optimized. He also gives a list of missing pieces: reflection instead of scalar rewards, system prompt learning, culture, a smaller knowledge-light core, and entropy against collapse. His view of RL moves from "significantly significantly more powerful" than imitation (January) to "terrible" but better than what came before (October). We read this as a sharpening, not a reversal: trial-and-error beats imitation, but outcome rewards are a weak way to do it.
3. **The demo-to-product thread becomes his own experience.** In 2024 it was Waymo and "a lot more than code". In 2025 it is MenuGen ("closer to 20%"), the IKEA list and the march of nines. His suggested fix moves the problem: make products and docs legible to LLMs, so agents can do the configuration.
4. **Empowerment is now framed as a race to keep humans capable.** The optimism (benefits flowing to "regular people", vibe coding for everyone) is stronger than before. So is the fear ("humanity gets disempowered", WALL-E, optimizable video, slop). His answers are about human capacity: education as "ramps to knowledge", agency, schools that test without AI, and reading with an LLM only after a manual first pass.
5. **Timelines and demos keep him calibrated.** "Decade of agents", "5-10X pessimistic" and "unimpressed by demos" come from the same self-driving experience that drives the march of nines. It is a consistent position across the year, stated against both hype and denial.

### Uncertainties and gaps

- T07 is a publisher transcript, not audio-checked. T06 has a stated error warning and was not used for quotation.
- Y11 and Y12 (about 5h40m) were not read in full. They may contain more detail on his daily tools and how he checks outputs. Only the closing advice of Y11 ("check their work… own the product of your work") and Y12's deep-research section ("Treat this as your first draft") were read.
- Image-only content is not in the archive: the textbook diagram, the GPT-4.5 poll images, the Excalidraw board, the bacterial-code image and the nano banana outputs.
- Blog posts outside A03–A06 were not read: digital hygiene (quoted in full in its post), the sleep tracker, auto-grading HN, and the Animals vs. Ghosts, Verifiability and Space of Minds posts linked from A06. Two X articles (Apr 8, Dec 20) are link-only in the archive; we take them to be A04 and A06.
- We read "the decade of agents" and "loss of control" as his forecasts, not settled positions. He gives "double digit percent uncertainty" on the Sutton questions ([Oct 2](https://x.com/karpathy/status/1973435013875314729)).

### Questions for the user

1. He has three coding modes by stakes: vibe coding for throwaway work, a "tight leash" for code he cares about, and autocomplete for novel code. For a product you build alone, which parts are throwaway and which do you care about, and what is your verification step for each?
2. "The primary audience of your thing… is now an LLM". If an agent, not a person, were the first user of your product, what would you change: the docs, the interface, the data format?
3. His fear is "humanity gets disempowered", and his answer is education, with ramps and effort. How do you want AI in your own learning to build your capacity rather than replace it? Would you adopt his rule of a manual first pass before asking the LLM?

## 2026: reported changes in coding practice, with original recordings still to verify

**Observation — author-published AI-edited excerpt, T09.** The April 30 [Sequoia text](https://karpathy.bearblog.dev/sequoia-ascent-2026/) retrospectively describes increased trust around December 2025 and revisits MenuGen's need for an app interface. It is not a verbatim transcript.

**Interpretation to test:** distinguish changes in his observed tool performance, working methods and general beliefs; these need not move together. The March [No Priors recording](https://www.youtube.com/watch?v=kwSVtQ7dziU), 2026 X candidates and October 31 [HackerTube](https://karpathy.bearblog.dev/hacker-tube/) remain unreviewed. This is an open period through November 6, not a completed endpoint.

## Four connected research threads

| Lens from the brief | Evidence available now | Main unresolved comparison |
|---|---|---|
| AI fundamentals and limits | Training recipe; syllabus descriptions; opening Dwarkesh excerpt; year review | Actual 2022–2024 explanations versus later learning/intelligence claims |
| Human agency and empowerment | Eureka announcement; Power to the people | Educational aspiration versus outcomes; broad access versus concentration |
| Coding and thought organization | Append-and-review; MenuGen; partial Sequoia text | Personal notes versus AI context design; prototypes versus maintained systems |
| Engineering and project practice | Training recipe; MenuGen | Which practices persist, which adapt, and what original project/recording evidence supports that? |

The strongest next step is to repair the early chronology with original video/transcript evidence and strengthen the 2025–2026 comparison with audio-checked passages. Continue broad inventory alongside that work. Personal applications and beliefs can later enter `LEARNING.md`; none are asserted or approved here.

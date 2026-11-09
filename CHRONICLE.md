# Karpathy: provisional chronological outline

Updated 2026-11-06 (Asia/Shanghai). **Initial outline, not a completed intellectual history.** The 2022 and 2023 sections are written from a full read of each year's X posts. Later sections are still outline-level. Full agreed source scope remains in [README.md](README.md). The working period is 2022 onward, with older explanatory context. Source identities and separate access/review states are in [sources.jsonl](sources.jsonl); [coverage and evidence notes](sources/2026-11-06-inventory-and-evidence.md) explain gaps and review extents.

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

## 2024: an explicit educational design; technical and interview evidence still open

**Observation — reviewed announcement, A02.** The July 16 [Eureka Labs introduction](https://eurekalabs.ai/) proposes teacher-designed courses supported by AI guidance.

**Interpretation:** human expertise and scaled assistance are explicit parts of this proposed product. It is not evidence of successful deployment. The tokenizer/GPT-2 videos, Berkeley and GPU Mode talks, and [No Priors interview](https://www.youtube.com/watch?v=hM_h0UA7upI) remain necessary checks on technical practice, project choice and the relationship between AI and human cognition.

## March–April 2025: organizing thought, broadening individual reach, encountering delivery friction

**Observation — reviewed writing, A03–A05.** The March 19 [note-taking account](https://karpathy.bearblog.dev/the-append-and-review-note/) describes a longstanding practice, not a new AI method. April 7's [empowerment argument](https://karpathy.bearblog.dev/power-to-the-people/) includes possible future concentration of benefits. April 27's [MenuGen account](https://karpathy.bearblog.dev/vibe-coding-menugen/) contrasts rapid construction with integration difficulties.

**Interpretation:** these artifacts connect cognitive simplicity, expanded personal capability and the work of delivering usable products. They do not prove an entrepreneurial formula.

**Observation — archived X post, February 3, 2025 (Beijing time).** The ["vibe coding" post](https://x.com/karpathy/status/1886192184808149383) describes giving in to the vibes: "I 'Accept All' always, I don't read the diffs anymore", with "the code grows beyond my usual comprehension". He limits it explicitly: "It's not too bad for throwaway weekend projects, but still quite amusing." Compare with December 2022's "I prompt. & edit." The 2025 post is about a specific kind of project, not a general working method. The rest of the 2025 X posts and the two general-audience videos remain unreviewed.

## June–December 2025: useful agents, reliability limits and a retrospective assessment

June's [YC talk](https://www.youtube.com/watch?v=LCEmiRjPEtQ) is a registered review target; a linked third-party transcript warns of errors, so no direct speech claims rely on it here.

**Observation — reviewed excerpt, T07.** In the October 17 [Dwarkesh transcript](https://www.dwarkesh.com/p/andrej-karpathy), opening 00:00:07–00:02:57, everyday usefulness coexists with doubts about employee-like autonomy. **Observation — reviewed writing, A06:** the December 19 [year review](https://karpathy.bearblog.dev/year-in-review-2025/) links uneven capabilities, verification and application design.

**Interpretation:** encouragement and caution are simultaneous positions, not necessarily a reversal. The interview's later sections and original YC recording are needed before writing a continuous argument across these dates.

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

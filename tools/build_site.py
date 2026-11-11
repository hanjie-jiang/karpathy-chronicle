"""Build docs/data.js for the public site from a curated event list.

Run from the project root:  python -I tools/build_site.py

- X events: date and URL are taken from the local archive by post ID, and
  every quote must appear verbatim in the archived post text, or the build fails.
- Non-X events (blog posts, talks) carry the date and URL recorded in sources.jsonl
  and are summaries in our words unless marked as a transcript quote.
- The site is a derived view of CHRONICLE.md. When CHRONICLE changes, update this file.

The archive itself (sources/x/*.jsonl) is private and is not published.
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = ROOT / "sources" / "x" / "karpathy-x-posts.jsonl"
OUT = ROOT / "docs" / "data.js"

# lens: milestone | fund | agency | coding | practice
# status: "read" = period fully read; "spot" = post read on its own, period not yet read
X = [
    # ---- 2022 ----
    ("1508148604149587972", "milestone", ["re-sharpen my technical edge and train some neural nets"], "Takes time off after almost five years at Tesla.", []),
    ("1547332301519851520", "milestone", ["revisiting my long-term passions around technical work in AI, open source and education"], "Announces he is leaving Tesla, with no concrete plans.", []),
    ("1559672719414681601", "milestone", ["the culmination of about 8 years of obsessing about the best way to explain neural nets and backprop"], "Releases micrograd, the first lecture in a from-scratch series.", []),
    ("1529514197121384448", "fund", ["alien artifacts", "Obviously powerful, especially if you poke it just right"], "LLMs as unfamiliar objects, not brains.", ["computer"]),
    ("1536061913376776192", "fund", ["models appear to follow smooth scaling laws and data+model size can still plenty grow"], "Expects scale to keep paying off.", []),
    ("1567233122252750848", "fund", ["how much can an AI learn from internet text alone?"], "A limit framed as an open question.", []),
    ("1582807367988654081", "fund", ["general-purpose differentiable computer"], "The Transformer as a general computer.", ["computer"]),
    ("1593081701454204930", "fund", ["cognitive engine"], "The LLM orchestrating calculators, interpreters and search through text.", ["computer"]),
    ("1599488637422694400", "fund", ["Asking them to produce more text is giving them more time to think"], "On ChatGPT: models need tokens to think.", []),
    ("1507893647341142016", "agency", ["First time I feel attacked by AI in the brain"], "On TikTok: attention-optimizing AI as a threat.", ["empower"]),
    ("1561818955966058500", "agency", ["a day of historic proportion for human creativity"], "The Stable Diffusion open release.", ["empower"]),
    ("1600012576825360384", "agency", ["How long until we measure wealth inequality in FLOPS"], "Concentration of compute as a risk.", ["empower"]),
    ("1603835488443330560", "agency", ["necessary for higher stake applications"], "Visible, checkable SQL in a text-to-SQL demo.", ["verify", "oversight"]),
    ("1497652099701620738", "coding", ["Programming turns into a kind of applied psychology of neural nets"], "Prompting as programming.", ["computer"]),
    ("1532852924212072448", "coding", [], "Describes one running note where ideas are added at the top and most sink: the practice he later wrote up in 2025.", []),
    ("1574906895453675521", "coding", ["strong statements that are understood to be only 90% true"], "His communication style, and a reason to read his short claims as deliberately strong.", []),
    ("1608895189078380544", "coding", ["I don't even really code, I prompt. & edit."], "Copilot writes most of his code, and he still edits it.", ["oversight"]),
    ("1486215976559398915", "practice", ["Everybody gangsta until real-world deployment in production."], "Deployment realities over benchmarks.", []),
    ("1558863432023126020", "practice", ["hard to solve but easy to verify"], "The asymmetry that makes progress possible.", ["verify"]),
    ("1574501715990102016", "practice", ["mostly built Lexicap so I could share a few snippets"], "Building small tools for his own needs.", []),
    ("1599852921541128194", "practice", ["not so much to those with data but those with a data engine"], "The data engine as the competitive advantage.", []),
    ("1607791539258003457", "practice", ["educational and 2) efficient in one repo"], "Splits minGPT because teaching and performance are different goals.", []),
    # ---- 2023 ----
    ("1613250487838707712", "milestone", ["simplest, fastest repo for training/finetuning medium-sized GPTs"], "Releases nanoGPT.", []),
    ("1623476659369443328", "milestone", ["personally benefited greatly from"], "Rejoins OpenAI.", []),
    ("1683143097604243456", "milestone", [], "Releases llama2.c: Llama 2 inference in one ~500-line C file.", []),
    ("1617979122625712128", "fund", ["The hottest new programming language is English"], "English as programming.", ["computer"]),
    ("1632800081622761472", "fund", ["not an AI but a simulator"], "A pretrained LLM simulates internet documents.", []),
    ("1638983034522460162", "fund", ["new kind of computer architecture that runs on text"], "GPT as a computer.", ["computer"]),
    ("1642600116837298178", "fund", ["completely unaware of their own strengths and limitations"], "A concrete limit.", []),
    ("1687248476508487681", "fund", ["Algorithmic progress was necessity, now bonus"], "Why scale dominates.", []),
    ("1707437820045062561", "fund", ["the kernel process of a new Operating System"], "The LLM OS framing, on X by September 2023.", ["computer"]),
    ("1733299213503787018", "fund", ["hallucination is all LLMs do"], "The assistant, not the model, has the hallucination problem; fix it with retrieval, sampling and verification.", ["verify"]),
    ("1654892810590650376", "agency", ["cambrian explosion"], "The open-source LLM ecosystem, conditioned on expensive base models.", ["empower"]),
    ("1673450276999815170", "agency", ["Most apps are actively adversarial to users"], "The attention concern continues.", ["empower"]),
    ("1681356674635034625", "agency", ["the most capable LLM available directly as weights to anyone"], "Welcomes Llama 2.", ["empower"]),
    ("1715806187663585287", "agency", ["Protecting your brain at 60Hz"], "An LLM filter that blurs triggering content: a \"programmable exocortex\".", ["empower"]),
    ("1740078732562636929", "agency", ["intelligence augmentation"], "Reads Licklider: augmentation may be a transient stage before automation.", ["empower"]),
    ("1617265772631588865", "coding", ["for any prediction for +x years I first consider -x year delta"], "An annual habit of writing and revisiting predictions.", []),
    ("1620103414490468352", "coding", ["exhausting treasure hunt"], "Against nested indirection in code.", []),
    ("1637151779757621250", "coding", ["quit too fast"], "Working with assistants takes adaptation.", []),
    ("1722359332116062491", "coding", ["until it is ~pass-through"], "Predicts human oversight of coding will rise in abstraction until it barely contributes.", ["oversight"]),
    ("1619749146340237313", "practice", ["high experimental throughput"], "Experimenting as the way to make progress.", []),
    ("1642920043423088640", "practice", ["You need prompt engineers and LLM Ops"], "Building with models rather than training them.", []),
    ("1674873002314563584", "practice", ["One can be quite successful in this role without ever training anything"], "Endorses the \"AI Engineer\" role.", []),
    ("1689819017610227712", "practice", ["How long it takes to make demos *real*"], "Demos versus real products.", []),
    # ---- 2024 (thread-tagged; other cited 2024 posts come from CHRONICLE automatically) ----
    ("1757600075281547344", "milestone", ["My immediate plan is to work on my personal projects"], "Leaves OpenAI.", []),
    ("1777427944971083809", "milestone", ["train LLMs in pure C without 245MB of PyTorch"], "Releases llm.c.", []),
    ("1813263734707790301", "milestone", ["a new kind of school that is AI native"], "Announces Eureka Labs: teacher-designed courses scaled by an AI teaching assistant.", ["empower"]),
    ("1744179910347039080", "agency", ["Of all humans, not a top percentile"], "\"e/ia\": intelligence amplification, tools that empower rather than replace.", ["empower"]),
    ("1815842603377779140", "agency", ["the first time that a frontier-capability LLM is available to everyone to work with and build on"], "Llama 3.1 405B, open weights.", ["empower"]),
    ("1828210213620748655", "agency", ["scrappy solo serial micro-entrepreneur viable"], "Cloud plus AI makes one-person companies viable.", ["empower"]),
    ("1780692023970038259", "fund", ["computers that do statistical arithmetic on tokens"], "The history of computing repeating with LLMs.", ["computer"]),
    ("1835024197506187617", "fund", ["highly general purpose technology for statistical modeling of token streams"], "LLMs have little to do with language.", ["computer"]),
    ("1816531576228053133", "fund", ["Jagged Intelligence", "keep a human in the loop"], "Brilliant at some tasks, failing at simple ones, and not always obvious which is which.", ["verify", "oversight"]),
    ("1862565643436138619", "fund", ["You're asking a human data labeler"], "What you are really talking to when you \"ask an AI\".", ["verify"]),
    ("1767598414945292695", "coding", ["supervising the automation", "How does a human provide oversight?"], "Software engineering will follow self-driving: more autonomy, oversight at a higher level.", ["oversight"]),
    ("1827143768459637073", "coding", ["reviewing and editing the generated diffs"], "With Cursor and Sonnet, most of his programming is now English, and he still reviews.", ["oversight"]),
    ("1804187473167421798", "coding", ["One built-in UI/UX feature of LLM interfaces I'd love is proof"], "He checks commands against the docs to verify the model's recollection.", ["verify"]),
    ("1831776835388285347", "practice", ["making actual apps is a lot more than code"], "Building is not shipping: environment and deployment are the hard part.", []),
    # ---- 2025 (thread-tagged; other cited 2025 posts come from CHRONICLE automatically) ----
    ("1887211193099825254", "milestone", ["Deep Dive into LLMs like ChatGPT"], "A 3.5-hour general-audience video on how LLMs are trained.", []),
    ("1977755427569111362", "milestone", ["full-stack training/inference pipeline of a simple ChatGPT clone"], "Releases nanochat, the planned capstone of his LLM101n course.", []),
    ("1886192184808149383", "coding", ["I don't read the diffs anymore", "throwaway weekend projects"], "Names \"vibe coding\", explicitly limited to throwaway projects.", ["oversight"]),
    ("1915581920022585597", "coding", ["keeping a very tight leash", "always taking the inline learning opportunity, not delegating"], "For code he cares about: approaches first, small changes, review with the docs open, test, commit.", ["oversight", "verify"]),
    ("1930305209747812559", "coding", ["It's about staring at the code"], "LLMs made writing code instant but not checking it, so they should hand over work in small, easy-to-verify steps.", ["verify", "oversight"]),
    ("1959703967694545296", "coding", ["I don't run in YOLO mode", "they basically don't have a sense of taste"], "Describes his layered coding setup and the cleanup agents still need.", ["oversight"]),
    ("1979644538185752935", "coding", ["chunks that I can keep in my head", "make fewer assumptions and ask/collaborate with me"], "Says the industry overshoots tooling relative to present capability.", ["oversight"]),
    ("2004607146781278521", "coding", ["I've never felt this much behind as a programmer"], "At year end: a new layer of agents, prompts and tools to master, and a sense of falling behind.", ["oversight"]),
    ("1990116666194456651", "fund", ["Software 2.0 easily automates what you can verify"], "Verifiability predicts which tasks AI automates, and explains the jagged frontier.", ["verify"]),
    ("1938626382248149433", "fund", ["maximally sacrifices encyclopedic knowledge for capability"], "The \"cognitive core\": a small local model that reasons, looks things up, and stays yours.", ["computer", "empower"]),
    ("1935518272667217925", "fund", ["LLMs are a new kind of computer, and you program them *in English*"], "YC talk summary: LLMs as utilities, fabs and operating systems; build partial-autonomy products.", ["computer"]),
    ("1914494203696177444", "practice", ["is now an LLM, not a human"], "Build docs and products for agents to read and script.", ["computer"]),
    ("1917961248031080455", "practice", ["painful slog as a deployed, real app"], "MenuGen: the demo was quick, deployment was the work, and an LLM could not reach most of it.", []),
    ("1894099637218545984", "agency", ["Agency is significantly more powerful and significantly more scarce"], "Agency over intelligence, in hiring and education.", ["empower"]),
    ("1952076108565991588", "agency", ["It is imperative that humanity not fall while AI ascends"], "Funds a challenge for things that \"uplift team human\".", ["empower"]),
    ("1929634696474120576", "agency", ["TikTok is nothing compared to what is possible"], "Generated video can be optimized directly against engagement, and he doubts we will like the optimum.", ["empower"]),
    ("1993010584175141038", "agency", ["proficient in the use of AI, but can also exist without it"], "To a school board: grade in class, and keep the ability to verify AI.", ["empower", "verify"]),
    # ---- 2026 (thread-tagged; other cited 2026 posts come from CHRONICLE automatically) ----
    ("2015883857489522876", "coding", ["80% agent coding and 20% edits+touchups in December", "watch them like a hawk"], "The proportions flip in one month. Agent mistakes are now conceptual, so code he cares about is still watched closely.", ["oversight"]),
    ("2019137879310836075", "coding", ["acting as oversight", "without any compromise on the quality of the software"], "Names \"agentic engineering\": the professional, overseen version of vibe coding.", ["oversight"]),
    ("2026731645169185220", "coding", ["coding agents basically didn’t work before December and basically work since"], "December 2025 as a threshold in the models, not just in his habits.", ["oversight"]),
    ("2030371219518931079", "coding", ["the human iterates on the prompt (.md)"], "autoresearch: agents run training experiments in a loop; the human writes the instructions.", ["oversight", "verify"]),
    ("2064409694761054332", "coding", ["never felt this tempting to stop looking at the code at all"], "On a new Claude model, as an Anthropic employee, with the caveat \"don't do this in prod!\"", ["oversight"]),
    ("2105819303471976479", "coding", ["rise up the abstractions into oversight and understanding"], "As agents do the legwork, his tools for understanding become diagrams, HTML pages and explainer videos.", ["verify", "oversight"]),
    ("2039805659525644595", "coding", ["more into manipulating knowledge"], "The LLM wiki: an LLM compiles raw sources into a Markdown wiki it maintains, and answers are filed back.", []),
    ("2116957135661945283", "practice", ["I only talk to Claude and have it do everything"], "HackerTube: his only manual work was an API key, a server and a domain name.", ["oversight"]),
    ("2042334451611693415", "fund", ["The goldmines are elsewhere"], "Jaggedness has two causes: verifiable rewards, and what labs choose to train for revenue.", ["verify"]),
    ("2109361546505966046", "fund", ["a sharp funnel"], "The capability gap widens: about 6B barely touched, 20M professionals see it, 5,000 insiders see more.", ["empower"]),
    ("2056753169888334312", "milestone", ["I've joined Anthropic"], "Joins a frontier lab two months after arguing the case for staying independent.", []),
    ("2026360908398862478", "practice", ["Build. For. Agents."], "A checklist: Markdown docs, skills, a CLI or MCP for every product.", ["computer"]),
    ("2024583544157458452", "practice", ["highly custom, ephemeral apps"], "No more app store: services become sensors and actuators that agents glue together on the spot.", ["computer"]),
    ("2036487306585268612", "practice", ["this has to be re-evaluated"], "After a supply-chain attack: fewer dependencies, let an LLM \"yoink\" the functionality instead.", []),
    ("2017442712388309406", "agency", ["a complete mess of a computer security nightmare at scale"], "On a social network of 150,000 agents: overhyped today, not in principle.", ["empower"]),
    ("2040549459193704852", "agency", ["increasing the visibility, legibility and accountability of their governments"], "AI lets citizens read what governments publish.", ["empower"]),
    ("2040572272944324650", "agency", ["puts *you* in full control"], "Personal memory as files you own and can inspect, usable with any AI.", ["empower"]),
    ("2037921699824607591", "agency", ["super useful as a tool for forming your own opinions"], "Use LLMs to argue several directions, and watch for sycophancy.", ["empower"]),
]
READ_YEARS = {2022, 2023, 2024, 2025, 2026}

OTHER = [
    dict(date="2019-04-25", lens="practice", kind="writing", title="A Recipe for Training Neural Networks", url="https://karpathy.github.io/2019/04/25/recipe/",
         note="Data inspection, simple baselines and incremental validation, against silent failures. Context before the main period.", threads=["verify"], status="read"),
    dict(date="2023-05-23", lens="coding", kind="talk", title="State of GPT (talk)", url="https://www.youtube.com/watch?v=bZQun8Y4L2A",
         quotes=["think co-pilots, instead of completely autonomous agents"], note="Advice: low-stakes uses, always with human oversight. Recommendations section only, third-party transcript.", threads=["oversight"], status="read"),
    dict(date="2023-11-24", lens="fund", kind="talk", title="Intro to Large Language Models (video)", url="https://www.youtube.com/watch?v=zjkBMFhNj_g",
         note="Presents the LLM OS diagram to a general audience. Tool-use and LLM OS passages only.", threads=["computer"], status="read"),
    dict(date="2024-07-16", lens="milestone", kind="writing", title="Eureka Labs announced", url="https://eurekalabs.ai/",
         note="Teacher-designed courses supported by AI guidance. A proposed product, not evidence of outcomes.", threads=["empower"], status="read"),
    dict(date="2025-03-19", lens="coding", kind="writing", title="The append-and-review note", url="https://karpathy.bearblog.dev/the-append-and-review-note/",
         note="Writes up the single-note practice already visible in June 2022.", threads=[], status="read"),
    dict(date="2025-04-07", lens="agency", kind="writing", title="Power to the people", url="https://karpathy.bearblog.dev/power-to-the-people/",
         note="LLMs benefit regular people more than organizations, for now. That changes if money can buy a much better model.", threads=["empower"], status="read"),
    dict(date="2025-04-27", lens="practice", kind="writing", title="Vibe coding MenuGen", url="https://karpathy.bearblog.dev/vibe-coding-menugen/",
         note="Felt 80% done, was closer to 20%: integration and deployment were the hard part. Calls for services an LLM can configure.", threads=[], status="read"),
    dict(date="2025-10-17", lens="fund", kind="talk", title="Dwarkesh Podcast interview", url="https://www.dwarkesh.com/p/andrej-karpathy",
         note="Decade of agents; RL as \"sucking supervision through a straw\"; agents not net useful for novel code; the march of nines; education against disempowerment. Read in full (publisher transcript).", threads=["oversight", "empower"], status="read"),
    dict(date="2025-12-19", lens="fund", kind="writing", title="2025 year in review", url="https://karpathy.bearblog.dev/year-in-review-2025/",
         note="RL on verifiable rewards, jagged \"ghost\" intelligence, distrust of benchmarks, the LLM app layer, agents on your computer, vibe coding, and a new GUI.", threads=["verify"], status="read"),
    dict(date="2026-03-20", lens="coding", kind="talk", title="No Priors interview, \"Skill Issue\"", url="https://www.youtube.com/watch?v=kwSVtQ7dziU",
         note="No code typed since December; remove yourself as the bottleneck; autoresearch; jokes outside the RL; the case for and against joining a frontier lab; explaining to agents, not people. Read in full (third-party transcript).", threads=["oversight", "verify", "empower"], status="read"),
    dict(date="2026-04-29", lens="coding", kind="talk", title="Sequoia AI Ascent 2026", url="https://karpathy.bearblog.dev/sequoia-ascent-2026/",
         note="Vibe coding raises the floor, agentic engineering the ceiling; some apps (MenuGen) shouldn't exist; jaggedness = verifiable plus \"labs care\"; you can't outsource your understanding. Read in full in the AI-edited text he published, not verbatim.", threads=["oversight", "verify"], status="read"),
    dict(date="2026-10-31", lens="practice", kind="writing", title="HackerTube", url="https://karpathy.bearblog.dev/hacker-tube/",
         note="A video site built in about 2 hours by talking to Claude only: \"I don't actually _do_ anything resembling traditional engineering anymore\".", threads=["oversight"], status="read"),
]

THREADS = [
    dict(id="oversight", title="How much to oversee AI-written code",
         reading="Our reading: not a straight line toward less oversight. Advice depends on stakes and on the tools of the moment. He limits 'vibe coding' to throwaway projects and, for code you care about, still says to watch closely. In 2025 he sorts his tools by stakes, and at year end says he feels behind. In 2026 agents write nearly everything, but 'don't do this in prod!' keeps the stakes split alive."),
    dict(id="verify", title="Verification as the bottleneck",
         reading="Our reading: a recurring concern from 2019 onward, inferred by us at first. In 2025 he states it himself: coding 'is about staring at the code', and verifiability decides what AI automates. In 2026 checking moves into the setup: success criteria, tests first, metrics an agent can climb."),
    dict(id="computer", title="The LLM as a new kind of computer",
         reading="Our reading: the analogy builds in steps, from 'differentiable computer' (2022) to 'LLM OS' (Sept 2023), then to 'statistical modeling of token streams' (2024). This dates when he said it publicly, not when he first thought it."),
    dict(id="empower", title="Empowerment and its risks",
         reading="Our reading: excitement about open tools and individual reach sits beside warnings about attention-exploiting apps and concentration. Both are held at once. In 2026 he adds citizens auditing governments and personal data you own, then joins a frontier lab."),
]

PERIODS = [
    dict(id="2022", title="Leaving management, returning to building and teaching", range=["2022-01-01", "2022-12-31"], status="read",
         coverage="All 251 X posts read. Lex interview: located passages only. Lectures not reviewed.",
         summary="He leaves Tesla to \"do a lot more technical stuff\", releases from-scratch lectures, and by December reports that Copilot writes most of his code.",
         interpretation=["The clearest change is in his role (manager to builder and teacher), not in his beliefs: scaling, Transformers and data engines continue his earlier framing.",
                         "Deep understanding of how models work and delegating code to them coexisted: he prompts and edits.",
                         "Verification recurs, and optimism and caution about empowerment are held together."]),
    dict(id="2023", title="Back at OpenAI, building a vocabulary for using LLMs", range=["2023-01-01", "2023-12-31"], status="read",
         coverage="All 186 X posts read. State of GPT and Intro to LLMs: selected sections only.",
         summary="Focus moves from how models are built to how they are used: English as programming, the LLM OS, the AI Engineer role, LLMs as \"dream machines\".",
         interpretation=["In May he advises co-pilots with human oversight. In November he predicts oversight becoming \"~pass-through\". We read the first as advice and the second as forecast; he does not reconcile them.",
                         "Verification becomes concrete: retrieval, multiple samples, verification chains.",
                         "Open weights, personal hardware and protective filters point toward individual control."]),
    dict(id="2024", title="Independent again, naming the limits, putting empowerment first", range=["2024-01-01", "2024-12-31"], status="read",
         coverage="All 203 X posts read. Sequoia and No Priors interviews read in full, Berkeley talk segment read (third-party transcripts). Tokenizer and GPT-2 lectures not read.",
         summary="He leaves OpenAI, builds llm.c and reproduces GPT-2 in public, and starts Eureka Labs. He coins \"jagged intelligence\" and calls himself \"team human\".",
         interpretation=["His most explicit year on empowerment so far: \"IA\" not AI, \"of all humans, not a top percentile\", AGI as \"a magnifier of power\". He admits he would still rent a better closed model, with open ones as a fallback.",
                         "A sharper vocabulary for limits (jagged intelligence, lossy recollection, the average data labeler, the junior-intern test) always ends in oversight or verification, not withdrawal.",
                         "Oversight moves up a level but does not vanish: in August he still reviews the diffs. The gap between demo and product becomes a theme that anticipates MenuGen in 2025."]),
    dict(id="2025", title="Vibe coding, building for agents, and what models lack", range=["2025-01-01", "2025-12-31"], status="read",
         coverage="All 158 X posts read. Dwarkesh interview read in full (publisher transcript); YC talk via his own summary; four blog posts read. The two general-audience videos: short passages only.",
         summary="He names vibe coding and limits it to throwaway projects, vibe-codes MenuGen and hits the deployment wall, releases nanochat, and builds a theory of what models lack. At year end he says he has \"never felt this much behind as a programmer\".",
         interpretation=["Coding advice is sorted by stakes: vibe coding for throwaway work, a \"tight leash\" for code he cares about, autocomplete for novel code. Verification cost is the rule underneath.",
                         "Jagged intelligence gets a cause (what is verifiable gets optimized) and a list of missing pieces: reflection instead of scalar rewards, system prompt learning, culture, a knowledge-light cognitive core.",
                         "The demo-to-product gap becomes personal (MenuGen) and turns into a design rule: make products and docs readable by LLMs.",
                         "Empowerment becomes a race to keep humans capable: stronger optimism about regular people, and a stated fear that humanity \"gets disempowered\"."]),
    dict(id="2026", title="Agentic engineering, out of the loop, into a frontier lab", range=["2026-01-01", "2026-11-06"], status="read",
         coverage="All 70 X posts read (to Nov 2). No Priors interview and Sequoia AI Ascent text read in full (third-party and AI-edited transcripts); HackerTube post read. Open period.",
         summary="Coding agents \"basically work\" since December: he goes from 80% agent coding to \"I only talk to Claude\". He builds autoresearch and an LLM wiki, names \"agentic engineering\", and joins Anthropic in May.",
         interpretation=["Verification moves from reading code to designing checks: success criteria, tests first, metrics an agent can climb. The stakes split survives (\"don't do this in prod!\").",
                         "\"Remove yourself as the bottleneck\" partly reverses his 2025 wish to learn along the way. The human job becomes understanding, and he admits his code-writing ability is atrophying.",
                         "Jaggedness = verifiable × what labs choose to train for revenue. The capability gap becomes a \"sharp funnel\".",
                         "He argued in March for staying independent, then joined a frontier lab in May. After that he posts far less, partly about his employer's products."]),
]


# ---- Belief tracks (prototype: one track) ----
# One question, a few dated stations in his words, placed on an ordered scale.
# kind: practice (his own coding) | forecast | advice (to others) | feeling
# lane: "care" (code he cares about) | "throwaway" (projects where mistakes cost little)
# level: 1..4 on the scale below; the label and note are ours, the quote is his.
# X stations take date and URL from the archive and the quote must be verbatim.
TRACKS = [
    dict(id="oversight", prototype=True,
         question="How much of the coding does he hand to AI?",
         scale_note="His own image for this is the \"autonomy slider\". The four steps are our wording.",
         levels=["He writes; AI autocompletes", "AI drafts; he reads every change", "Agents write; he watches closely", "AI writes; he doesn't read it"],
         stations=[
             dict(x="1608895189078380544", kind="practice", lane="care", level=2, short="prompt & edit", change="Start",
                  quote="I don't even really code, I prompt. & edit.", note="Copilot writes about 80% of his code. He still edits it."),
             dict(date="2023-05-23", url="https://www.youtube.com/watch?v=bZQun8Y4L2A", source="State of GPT talk (third-party transcript)",
                  kind="advice", lane="care", level=2, short="co-pilots, not agents", change="Advice",
                  quote="think co-pilots, instead of completely autonomous agents", note="His advice to developers: keep a human in the loop."),
             dict(x="1722359332116062491", kind="forecast", lane="care", level=4, short="forecast: ~pass-through", change="Forecast",
                  quote="Human input and oversight gradually ascends in abstraction and contributes less, until it is ~pass-through.",
                  note="A prediction about where coding is heading, not a description of his own work."),
             dict(x="1767598414945292695", kind="forecast", lane="care", level=3, short="how to oversee?", change="Forecast",
                  quote="How does a human provide oversight?", note="Expects coding to follow self-driving: more automation, with the human supervising."),
             dict(x="1827143768459637073", kind="practice", lane="care", level=2, short="reviews the diffs", change="Same",
                  quote="reviewing and editing the generated diffs", note="With Cursor and Sonnet, most of his programming is English, and he still reads the changes."),
             dict(x="1886192184808149383", kind="practice", lane="throwaway", level=4, short="vibe coding", change="Splits by stakes",
                  quote="I don't read the diffs anymore", note="Names vibe coding and limits it to \"throwaway weekend projects\"."),
             dict(x="1915581920022585597", kind="practice", lane="care", level=2, short="tight leash", change="Splits by stakes",
                  quote="keeping a very tight leash on this new over-eager junior intern savant",
                  note="For code he cares about: approaches first, small steps, review with the docs open, test, commit."),
             dict(x="1917961248031080455", kind="practice", lane="throwaway", level=4, short="MenuGen", change="Same",
                  quote="I wrote none of the code directly", note="A vibe-coded web app. Building was easy; deploying it was the hard part."),
             dict(x="1930305209747812559", kind="advice", lane="care", level=2, short="the work is checking", change="Advice",
                  quote="It's about staring at the code", note="Writing code got instant; checking it did not. This is the rule under the whole track."),
             dict(x="1959703967694545296", kind="practice", lane="care", level=1, short="mostly tab complete", change="Moves down",
                  quote="the bread & butter (~75%?) of my LLM assistance continues to be just (Cursor) tab complete",
                  note="Agents for larger chunks, but \"I don't run in YOLO mode\"."),
             dict(date="2025-10-17", url="https://www.dwarkesh.com/p/andrej-karpathy", source="Dwarkesh Podcast (publisher transcript, ≈00:35:42)",
                  kind="practice", lane="care", level=1, short="autocomplete for nanochat", change="Same",
                  quote="For now, autocomplete is my sweet spot.", note="For novel code like nanochat, agents were \"not net useful\"."),
             dict(x="2004607146781278521", kind="feeling", lane="care", level=None, short="\"never felt this much behind\"", change="Turning point",
                  quote="I've never felt this much behind as a programmer.", note="A feeling, not yet a new workflow: a new layer of agents and tools to master."),
             dict(x="2015883857489522876", kind="practice", lane="care", level=3, short="80% agents, watched closely", change="Moves up",
                  quote="80% agent coding and 20% edits+touchups in December",
                  note="Up from \"about 80% manual+autocomplete\" in November. Still: \"watch them like a hawk\"."),
             dict(x="2019137879310836075", kind="advice", lane="care", level=3, short="agentic engineering", change="Advice",
                  quote="you are orchestrating agents who do and acting as oversight", note="His name for professional agent work: leverage \"without any compromise on the quality of the software\"."),
             dict(date="2026-03-20", url="https://www.youtube.com/watch?v=kwSVtQ7dziU", source="No Priors interview (third-party transcript)",
                  kind="practice", lane="care", level=3, short="no code typed since Dec", change="Moves up",
                  quote="I don't think I've typed like a line of code probably since December basically.", note="He reviews agents' work \"depending on how much you care about that code\"."),
             dict(x="2064409694761054332", kind="advice", lane="care", level=3, short="tempting to stop looking", change="Advice",
                  quote="never felt this tempting to stop looking at the code at all (but don't do this in prod!)", note="Written as an Anthropic employee about a new Claude model."),
             dict(x="2116957135661945283", kind="practice", lane="throwaway", level=4, short="only talks to Claude", change="Same",
                  quote="I only talk to Claude and have it do everything", note="HackerTube, a weekend project. Manual work: an API key, a server, a domain."),
         ],
         reading="Not a steady climb. For code he cares about, his own practice stays at or below \"reads every change\" for three years, and in 2025 even drops to mostly autocomplete, while his 2023 forecast pointed to \"~pass-through\". From February 2025 he splits by stakes: throwaway projects go to the top. The real jump for code he cares about comes in December 2025, and even then he says to watch the agents closely. By March 2026 he types no code at all, yet for production he still says \"don't do this in prod!\": the top step stays reserved for throwaway projects."),
]


# ---- Attention: share of posts per half-year that touch each theme ----
# Counted automatically by keyword over every archived post from 2022 on.
# This measures what he talks about, not what he believes. Spot checks
# (2026-11-10, 12-15 random matches per theme) found roughly 75-90% of
# matches on topic. The lists are deliberately simple so anyone can audit them.
ATTENTION = [
    ("coding", "Coding with AI", r"\b(copilot|cursor|vibe.?cod\w*|claude code|codex|autocomplet\w*|tab complete|(?<!regular )programming|programmers?|coding|codebase|diffs?|pull requests?)\b", re.I),
    ("agents", "Agents", r"\b(agents?|agentic|operator|autonom\w*|computer use)\b", re.I),
    ("checking", "Checking AI's work", r"\b(verif\w*|hallucinat\w*|evals?|evaluations?|benchmark\w*|double.?check\w*|leaderboard|bugs?|test set|correctness)\b", re.I),
    ("training", "How models learn", r"\b(RL|RLHF|RLVR)\b|\b(reinforcement learning|pretrain\w*|finetun\w*|fine-tun\w*|rewards?|imitation|synthetic data|scaling laws?|cognitive core)\b", 0),
    ("teaching", "Teaching and learning", r"\b(lectures?|(?<!of )courses?|education\w*|teach\w*|students?|schools?|tutor\w*|eureka|LLM101n|curriculum|textbooks?)\b", re.I),
    ("power", "Who benefits", r"\b(empower\w*|humanity|team human|regular people|open.?weights?|open.?source|privacy|sovereignty|agency|dark patterns?|centraliz\w*|power to the people)\b", re.I),
]


def build_attention(posts, events):
    # half-years; the open year 2026 is one bucket (too few posts to split)
    half = lambda d: d[:4] if d[:4] == "2026" else f"{d[:4]} H{1 if int(d[5:7]) <= 6 else 2}"
    pool = sorted((p for p in posts.values() if p["year"] >= 2022), key=lambda p: p["date_cst"])
    buckets = sorted({half(p["date_cst"]) for p in pool})
    totals = [sum(1 for p in pool if half(p["date_cst"]) == b) for b in buckets]
    quote = {e["url"]: e["quotes"][0] for e in events if e.get("kind") == "post" and e.get("quotes")}
    themes = []
    for tid, label, rx, flags in ATTENTION:
        pat = re.compile(rx, flags) if flags else None
        if not flags:  # first group case-sensitive (RL acronyms), second case-insensitive
            a, b = rx.split("|\\b(", 1)
            pa, pb = re.compile(a), re.compile("\\b(" + b, re.I)
            match = lambda t: pa.search(t) or pb.search(t)
        else:
            match = pat.search
        hits = [[] for _ in buckets]
        for p in pool:
            if match(p["text"]):
                hits[buckets.index(half(p["date_cst"]))].append(
                    dict(date=p["date_cst"], url=p["url"], quote=quote.get(p["url"], "")))
        themes.append(dict(id=tid, label=label, counts=[len(h) for h in hits], posts=hits))
    return dict(buckets=buckets, totals=totals, themes=themes,
                note="Counted automatically by keyword across every archived post since 2022. It shows what he talks about, not what he believes. Some matches are off-topic.")


def build_tracks(posts, errors):
    out = []
    for tr in TRACKS:
        stations = []
        for i, s in enumerate(tr["stations"], 1):
            s = dict(s, n=i)
            if "x" in s:
                p = posts.get(s["x"])
                if not p:
                    errors.append(f"track post missing: {s['x']}")
                    continue
                if s["quote"] not in p["text"]:
                    errors.append(f"track quote not verbatim in {s['x']}: {s['quote']!r}")
                s.update(date=p["date_cst"], url=p["url"], source="X post",
                         status="read" if p["year"] in READ_YEARS else "spot")
                del s["x"]
            else:
                s["status"] = "read" if int(s["date"][:4]) in READ_YEARS else "spot"
            stations.append(s)
        out.append(dict(tr, stations=stations))
    return out


CHRONICLE = ROOT / "CHRONICLE.md"
REPO_URL = "https://github.com/hanjie-jiang/karpathy-chronicle/blob/main/CHRONICLE.md"
LENS_HEADINGS = {
    "context": "milestone",
    "ai fundamentals and limits": "fund",
    "human agency and empowerment": "agency",
    "coding and thought organization": "coding",
    "engineering and project practice": "practice",
}
LINK = re.compile(r"\[[^\]]*\]\(https://x\.com/karpathy/status/(\d+)\)")
QUOTE = re.compile(r"\"([^\"]+)\"|“([^”]+)”")


def slug(heading):
    """GitHub's anchor for a Markdown heading."""
    s = heading.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


REPO_BLOB = "https://github.com/hanjie-jiang/karpathy-chronicle/blob/main/"
PRIVATE_SECTIONS = {"questions for the user"}  # prompts addressed to the owner, not to readers


def inline(t):
    """Escape HTML, then render links, bold and italics."""
    t = html.escape(t, quote=False)
    def link(m):
        url = m.group(2)
        if not re.match(r"https?://", url):
            url = REPO_BLOB + url  # repo-relative file
        return f'<a href="{html.escape(url)}" target="_blank" rel="noopener">{m.group(1)}</a>'
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])_(.+?)_(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)([^*]+?)\*(?![\w*])", r"<em>\1</em>", t)
    return t


def md_to_html(md):
    """Small Markdown subset used by CHRONICLE: ###, paragraphs, - and 1. lists (one nesting level)."""
    out, para, stack = [], [], []  # stack of open list tags, by indent level
    blank = False

    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    def close_lists(depth=0):
        while len(stack) > depth:
            out.append(f"</li></{stack.pop()}>")

    for raw in md.splitlines():
        line = raw.rstrip()
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)", line)
        if not line.strip():
            flush_para()
            blank = True
            continue
        if stack and blank and not m and not raw.startswith("  "):
            close_lists()  # a paragraph after a blank line ends the list
        blank = False
        if line.startswith("### "):
            flush_para(); close_lists()
            out.append(f"<h4>{inline(line[4:])}</h4>")
        elif m:
            flush_para()
            depth = 1 if len(m.group(1)) >= 2 else 0
            tag = "ol" if m.group(2)[0].isdigit() else "ul"
            if len(stack) < depth + 1:
                out.append(f"<{tag}><li>")
                stack.append(tag)
            else:
                close_lists(depth + 1)
                out.append("</li><li>")
            out.append(inline(m.group(3)))
        elif stack:
            out.append(" " + inline(line.strip()))  # continuation of a list item
        else:
            para.append(line.strip())
    flush_para(); close_lists()
    return "\n".join(out)


def chapters():
    """Chapter HTML per year: every ## section naming that year, minus private subsections."""
    text = CHRONICLE.read_text(encoding="utf-8")
    result = {}
    for sec in re.split(r"\n(?=## )", text):
        head = sec.splitlines()[0]
        m = re.search(r"\b(20\d\d)\b", head)
        if not head.startswith("## ") or not m:
            continue
        body = sec.split("\n", 1)[1] if "\n" in sec else ""
        parts = re.split(r"\n(?=### )", "\n" + body)
        keep = [p for p in parts if p.strip().splitlines()[0][4:].strip().lower() not in PRIVATE_SECTIONS] if body.strip() else []
        sub = f"<h3>{inline(head[3:])}</h3>\n" if not head[3:].startswith(m.group(1)) else ""
        result.setdefault(m.group(1), []).append(sub + md_to_html("\n".join(keep)))
    return {y: "\n".join(v) for y, v in result.items()}


def plain(seg):
    """The sentence of chronicle prose that leads up to a citation, without Markdown."""
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", seg)
    t = re.sub(r"[*_`]", "", t)
    t = re.split(r"\n\s*-\s+", t)[-1].replace("\n", " ")  # last nested sub-bullet only
    t = re.sub(r"^[\s).;,:-]+", "", t).rstrip(" (;,")
    last = re.split(r"(?<=[.!?])\s+(?=[A-Z\"“])", t)[-1]
    if last.count('"') % 2 == 0:  # don't cut a sentence inside a quotation
        t = last
    t = re.sub(r"^(also|and|then)\b[:,]?\s*", "", t.strip(" (;,.:"), flags=re.I).strip(" (;,:")
    if t and not t.endswith((".", "!", "?", '"', "”")):
        t += "."
    return (t[:1].upper() + t[1:])[:220]


def chronicle_events(posts, curated_ids, errors):
    """Every X post cited in a fully read period's lens sections becomes an event.

    Lens comes from the ### heading; quotes are the quoted fragments in the same
    paragraph that appear verbatim in that post; the note is the bullet's bold lead.
    """
    text = CHRONICLE.read_text(encoding="utf-8")
    events, anchors = [], {}
    year, lens = None, None
    for block in re.split(r"\n(?=## |### |- |\n)", text):
        line = block.strip()
        if not line:
            continue
        m = re.search(r"\b(20\d\d)\b", line.splitlines()[0])
        if line.startswith("## "):
            year = int(m.group(1)) if m else None
            if m:
                anchors.setdefault(str(year), REPO_URL + "#" + slug(line[3:].splitlines()[0]))
            lens = None
            continue
        if line.startswith("### "):
            lens = LENS_HEADINGS.get(line[4:].splitlines()[0].strip().lower())
            continue
        if year not in READ_YEARS or not lens:
            continue
        lead = re.match(r"-?\s*\*\*(.+?)\*\*", line)
        note = lead.group(1).rstrip(".") + "." if lead else ""
        frags = [a or b for a, b in QUOTE.findall(line)]
        prev_end = lead.end() if lead else 0
        for lm in LINK.finditer(line):
            pid = lm.group(1)
            seg, prev_end = line[prev_end:lm.start()], lm.end()
            if pid in curated_ids:
                continue
            clause = plain(seg)
            p = posts.get(pid)
            if not p:
                errors.append(f"CHRONICLE cites post missing from archive: {pid}")
                continue
            quotes = []
            for f in frags:
                piece = max((s.strip(" .,") for s in f.split("…")), key=len)
                if len(piece) > 12 and piece in p["text"] and piece not in quotes:
                    quotes.append(piece)
            events.append(dict(date=p["date_cst"], lens=lens, kind="post", url=p["url"], quotes=quotes[:2],
                               note=clause if len(clause) > 15 else (note or "Cited in the chronicle."),
                               threads=[], status="read"))
            curated_ids.add(pid)
    return events, anchors


def main():
    posts = {}
    for line in ARCHIVE.open(encoding="utf-8"):
        d = json.loads(line)
        posts[d["id"]] = d
    events, errors = [], []
    extra, anchors = chronicle_events(posts, {x[0] for x in X}, errors)
    events += extra
    chap = chapters()
    for p in PERIODS:
        p["chapter"] = anchors.get(p["id"])
        p["chapter_html"] = chap.get(p["id"], "")
    for pid, lens, quotes, note, threads in X:
        p = posts.get(pid)
        if not p:
            errors.append(f"missing post {pid}")
            continue
        for q in quotes:
            if q not in p["text"]:
                errors.append(f"quote not verbatim in {pid}: {q!r}")
        events.append(dict(date=p["date_cst"], lens=lens, kind="post", url=p["url"], quotes=quotes, note=note,
                           threads=threads, status="read" if p["year"] in READ_YEARS else "spot"))
    for o in OTHER:
        events.append(dict(quotes=[], **o) if "quotes" not in o else dict(o))
    tracks = build_tracks(posts, errors)
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    events.sort(key=lambda e: e["date"])
    read_posts = sum(1 for p in posts.values() if p["year"] in READ_YEARS)
    total_posts = sum(1 for p in posts.values() if p["year"] >= 2022)
    data = dict(updated="2026-11-10", events=events, threads=THREADS, periods=PERIODS, tracks=tracks,
                attention=build_attention(posts, events),
                posts_read=read_posts, posts_total=total_posts)
    OUT.write_text("// Generated by tools/build_site.py. Do not edit by hand.\nwindow.CHRONICLE = "
                   + json.dumps(data, ensure_ascii=False, indent=1) + ";\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(events)} events ({len(extra)} added from CHRONICLE), all X quotes verbatim")
    missing = [p["id"] for p in PERIODS if not p["chapter"]]
    if missing:
        print("warning: no CHRONICLE heading for periods", missing)


if __name__ == "__main__":
    main()

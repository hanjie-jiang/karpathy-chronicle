"""Build docs/data.js for the public site from a curated event list.

Run from the project root:  python -I tools/build_site.py

- X events: date and URL are taken from the local archive by post ID, and
  every quote must appear verbatim in the archived post text, or the build fails.
- Non-X events (blog posts, talks) carry the date and URL recorded in sources.jsonl
  and are summaries in our words unless marked as a transcript quote.
- The site is a derived view of CHRONICLE.md. When CHRONICLE changes, update this file.

The archive itself (sources/x/*.jsonl) is private and is not published.
"""
import json
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
    # ---- spot-read later posts (periods not yet fully read) ----
    ("1886192184808149383", "coding", ["I don't read the diffs anymore", "throwaway weekend projects"], "Names \"vibe coding\", explicitly limited to throwaway projects.", ["oversight"]),
    ("1959703967694545296", "coding", ["I don't run in YOLO mode", "they basically don't have a sense of taste"], "Describes his layered coding setup and the cleanup agents still need.", ["oversight"]),
    ("1979644538185752935", "coding", ["chunks that I can keep in my head", "make fewer assumptions and ask/collaborate with me"], "Says the industry overshoots tooling relative to present capability.", ["oversight"]),
    ("2015883857489522876", "coding", ["watch them like a hawk", "make wrong assumptions on your behalf"], "Agent mistakes are now conceptual; CLAUDE.md instructions only partly fix them. Source of community \"Karpathy skills\" files.", ["oversight"]),
    ("2037921699824607591", "agency", ["super useful as a tool for forming your own opinions"], "Use LLMs to argue several directions, and watch for sycophancy.", ["empower"]),
]
READ_YEARS = {2022, 2023}

OTHER = [
    dict(date="2019-04-25", lens="practice", kind="writing", title="A Recipe for Training Neural Networks", url="https://karpathy.github.io/2019/04/25/recipe/",
         note="Data inspection, simple baselines and incremental validation, against silent failures. Context before the main period.", threads=["verify"], status="read"),
    dict(date="2023-05-23", lens="coding", kind="talk", title="State of GPT (talk)", url="https://www.youtube.com/watch?v=bZQun8Y4L2A",
         quotes=["think co-pilots, instead of completely autonomous agents"], note="Advice: low-stakes uses, always with human oversight. Recommendations section only, third-party transcript.", threads=["oversight"], status="read"),
    dict(date="2023-11-24", lens="fund", kind="talk", title="Intro to Large Language Models (video)", url="https://www.youtube.com/watch?v=zjkBMFhNj_g",
         note="Presents the LLM OS diagram to a general audience. Tool-use and LLM OS passages only.", threads=["computer"], status="read"),
    dict(date="2024-07-16", lens="milestone", kind="writing", title="Eureka Labs announced", url="https://eurekalabs.ai/",
         note="Teacher-designed courses supported by AI guidance. A proposed product, not evidence of outcomes.", threads=["empower"], status="spot"),
    dict(date="2025-03-19", lens="coding", kind="writing", title="The append-and-review note", url="https://karpathy.bearblog.dev/the-append-and-review-note/",
         note="Writes up the single-note practice already visible in June 2022.", threads=[], status="spot"),
    dict(date="2025-04-07", lens="agency", kind="writing", title="Power to the people", url="https://karpathy.bearblog.dev/power-to-the-people/",
         note="LLMs benefiting individuals first, with possible future concentration of benefits.", threads=["empower"], status="spot"),
    dict(date="2025-04-27", lens="practice", kind="writing", title="Vibe coding MenuGen", url="https://karpathy.bearblog.dev/vibe-coding-menugen/",
         note="Building was fast; integration and deployment were the hard part.", threads=[], status="spot"),
    dict(date="2025-10-17", lens="fund", kind="talk", title="Dwarkesh Podcast interview", url="https://www.dwarkesh.com/p/andrej-karpathy",
         note="Everyday usefulness alongside doubts about employee-like autonomy. Opening excerpt only.", threads=["oversight"], status="spot"),
    dict(date="2025-12-19", lens="fund", kind="writing", title="2025 year in review", url="https://karpathy.bearblog.dev/year-in-review-2025/",
         note="Uneven capabilities, verification and application design.", threads=["verify"], status="spot"),
    dict(date="2026-04-30", lens="coding", kind="talk", title="Sequoia Ascent 2026 (edited text)", url="https://karpathy.bearblog.dev/sequoia-ascent-2026/",
         note="Retrospectively describes increased trust in agents around December 2025. AI-edited excerpt, not verbatim.", threads=["oversight"], status="spot"),
]

THREADS = [
    dict(id="oversight", title="How much to oversee AI-written code",
         reading="Our reading: not a straight line toward less oversight. Advice depends on stakes and on the tools of the moment. He limits 'vibe coding' to throwaway projects and, for code you care about, still says to watch closely."),
    dict(id="verify", title="Verification as the bottleneck",
         reading="Our reading: a recurring concern from 2019 onward. It is a pattern we infer, not a framework he names."),
    dict(id="computer", title="The LLM as a new kind of computer",
         reading="Our reading: the analogy builds in steps, from 'differentiable computer' (2022) to 'LLM OS' (Sept 2023). This dates when he said it publicly, not when he first thought it."),
    dict(id="empower", title="Empowerment and its risks",
         reading="Our reading: excitement about open tools and individual reach sits beside warnings about attention-exploiting apps and concentration. Both are held at once."),
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
    dict(id="2024", title="An explicit educational design", range=["2024-01-01", "2024-12-31"], status="outline",
         coverage="0 of 203 X posts read yet. Talks and videos not yet reviewed.", summary="Eureka Labs is announced. The rest of the year is next in the reading queue.", interpretation=[]),
    dict(id="2025", title="Vibe coding, useful agents and their limits", range=["2025-01-01", "2025-12-31"], status="outline",
         coverage="A few posts and four blog posts read on their own. Full X read not started (158 posts).",
         summary="Vibe coding is named, limited to throwaway projects. Blog posts on note-taking, empowerment and the friction of delivery. A year review on uneven capability.", interpretation=[]),
    dict(id="2026", title="Changing coding practice (open period)", range=["2026-01-01", "2026-11-06"], status="outline",
         coverage="A few posts and one edited talk text read. Full X read not started (70 posts).",
         summary="Agents are a large net gain but still need close watching for code you care about.", interpretation=[]),
]


def main():
    posts = {}
    for line in ARCHIVE.open(encoding="utf-8"):
        d = json.loads(line)
        posts[d["id"]] = d
    events, errors = [], []
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
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    events.sort(key=lambda e: e["date"])
    data = dict(updated="2026-11-09", events=events, threads=THREADS, periods=PERIODS)
    OUT.write_text("// Generated by tools/build_site.py. Do not edit by hand.\nwindow.CHRONICLE = "
                   + json.dumps(data, ensure_ascii=False, indent=1) + ";\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(events)} events, all X quotes verbatim")


if __name__ == "__main__":
    main()

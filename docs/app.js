(function () {
  const D = window.CHRONICLE;
  const LENSES = [
    { id: "milestone", label: "Work and life" },
    { id: "fund", label: "AI fundamentals and limits" },
    { id: "agency", label: "Agency and empowerment" },
    { id: "coding", label: "Coding and thinking" },
    { id: "practice", label: "Engineering practice" },
  ];
  const LENS = Object.fromEntries(LENSES.map((l) => [l.id, l]));
  const KIND = { post: "X post", talk: "Talk / interview", writing: "Writing" };
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const color = (lens) => `var(--${lens})`;
  // ---- language: ?lang= in the URL, then the saved choice, then the browser language
  const ZHUI = {
    tag: "独立 · 非官方 · 持续更新中",
    h1: "Karpathy 思想编年史",
    intro: "外星造物、造梦机器、人的灵魂、幽灵。Andrej Karpathy 如何解释 AI，以及他的看法从 2022 到 2026 年如何变化。每条引文都链接到原文；我们的解读会明确标注。<br><small>他的原话保留英文原文；其余内容为中文翻译。</small>",
    proto: "原型",
    at_h: "他在谈论什么",
    at_lede: "每半年中，涉及各主题的 X 帖子所占比例（自 2022 年起）。按关键词自动统计，因此反映的是关注度，而不是观点。",
    th_h: "主线",
    th_lede: "五个随时间追踪的观点。每一步都是他的原话。每张卡片末尾的灰底部分是我们的解读，可以对照原话检验。",
    pe_h: "时期",
    pe_lede: "编年史按时期逐段撰写，基于对当年全部帖子的通读。2026 年尚未结束：目前覆盖到 11 月初的帖子。",
    me_h: "方法与局限",
    me1: "<b>来源。</b>他的 X 帖子、演讲、访谈和文章。每次构建前，X 引文都会与他的帖子存档逐字核对。演讲引文来自第三方或机器转写稿，并已注明。",
    me2: "<b>日期。</b>帖子日期为北京时间（UTC+8），因此可能比美国日期晚一天。",
    me3: "<b>并不完整。</b>回复、纯图片帖子和大部分长录音尚未阅读。没有收录不代表他从未说过。公开言论反映的是他何时表达了什么，而不是他何时私下想到的。",
    me4: "<b>非官方。</b>这是一位学习者的独立解读，与 Andrej Karpathy 本人无关，也未获其认可。欢迎指正。",
    upd: "更新于",
    src: "源码与方法见",
    theme: "切换主题",
    n_me2: "比喻",
    n_fi: "发现",
    mt_h: "他关于 AI 的比喻",
    mt_lede: "外星造物、造梦机器、人的灵魂、幽灵：这些是他用来解释 AI 的意象，按它们在他 2022 年以来帖子中出现的先后排列。并非每个都是他首创，但合在一起，就是他理解 AI 的方式。每张卡片都链接到他说这句话的出处。",
    n_track: "编程图表",
    fi_h: "我们的发现",
    fi_lede: "通读他自 2022 年以来的全部帖子后，归纳出的五个规律。标题是我们的解读；旁边附上他的原话，供你核对。",
    n_at: "话题",
    n_th: "主线",
    n_pe: "时期",
    n_me: "方法",
  };
  const qlang = new URLSearchParams(location.search).get("lang");
  let saved = null;
  try { saved = localStorage.getItem("lang"); } catch (_) {}
  const ZH = (qlang || saved || (navigator.language || "").toLowerCase()).startsWith("zh");
  const tr = (s) => (ZH && D.zh && D.zh[s]) || s;
  const LG = (en, zh) => (ZH ? zh : en);
  if (ZH) {
    document.documentElement.lang = "zh-CN";
    document.title = "Karpathy 思想编年史";
    document.querySelectorAll("[data-i18n]").forEach((el) => { const v = ZHUI[el.dataset.i18n]; if (v) el.innerHTML = v; });
  }
  document.querySelectorAll(".lang a").forEach((a) => {
    const on = (a.dataset.l === "zh") === ZH;
    a.setAttribute("aria-current", on ? "true" : "false");
    a.addEventListener("click", (ev) => {
      ev.preventDefault();
      if (on) return;
      try { localStorage.setItem("lang", a.dataset.l); } catch (_) {}
      const u = new URL(location.href); u.searchParams.set("lang", a.dataset.l); location.href = u.toString();
    });
  });
  const fmt = (d) => new Date(d + "T00:00:00").toLocaleDateString(ZH ? "zh-CN" : "en-GB", { day: "numeric", month: "short", year: "numeric" });


  // ---- stats
  const read = D.periods.filter((p) => p.status === "read").length;
  $("stats").innerHTML = [
    [D.events.length, LG("sourced moments", "条有出处的记录")],
    [`${D.posts_read} / ${D.posts_total}`, LG("X posts read since 2022", "2022 年以来已读的 X 帖子")],
    [LG(`${read} of ${D.periods.length}`, `${read} / ${D.periods.length}`), LG("periods written", "已写完的时期")],
  ].map(([b, s]) => `<div class="stat"><b>${b}</b><span>${s}</span></div>`).join("");
  $("updated").textContent = fmt(D.updated);

  // ---- metaphors: the headline gallery, grouped, in order of first appearance
  (function renderMetaphors() {
    const M = D.metaphors || [];
    if (!M.length) { $("metaphors").remove(); return; }
    const GC = { is: "--practice", computer: "--fund", work: "--coding" };
    $("mgroups").innerHTML = D.metaphor_groups.map((g) => {
      const items = M.filter((m) => m.group === g.id).sort((a, b) => a.date.localeCompare(b.date));
      return `<div class="mgroup" style="--g:var(${GC[g.id]})"><h3>${esc(tr(g.title))}</h3><div class="mgrid">${items.map((m) => `
        <a class="mcard" href="${esc(m.url)}" target="_blank" rel="noopener">
          <span class="yr">${m.date.slice(0, 4)}</span>
          <span class="ph" lang="en">“${esc(m.phrase)}”</span>
          <span class="gl">${esc(tr(m.gloss))}</span>
          <span class="src">${fmt(m.date)} · ${esc(tr(m.source))} ↗</span>
        </a>`).join("")}</div></div>`;
    }).join("");
  })();

  // ---- findings: our headline, his words beside it
  (function renderFindings() {
    const F = D.findings || [];
    if (!F.length) { $("findings").remove(); return; }
    $("finds").innerHTML = F.map((f, i) => `
      <article class="find" id="finding-${i + 1}"><div class="n"><a href="#finding-${i + 1}" style="text-decoration:none;color:inherit" title="Link to this finding">${i + 1}</a></div>
        <div><h3>${esc(tr(f.title))}</h3><p class="why">${esc(tr(f.why))}</p></div>
        <ul class="evl">${f.evidence.map((e) => `<li><div class="d">${fmt(e.date)} · ${esc(tr(e.source))}${e.note ? " · " + esc(tr(e.note)) : ""}</div>
          <div class="t"><a href="${esc(e.url)}" target="_blank" rel="noopener">“${esc(e.quote)}”</a></div></li>`).join("")}</ul>
      </article>`).join("");
  })();

  // ---- attention: what he talks about, counted by keyword per half-year
  (function renderAttention() {
    const A = D.attention;
    if (!A) { $("attention").remove(); return; }
    const LOW = 20; // half-years with fewer posts than this are faded
    const share = (th, i) => (A.totals[i] ? th.counts[i] / A.totals[i] : 0);
    const max = Math.max(...A.themes.flatMap((th) => th.counts.map((_, i) => (A.totals[i] >= LOW ? share(th, i) : 0))));
    const years = [...new Set(A.buckets.map((b) => b.slice(0, 4)))];
    let html = A.themes.map((th) => `
      <div class="at-row"><div class="at-lab">${esc(tr(th.label))}</div>
        <div class="at-bars">${th.counts.map((c, i) => {
          const h = Math.min(100, (share(th, i) / max) * 100);
          return `<button type="button" class="at-b${A.totals[i] < LOW ? " low" : ""}" data-t="${th.id}" data-i="${i}"
            aria-label="${esc(tr(th.label))}, ${A.buckets[i]}: ${c} / ${A.totals[i]}"><i style="height:${Math.max(h, c ? 4 : 0)}%"></i></button>`;
        }).join("")}</div></div>`).join("");
    const cols = `grid-template-columns:repeat(${A.buckets.length},1fr)`;
    html = html.replace(/class="at-bars"/g, `class="at-bars" style="${cols}"`);
    html += `<div class="at-row at-axis"><div></div><div class="at-bars" style="${cols}">${years.map((y) => {
      const n = A.buckets.filter((b) => b.startsWith(y)).length;
      return `<span style="grid-column:span ${n}">${y}${y === "2026" ? LG(" so far", " 至今") : ""}</span>`;
    }).join("")}</div></div>`;
    $("at").innerHTML = html;
    const idle = `<p class="nt">${LG("Taller bar = a larger share of his posts that half-year. Click a bar to see the posts behind it.", "柱子越高 = 该半年中相关帖子占比越大。点击柱子可查看对应的帖子。")}</p>`;
    $("atcard").innerHTML = idle;
    $("at").addEventListener("click", (ev) => {
      const b = ev.target.closest(".at-b");
      if (!b) return;
      $("at").querySelectorAll(".at-b").forEach((x) => x.classList.toggle("sel", x === b));
      const th = A.themes.find((x) => x.id === b.dataset.t), i = +b.dataset.i;
      const ps = th.posts[i];
      const pct = Math.round((th.counts[i] / A.totals[i]) * 100);
      $("atcard").innerHTML = `<div class="m"><b>${esc(tr(th.label))}</b> · ${A.buckets[i]} · ${LG(`${th.counts[i]} of ${A.totals[i]} posts`, `${A.totals[i]} 条中的 ${th.counts[i]} 条`)} (${pct}%)${A.totals[i] < LOW ? LG(" · few posts this half-year, so the share is unreliable", " · 该半年帖子较少，比例不可靠") : ""}</div>
        <ul class="at-list">${ps.map((p) => `<li><a href="${esc(p.url)}" target="_blank" rel="noopener">${fmt(p.date)}</a>${p.quote ? ` <span>“${esc(p.quote)}”</span>` : ""}</li>`).join("") || `<li>${LG("No posts.", "没有帖子。")}</li>`}</ul>`;
    });
  })();

  // ---- belief track (prototype): one chart, words on demand
  (function renderTrack() {
    const T = (D.tracks || [])[0];
    if (!T) { $("track").remove(); return; }
    const COL = { care: "var(--coding)", throwaway: "var(--practice)" };
    const SHORT = ZH ? ["自己写", "逐行审阅", "监督智能体", "不看代码"] : ["Writes it himself", "Reviews every change", "Supervises agents", "Doesn't read it"];
    const TINY = ZH ? ["自己写", "审阅", "监督", "不看"] : ["Himself", "Reviews", "Supervises", "Unread"];
    const month = (d) => new Date(d + "T00:00:00").toLocaleDateString(ZH ? "zh-CN" : "en-GB", { month: "short", year: "numeric" });
    const S = T.stations;
    const pts = S.filter((s) => s.kind === "practice" || s.kind === "feeling" || s.n === 3);
    $("track-q").textContent = tr(T.question);
    $("track-lede").textContent = ZH ? "2023 年他预测，人对代码的监督会淡化到几乎没有。对他在乎的代码，他自己的做法直到 2025 年 12 月都停留在低位，随后陡升：到 2026 年 3 月他已不再手写代码，但仍说不要放手不看生产代码。将鼠标悬停或点击某个点，可阅读他的原话。" : "In 2023 he forecast that human oversight of code would fade to almost nothing. For code he cares about, his own practice stayed low until December 2025, then jumped: by March 2026 he typed no code, but still says not to stop looking at production code. Hover or tap a point to read his words.";
    const idle = `<p class="nt">${LG("Hover or tap a point on the chart to read what he said and when.", "将鼠标悬停或点击图中的点，查看他何时说了什么。")}</p>`;
    $("tcard").innerHTML = idle;

    let sel = null;
    function card(n) {
      const s = S.find((x) => x.n === +n);
      const c = s.kind === "practice" ? COL[s.lane] : "var(--muted)";
      const what = s.kind === "forecast" ? LG("Forecast (a prediction, not his own practice)", "预测（对未来的判断，不是他自己的做法）")
        : s.kind === "feeling" ? LG("A feeling, not yet a new way of working", "一种感受，还不是新的工作方式")
        : `${tr(T.levels[s.level - 1])}${s.lane === "throwaway" ? LG(" · throwaway project", " · 一次性项目") : LG(" · code he cares about", " · 他在乎的代码")}`;
      $("tcard").style.setProperty("--c", c);
      $("tcard").innerHTML = `<div class="m">${month(s.date)} · <b>${esc(what)}</b></div>
        <p class="qq">“${esc(s.quote)}”</p>
        <p class="nt">${esc(tr(s.note))} <a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(tr(s.source))} ↗</a>
        ${s.status === "spot" ? " · 2026 not fully read yet" : ""}</p>`;
    }

    function draw() {
      const box = $("trk");
      const W = Math.max(300, box.clientWidth - 16);
      const narrow = W < 640;
      const H = narrow ? 290 : 360, L = narrow ? 70 : 156, R = narrow ? 12 : 28, TOP = 44, BOT = 34;
      const Y = (k) => TOP + ((4 - k) * (H - TOP - BOT)) / 3;
      const a = Date.parse("2022-09-01"), b = Date.parse("2026-12-01");
      const X = (d) => L + ((Date.parse(d) - a) / (b - a)) * (W - L - R);
      const lab = narrow ? TINY : SHORT;
      let g = "";
      // rows and years
      for (let k = 1; k <= 4; k++) {
        g += `<line class="grid" x1="${L}" x2="${W - R}" y1="${Y(k)}" y2="${Y(k)}"/>`;
        g += `<text class="ax" x="${L - 12}" y="${Y(k) + 4}" text-anchor="end">${lab[k - 1]}</text>`;
      }
      g += `<text class="ax" x="${narrow ? 4 : L - 12}" y="${TOP - 26}" text-anchor="${narrow ? "start" : "end"}" font-weight="600">${LG("More to AI ↑", "交给 AI 更多 ↑")}</text>`;
      for (let y = 2023; y <= 2026; y++) {
        const xx = X(y + "-01-01");
        g += `<line class="grid" x1="${xx}" x2="${xx}" y1="${TOP - 8}" y2="${H - BOT + 6}" stroke-dasharray="2 5"/>`;
        g += `<text class="ax" x="${xx}" y="${H - 10}" text-anchor="middle">${y}</text>`;
      }

      // his practice: step line + soft area, per lane
      const lane = (ln) => S.filter((s) => s.kind === "practice" && s.lane === ln);
      const care = lane("care"), thr = lane("throwaway"), end = W - R;
      let d = `M${X(care[0].date)},${Y(care[0].level)}`;
      for (let i = 1; i < care.length; i++) d += ` H${X(care[i].date)} V${Y(care[i].level)}`;
      d += ` H${end}`;
      const base = Y(1) + 0.5;
      g += `<path d="${d} V${base} H${X(care[0].date)} Z" fill="var(--coding)" opacity=".08"/>`;
      g += `<path d="${d}" fill="none" stroke="var(--coding)" stroke-width="3" stroke-linejoin="round"/>`;
      const ty = Y(thr[0].level);
      g += `<path d="M${X(thr[0].date)},${ty} H${end}" fill="none" stroke="var(--practice)" stroke-width="3" stroke-dasharray="7 5"/>`;

      // the 2023 forecast: an arrow up, no timing implied
      const f = S.find((s) => s.n === 3), fx = X(f.date);
      g += `<defs><marker id="ah" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="var(--muted)"/></marker></defs>`;
      g += `<line x1="${fx}" y1="${Y(2) - 10}" x2="${fx}" y2="${Y(4) + 4}" stroke="var(--muted)" stroke-width="2" stroke-dasharray="4 4" marker-end="url(#ah)"/>`;

      // the December 2025 turn
      const fe = S.find((s) => s.kind === "feeling"), fex = X(fe.date);
      g += `<line x1="${fex}" y1="${TOP - 8}" x2="${fex}" y2="${H - BOT + 6}" stroke="var(--ink)" stroke-dasharray="3 4" opacity=".45"/>`;

      // a few direct labels (desktop only); phone relies on the card
      if (!narrow) {
        const c0 = care[0];
        g += `<text class="cl q" x="${X(c0.date) + 12}" y="${Y(2) - 14}">“I prompt. &amp; edit.”</text>`;
        g += `<text class="cl" x="${X("2023-06-01")}" y="${Y(2) + 22}" style="fill:var(--coding)">${LG("code he cares about", "他在乎的代码")}</text>`;
        g += `<text class="cl" x="${fx}" y="${Y(4) - 14}" text-anchor="middle" style="fill:var(--muted)">${LG("2023 forecast", "2023 年预测")}: “~pass-through”</text>`;
        g += `<text class="cl" x="${X(thr[0].date) - 14}" y="${ty + 5}" text-anchor="end" style="fill:var(--practice)">${LG("throwaway projects (vibe coding)", "一次性项目（氛围编程）")}</text>`;
        const tab = care.find((s) => s.level === 1);
        g += `<text class="cl q" x="${X(tab.date) - 12}" y="${Y(1) - 12}" text-anchor="end">“tab complete”</text>`;
        g += `<text class="cl" x="${fex - 8}" y="${TOP - 18}" text-anchor="end">“never felt this much behind”</text>`;
        const a80 = care.find((s) => s.quote.startsWith("80%"));
        g += `<text class="cl q" x="${X(a80.date) - 14}" y="${Y(a80.level) - 14}" text-anchor="end">“80% agent coding”</text>`;
      }

      // points (with a larger invisible hit area)
      pts.forEach((s) => {
        const cx = X(s.date);
        const cy = s.kind === "feeling" ? TOP - 8 : s.n === 3 ? Y(2) - 10 : Y(s.level);
        const c = s.kind === "practice" ? COL[s.lane] : s.kind === "feeling" ? "var(--ink)" : "var(--muted)";
        const hollow = s.status === "spot" || s.kind !== "practice";
        g += `<g class="pt${sel === s.n ? " sel" : ""}" data-n="${s.n}" tabindex="0" role="button" aria-label="${month(s.date)}: ${esc(s.quote)}">
          <circle cx="${cx}" cy="${cy}" r="18" fill="transparent"/>
          <circle class="v" cx="${cx}" cy="${cy}" r="6.5" fill="${hollow ? "var(--surface)" : c}" stroke="${c}" stroke-width="2.5"/></g>`;
      });
      box.innerHTML = `<svg viewBox="0 0 ${W} ${H}" height="${H}" role="img" aria-label="${esc(tr(T.question))}">${g}</svg>`;
    }

    const pick = (ev) => {
      const p = ev.target.closest(".pt");
      if (!p) return;
      if (ev.type === "keydown" && ev.key !== "Enter" && ev.key !== " ") return;
      if (ev.type !== "mouseover") { ev.preventDefault(); sel = +p.dataset.n; $("trk").querySelectorAll(".pt").forEach((e) => e.classList.toggle("sel", +e.dataset.n === sel)); }
      card(p.dataset.n);
    };
    ["mouseover", "click", "keydown"].forEach((t) => $("trk").addEventListener(t, pick));
    $("trk").addEventListener("mouseleave", () => { if (sel) card(sel); else $("tcard").innerHTML = idle; });
    draw();
    let rt; window.addEventListener("resize", () => { clearTimeout(rt); rt = setTimeout(draw, 120); });
  })();

  // ---- threads
  $("threadcards").innerHTML = D.threads.map((t) => {
    const evs = D.events.filter((e) => e.threads.includes(t.id));
    const isKey = (e) => (t.key || []).some((k) => e.url.includes(k));
    const step = (e) => `
      <li class="${e.status === "spot" ? "spot" : ""}" style="--c:${color(e.lens)}">
        <div class="d">${fmt(e.date)}${e.title ? " · " + esc(tr(e.title)) : ""}</div>
        <div class="t"><a href="${esc(e.url)}" target="_blank" rel="noopener">${(() => { const q = e.quotes[(e.tq || {})[t.id] || 0]; return esc(q ? "“" + q + "”" : tr(e.note)); })()}</a></div>
      </li>`;
    const keys = evs.filter(isKey);
    const TC = { ghost: "--milestone", oversight: "--coding", verify: "--fund", computer: "--practice", empower: "--agency" };
    return `<article class="card" style="--tc:var(${TC[t.id] || "--fund"})"><h3>${esc(tr(t.title))}</h3><ol class="steps">${keys.map(step).join("")}</ol>
      <div class="ours"><b>${LG("Our reading", "我们的解读")}</b>${esc(tr(t.reading))}</div>
      <details class="chap"><summary>${LG(`All ${evs.length} statements`, `全部 ${evs.length} 条原话`)}</summary><ol class="steps">${evs.map(step).join("")}</ol></details></article>`;
  }).join("");

  // ---- periods
  $("periodlist").innerHTML = D.periods.map((p) => `
    <article class="card period" id="p${p.id}">
      <div><div class="yr">${p.id}</div><span class="badge ${p.status}">${p.status === "read" ? LG("Fully read", "已通读") : LG("Outline", "提纲")}</span></div>
      <div>
        <h3>${esc(tr(p.title))}</h3>
        <p class="cov">${esc(tr(p.coverage))}</p>
        <p>${esc(tr(p.summary))}</p>
        ${p.interpretation.length ? `<div class="ours"><b>${LG("Our reading", "我们的解读")}</b><ul>${p.interpretation.map((s) => `<li>${esc(tr(s))}</li>`).join("")}</ul></div>` : ""}
        ${p.chapter_html ? `<details class="chap"><summary>${p.status === "read" ? LG(`Read the full ${p.id} chapter`, `阅读 ${p.id} 年完整章节（英文）`) : LG(`Read the current ${p.id} outline`, `阅读 ${p.id} 年提纲（英文）`)}</summary>
          ${ZH ? `<p class="zhnote">完整章节目前只有英文版。</p>` : ""}
          <div class="prose" lang="en">${p.chapter_html}</div>
          ${p.chapter ? `<p class="chapter"><a href="${esc(p.chapter)}" target="_blank" rel="noopener">${LG("Also on GitHub ↗", "在 GitHub 上查看 ↗")}</a></p>` : ""}
        </details>` : ""}
      </div>
    </article>`).join("");

  // ---- deep links (e.g. #p2025) target cards built above, after the browser's own jump
  if (location.hash.length > 1) {
    const t = document.getElementById(decodeURIComponent(location.hash.slice(1)));
    if (t) requestAnimationFrame(() => t.scrollIntoView());
  }

  // ---- nav: highlight the section in view
  if ("IntersectionObserver" in window) {
    const links = [...document.querySelectorAll(".nav .in > a")];
    const io = new IntersectionObserver((ents) => ents.forEach((en) => {
      if (en.isIntersecting) links.forEach((a) => a.classList.toggle("on", a.getAttribute("href") === "#" + en.target.id));
    }), { rootMargin: "-45% 0px -50% 0px" });
    ["metaphors", "findings", "track", "attention", "threads", "periods", "method"].forEach((id) => { const el = $(id); if (el) io.observe(el); });
    const yrs = [...document.querySelectorAll(".nav .yrs a")];
    const yo = new IntersectionObserver((ents) => ents.forEach((en) => {
      if (en.isIntersecting) yrs.forEach((a) => a.classList.toggle("on", a.getAttribute("href") === "#" + en.target.id));
    }), { rootMargin: "-40% 0px -55% 0px" });
    document.querySelectorAll(".period").forEach((el) => yo.observe(el));
    new IntersectionObserver((ents) => ents.forEach((en) => { if (!en.isIntersecting) yrs.forEach((a) => a.classList.remove("on")); }))
      .observe($("periods"));
  }

  // ---- theme toggle
  const root = document.documentElement;
  try { const t = localStorage.getItem("theme"); if (t) root.dataset.theme = t; } catch (_) {}
  $("themebtn").addEventListener("click", () => {
    const dark = root.dataset.theme ? root.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
    root.dataset.theme = dark ? "light" : "dark";
    try { localStorage.setItem("theme", root.dataset.theme); } catch (_) {}
  });
})();

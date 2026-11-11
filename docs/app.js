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
  const fmt = (d) => new Date(d + "T00:00:00").toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" });


  // ---- stats
  const read = D.periods.filter((p) => p.status === "read").length;
  $("stats").innerHTML = [
    [D.events.length, "sourced moments"],
    [`${D.posts_read} / ${D.posts_total}`, "X posts read since 2022"],
    [`${read} of ${D.periods.length}`, "periods written"],
  ].map(([b, s]) => `<div class="stat"><b>${b}</b><span>${s}</span></div>`).join("");
  $("updated").textContent = fmt(D.updated);

  // ---- attention: what he talks about, counted by keyword per half-year
  (function renderAttention() {
    const A = D.attention;
    if (!A) { $("attention").remove(); return; }
    const LOW = 20; // half-years with fewer posts than this are faded
    const share = (th, i) => (A.totals[i] ? th.counts[i] / A.totals[i] : 0);
    const max = Math.max(...A.themes.flatMap((th) => th.counts.map((_, i) => (A.totals[i] >= LOW ? share(th, i) : 0))));
    const years = [...new Set(A.buckets.map((b) => b.slice(0, 4)))];
    let html = A.themes.map((th) => `
      <div class="at-row"><div class="at-lab">${esc(th.label)}</div>
        <div class="at-bars">${th.counts.map((c, i) => {
          const h = Math.min(100, (share(th, i) / max) * 100);
          return `<button type="button" class="at-b${A.totals[i] < LOW ? " low" : ""}" data-t="${th.id}" data-i="${i}"
            aria-label="${esc(th.label)}, ${A.buckets[i]}: ${c} of ${A.totals[i]} posts"><i style="height:${Math.max(h, c ? 4 : 0)}%"></i></button>`;
        }).join("")}</div></div>`).join("");
    const cols = `grid-template-columns:repeat(${A.buckets.length},1fr)`;
    html = html.replace(/class="at-bars"/g, `class="at-bars" style="${cols}"`);
    html += `<div class="at-row at-axis"><div></div><div class="at-bars" style="${cols}">${years.map((y) => {
      const n = A.buckets.filter((b) => b.startsWith(y)).length;
      return `<span style="grid-column:span ${n}">${y}${y === "2026" ? " so far" : ""}</span>`;
    }).join("")}</div></div>`;
    $("at").innerHTML = html;
    const idle = `<p class="nt">Taller bar = a larger share of his posts that half-year. Click a bar to see the posts behind it.</p>`;
    $("atcard").innerHTML = idle;
    $("at").addEventListener("click", (ev) => {
      const b = ev.target.closest(".at-b");
      if (!b) return;
      $("at").querySelectorAll(".at-b").forEach((x) => x.classList.toggle("sel", x === b));
      const th = A.themes.find((x) => x.id === b.dataset.t), i = +b.dataset.i;
      const ps = th.posts[i];
      const pct = Math.round((th.counts[i] / A.totals[i]) * 100);
      $("atcard").innerHTML = `<div class="m"><b>${esc(th.label)}</b> · ${A.buckets[i]} · ${th.counts[i]} of ${A.totals[i]} posts (${pct}%)${A.totals[i] < LOW ? " · few posts this half-year, so the share is unreliable" : ""}</div>
        <ul class="at-list">${ps.map((p) => `<li><a href="${esc(p.url)}" target="_blank" rel="noopener">${fmt(p.date)}</a>${p.quote ? ` <span>“${esc(p.quote)}”</span>` : ""}</li>`).join("") || "<li>No posts.</li>"}</ul>`;
    });
  })();

  // ---- belief track (prototype): one chart, words on demand
  (function renderTrack() {
    const T = (D.tracks || [])[0];
    if (!T) { $("track").remove(); return; }
    const COL = { care: "var(--coding)", throwaway: "var(--practice)" };
    const SHORT = ["Writes it himself", "Reviews every change", "Supervises agents", "Doesn't read it"];
    const TINY = ["Himself", "Reviews", "Supervises", "Unread"];
    const month = (d) => new Date(d + "T00:00:00").toLocaleDateString("en-GB", { month: "short", year: "numeric" });
    const S = T.stations;
    const pts = S.filter((s) => s.kind === "practice" || s.kind === "feeling" || s.n === 3);
    $("track-q").textContent = T.question;
    $("track-lede").textContent = "In 2023 he forecast that human oversight of code would fade to almost nothing. For code he cares about, his own practice stayed low until December 2025. Hover or tap a point to read his words.";
    const idle = `<p class="nt">Hover or tap a point on the chart to read what he said and when.</p>`;
    $("tcard").innerHTML = idle;

    let sel = null;
    function card(n) {
      const s = S.find((x) => x.n === +n);
      const c = s.kind === "practice" ? COL[s.lane] : "var(--muted)";
      const what = s.kind === "forecast" ? "Forecast (a prediction, not his own practice)"
        : s.kind === "feeling" ? "A feeling, not yet a new way of working"
        : `${T.levels[s.level - 1]}${s.lane === "throwaway" ? " · throwaway project" : " · code he cares about"}`;
      $("tcard").style.setProperty("--c", c);
      $("tcard").innerHTML = `<div class="m">${month(s.date)} · <b>${esc(what)}</b></div>
        <p class="qq">“${esc(s.quote)}”</p>
        <p class="nt">${esc(s.note)} <a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.source)} ↗</a>
        ${s.status === "spot" ? " · 2026 not fully read yet" : ""}</p>`;
    }

    function draw() {
      const box = $("trk");
      const W = Math.max(300, box.clientWidth - 16);
      const narrow = W < 640;
      const H = narrow ? 290 : 360, L = narrow ? 70 : 156, R = narrow ? 12 : 28, TOP = 44, BOT = 34;
      const Y = (k) => TOP + ((4 - k) * (H - TOP - BOT)) / 3;
      const a = Date.parse("2022-09-01"), b = Date.parse("2026-03-15");
      const X = (d) => L + ((Date.parse(d) - a) / (b - a)) * (W - L - R);
      const lab = narrow ? TINY : SHORT;
      let g = "";
      // rows and years
      for (let k = 1; k <= 4; k++) {
        g += `<line class="grid" x1="${L}" x2="${W - R}" y1="${Y(k)}" y2="${Y(k)}"/>`;
        g += `<text class="ax" x="${L - 12}" y="${Y(k) + 4}" text-anchor="end">${lab[k - 1]}</text>`;
      }
      g += `<text class="ax" x="${L - 12}" y="${TOP - 26}" text-anchor="end" font-weight="600">More to AI ↑</text>`;
      for (let y = 2023; y <= 2026; y++) {
        const xx = X(y + "-01-01");
        g += `<line class="grid" x1="${xx}" x2="${xx}" y1="${TOP - 8}" y2="${H - BOT + 6}" stroke-dasharray="2 5"/>`;
        g += `<text class="ax" x="${xx}" y="${H - 10}" text-anchor="middle">${y}</text>`;
      }
      const x26 = X("2026-01-01");
      g += `<rect x="${x26}" y="${TOP - 8}" width="${W - R - x26}" height="${H - BOT - TOP + 14}" fill="var(--hatch)" opacity=".7"/>`;

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
        g += `<text class="cl" x="${X("2023-06-01")}" y="${Y(2) + 22}" style="fill:var(--coding)">code he cares about</text>`;
        g += `<text class="cl" x="${fx}" y="${Y(4) - 14}" text-anchor="middle" style="fill:var(--muted)">2023 forecast: “~pass-through”</text>`;
        g += `<text class="cl" x="${X(thr[0].date) - 14}" y="${ty + 5}" text-anchor="end" style="fill:var(--practice)">throwaway projects (vibe coding)</text>`;
        const tab = care.find((s) => s.level === 1);
        g += `<text class="cl q" x="${X(tab.date) - 12}" y="${Y(1) - 12}" text-anchor="end">“tab complete”</text>`;
        g += `<text class="cl" x="${fex - 8}" y="${TOP - 18}" text-anchor="end">“never felt this much behind”</text>`;
        const last = care[care.length - 1];
        g += `<text class="cl q" x="${X(last.date) - 14}" y="${Y(last.level) - 14}" text-anchor="end">“80% agent coding”</text>`;
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
      box.innerHTML = `<svg viewBox="0 0 ${W} ${H}" height="${H}" role="img" aria-label="${esc(T.question)}">${g}</svg>`;
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
    return `<article class="card"><h3>${esc(t.title)}</h3><ol class="steps">${evs.map((e) => `
      <li class="${e.status === "spot" ? "spot" : ""}" style="--c:${color(e.lens)}">
        <div class="d">${fmt(e.date)}${e.title ? " · " + esc(e.title) : ""}</div>
        <div class="t"><a href="${esc(e.url)}" target="_blank" rel="noopener">${esc(e.quotes[0] ? "“" + e.quotes[0] + "”" : e.note)}</a></div>
      </li>`).join("")}</ol>
      <div class="ours"><b>Our reading</b>${esc(t.reading.replace(/^Our reading:\s*(.)/, (_, c) => c.toUpperCase()))}</div></article>`;
  }).join("");

  // ---- periods
  $("periodlist").innerHTML = D.periods.map((p) => `
    <article class="card period">
      <div><div class="yr">${p.id}</div><span class="badge ${p.status}">${p.status === "read" ? "Fully read" : "Outline"}</span></div>
      <div>
        <h3>${esc(p.title)}</h3>
        <p class="cov">${esc(p.coverage)}</p>
        <p>${esc(p.summary)}</p>
        ${p.interpretation.length ? `<div class="ours"><b>Our reading</b><ul>${p.interpretation.map((s) => `<li>${esc(s)}</li>`).join("")}</ul></div>` : ""}
        ${p.chapter_html ? `<details class="chap"><summary>${p.status === "read" ? `Read the full ${p.id} chapter` : `Read the current ${p.id} outline`}</summary>
          <div class="prose">${p.chapter_html}</div>
          ${p.chapter ? `<p class="chapter"><a href="${esc(p.chapter)}" target="_blank" rel="noopener">Also on GitHub ↗</a></p>` : ""}
        </details>` : ""}
      </div>
    </article>`).join("");

  // ---- theme toggle
  const root = document.documentElement;
  try { const t = localStorage.getItem("theme"); if (t) root.dataset.theme = t; } catch (_) {}
  $("themebtn").addEventListener("click", () => {
    const dark = root.dataset.theme ? root.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
    root.dataset.theme = dark ? "light" : "dark";
    try { localStorage.setItem("theme", root.dataset.theme); } catch (_) {}
  });
})();

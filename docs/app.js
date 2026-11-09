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

  D.events.forEach((e, i) => (e.i = i));
  let thread = null;
  let selected = null;

  // ---- stats
  const read = D.periods.filter((p) => p.status === "read").length;
  $("stats").innerHTML = [
    [D.events.length, "sourced moments"],
    [`${D.posts_read} / ${D.posts_total}`, "X posts read since 2022"],
    [`${read} of ${D.periods.length}`, "periods written"],
  ].map(([b, s]) => `<div class="stat"><b>${b}</b><span>${s}</span></div>`).join("");
  $("updated").textContent = fmt(D.updated);

  // ---- time scale: a narrow "before 2022" stub, then 2022-01-01 .. 2027-01-01
  const PRE = 4; // percent
  const t0 = Date.parse("2022-01-01"), t1 = Date.parse("2027-01-01");
  const x = (d) => {
    const t = Date.parse(d);
    if (t < t0) return PRE / 2;
    return PRE + ((t - t0) / (t1 - t0)) * (100 - PRE);
  };

  // ---- chips
  const chips = [{ id: null, title: "All" }, ...D.threads];
  $("chips").innerHTML = chips.map((t) =>
    `<button class="chip" type="button" data-t="${t.id || ""}" aria-pressed="${t.id === thread}">${esc(t.title)}</button>`).join("");
  $("chips").addEventListener("click", (ev) => {
    const b = ev.target.closest(".chip");
    if (!b) return;
    thread = b.dataset.t || null;
    [...$("chips").children].forEach((c) => c.setAttribute("aria-pressed", String((c.dataset.t || null) === thread)));
    applyFilter();
  });

  // ---- lanes
  const ROWH = 17, PAD = 14;
  const tl = $("tl");
  LENSES.forEach((lens) => {
    const evs = D.events.filter((e) => e.lens === lens.id);
    // stack nearby dots into sub-rows
    const rows = [];
    evs.forEach((e) => {
      const px = x(e.date);
      let r = rows.findIndex((last) => px - last > 1.6);
      if (r === -1) { rows.push(px); r = rows.length - 1; } else rows[r] = px;
      e.px = px; e.row = r;
    });
    const n = Math.max(rows.length, 1);
    const h = PAD * 2 + (n - 1) * ROWH;
    const row = document.createElement("div");
    row.className = "tl-row";
    row.innerHTML = `<div class="tl-label"><i style="background:${color(lens.id)}"></i>${lens.label}</div>`;
    const track = document.createElement("div");
    track.className = "tl-track";
    track.style.height = h + "px";
    let bands = `<div class="band pre" style="left:0;width:${PRE}%"></div>`;
    D.periods.filter((p) => p.status !== "read").forEach((p) => {
      const a = x(p.range[0]), b = x(p.range[1]);
      bands += `<div class="band outline" style="left:${a}%;width:${b - a}%"></div>`;
    });
    for (let y = 2022; y <= 2026; y++) bands += `<div class="yearline" style="left:${x(y + "-01-01")}%"></div>`;
    track.innerHTML = bands;
    evs.forEach((e) => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "ev" + (e.status === "spot" ? " spot" : "");
      b.style.setProperty("--c", color(e.lens));
      b.style.left = e.px + "%";
      b.style.top = PAD + e.row * ROWH + "px";
      b.dataset.i = e.i;
      b.setAttribute("aria-label", `${fmt(e.date)}: ${e.quotes[0] || e.title || e.note}`);
      track.appendChild(b);
      e.el = b;
    });
    row.appendChild(track);
    tl.appendChild(row);
  });
  // axis
  let ax = `<span style="left:${PRE / 2}%">2019</span>`;
  for (let y = 2022; y <= 2026; y++) ax += `<span style="left:${(x(y + "-01-01") + x(y + 1 + "-01-01")) / 2}%">${y}</span>`;
  const axis = document.createElement("div");
  axis.className = "axis";
  axis.innerHTML = `<div></div><div class="axis-track">${ax}</div>`;
  tl.appendChild(axis);

  // tooltip + select
  const tip = $("tip");
  tl.addEventListener("mouseover", (ev) => {
    const b = ev.target.closest(".ev");
    if (!b) return;
    const e = D.events[b.dataset.i];
    tip.innerHTML = `<small>${fmt(e.date)} · ${KIND[e.kind]}</small>${esc(e.quotes[0] ? "“" + e.quotes[0] + "”" : e.title || e.note)}`;
    const r = b.getBoundingClientRect(), R = tl.getBoundingClientRect();
    let left = r.left - R.left + 12;
    tip.style.opacity = 1;
    if (left + 300 > R.width) left = Math.max(8, r.left - R.left - tip.offsetWidth - 4);
    tip.style.left = left + "px";
    tip.style.top = r.top - R.top + 14 + "px";
  });
  tl.addEventListener("mouseout", (ev) => { if (ev.target.closest(".ev")) tip.style.opacity = 0; });
  tl.addEventListener("click", (ev) => {
    const b = ev.target.closest(".ev");
    if (b) select(+b.dataset.i);
  });

  function sourceLabel(e) {
    if (e.kind === "post") return "Open the post on X";
    if (e.kind === "talk") return "Open the recording or text";
    return "Read the original";
  }

  function select(i) {
    if (selected !== null) D.events[selected].el.classList.remove("sel");
    selected = i;
    const e = D.events[i];
    e.el.classList.add("sel");
    const lens = LENS[e.lens];
    const threads = e.threads.map((t) => D.threads.find((x) => x.id === t)).filter(Boolean).map((t) => t.title);
    $("detail").innerHTML = `
      <div class="meta">
        <span>${fmt(e.date)}</span>
        <span class="pill"><i style="background:${color(e.lens)}"></i>${lens.label}</span>
        <span>${KIND[e.kind]}${e.title ? ": " + esc(e.title) : ""}</span>
        ${threads.length ? `<span>Thread: ${esc(threads.join(", "))}</span>` : ""}
      </div>
      ${e.quotes.map((q) => `<p class="q">${esc(q)}</p>`).join("")}
      <p class="ctx">${e.quotes.length ? "Context, in our words: " : ""}${esc(e.note)}</p>
      ${e.status === "spot" ? `<p class="warn">Read on its own. The rest of this period has not been read yet, so the surrounding context may change.</p>` : ""}
      <a href="${esc(e.url)}" target="_blank" rel="noopener">${sourceLabel(e)} ↗</a>`;
  }

  // ---- list view (narrow screens)
  function renderList() {
    const evs = D.events.filter((e) => !thread || e.threads.includes(thread));
    let html = "", year = null;
    evs.forEach((e) => {
      const y = e.date.slice(0, 4) < "2022" ? "Before 2022" : e.date.slice(0, 4);
      if (y !== year) { html += `<h3>${y}</h3>`; year = y; }
      html += `<div class="li"><span class="ev${e.status === "spot" ? " spot" : ""}" style="--c:${color(e.lens)}"></span><div>
        <div class="li-date">${fmt(e.date)} · ${LENS[e.lens].label}</div>
        <div class="li-q">${esc(e.quotes[0] ? "“" + e.quotes[0] + "”" : e.title || e.note)}</div>
        <div class="li-date">${e.quotes[0] ? esc(e.note) + " " : ""}<a href="${esc(e.url)}" target="_blank" rel="noopener">Source ↗</a></div>
      </div></div>`;
    });
    $("list").innerHTML = html;
  }

  function applyFilter() {
    D.events.forEach((e) => e.el.classList.toggle("dim", !!thread && !e.threads.includes(thread)));
    renderList();
  }
  applyFilter();

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

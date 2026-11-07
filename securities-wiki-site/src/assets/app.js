const state = {
  categories: [],
  pages: [],
  pageById: new Map(),
  searchResults: [],
};

const $ = (selector) => document.querySelector(selector);
const escapeHtml = (value) => String(value).replace(/[&<>"']/g, (character) => ({
  "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
})[character]);

function routeId() {
  return decodeURIComponent(window.location.hash.slice(2).split("?")[0]);
}

function normalize(value) {
  return value.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/đ/g, "d").replace(/Đ/g, "D").toLowerCase();
}

function pageLink(page) {
  return `#/${page.id}`;
}

function renderNavigation(activeId = "") {
  $("#nav").innerHTML = state.categories.map((category, index) => {
    const active = category.pages.some((page) => page.path.slice(0, -3) === activeId);
    const items = category.pages.map((page) => {
      const id = page.path.slice(0, -3);
      return `<a class="nav-page ${id === activeId ? "active" : ""}" href="#/${id}" ${id === activeId ? 'aria-current="page"' : ""}>${escapeHtml(page.title)}</a>`;
    }).join("");
    return `<details class="nav-group" ${active || (!activeId && index === 0) ? "open" : ""}><summary><span class="nav-index">${String(index).padStart(2, "0")}</span><span>${escapeHtml(category.title)}</span><span class="nav-count">${category.pages.length}</span></summary><div class="nav-pages">${items}</div></details>`;
  }).join("");
}

function renderHome() {
  const featured = ["01-market-foundations", "03-trading-and-matching", "05-connectivity", "08-risk-and-compliance", "09-solution-architecture", "11-leadership-and-governance"];
  const cards = featured.map((id) => {
    const category = state.categories.find((item) => item.category === id);
    if (!category) return "";
    const index = state.categories.indexOf(category) + 1;
    const first = category.pages[0];
    return `<a class="topic-card" href="#/${first.path.slice(0, -3)}"><div class="topic-top"><span>${String(index).padStart(2, "0")}</span><span class="topic-arrow">↗</span></div><h3>${escapeHtml(category.title)}</h3><p>${category.pages.length} bài học</p></a>`;
  }).join("");
  $("#main").innerHTML = `<div class="home-container">
    <div class="eyebrow"><span class="eyebrow-line"></span> WIKI ĐÀO TẠO · THỊ TRƯỜNG VIỆT NAM</div>
    <section class="hero"><div class="hero-copy"><h1>Hiểu thị trường.<br><em>Thiết kế hệ thống.</em></h1><p>Từ nguyên lý khớp lệnh đến vận hành công ty chứng khoán — một nền tảng kiến thức chung cho architect và lãnh đạo nghiệp vụ.</p><a class="primary-cta" href="#/${state.pages[0].id}">Bắt đầu lộ trình <span>↗</span></a></div><div class="hero-graphic" aria-hidden="true"><div class="orbit orbit-one"></div><div class="orbit orbit-two"></div><div class="orbit orbit-three"></div><div class="hero-monogram">S<span>.</span></div><div class="graphic-label">MARKET <span>/</span> SYSTEMS</div></div></section>
    <div class="metrics"><div><strong>${state.pages.length}</strong><span>BÀI HỌC</span></div><div><strong>${state.categories.length}</strong><span>CHUYÊN MỤC</span></div><div><strong>02</strong><span>GÓC NHÌN: NGHIỆP VỤ & KIẾN TRÚC</span></div></div>
    <section class="home-section"><div class="section-heading"><div><span class="overline">EXPLORE THE KNOWLEDGE BASE</span><h2>Khám phá theo chủ đề</h2></div><span class="section-note">Chọn một chủ đề để bắt đầu →</span></div><div class="topics">${cards}</div></section>
    <section class="learning-banner"><div><span class="overline">LỘ TRÌNH ĐỀ XUẤT</span><h2>Học có hệ thống, áp dụng vào thực tế.</h2><p>8 tuần từ thị trường, lệnh và bảng giá đến kiến trúc, kiểm soát rủi ro và tình huống vận hành.</p></div><a href="#/${state.pages[0].id}">Xem lộ trình <span>→</span></a></section>
    <footer class="home-footer">Nội dung đào tạo tham chiếu · Quy tắc thị trường cần kiểm tra theo ngày hiệu lực và nguồn chính thức.</footer>
  </div>`;
  document.title = "Wiki Chứng khoán Việt Nam";
  $("#reading-progress").style.width = "0";
}

function renderArticle(page) {
  const index = state.pages.findIndex((item) => item.id === page.id);
  const headings = [...page.html.matchAll(/<h([23]) id="([^"]+)">([\s\S]*?)<\/h\1>/g)].map((match) => ({ level: match[1], id: match[2], label: match[3].replace(/<[^>]*>/g, "") }));
  const links = headings.map((heading) => `<a class="toc-level-${heading.level}" href="${pageLink(page)}?anchor=${encodeURIComponent(heading.id)}">${escapeHtml(heading.label)}</a>`).join("");
  const previous = state.pages[index - 1];
  const next = state.pages[index + 1];
  $("#main").innerHTML = `<div class="article-layout"><article class="article-column">
    <div class="breadcrumbs"><a href="#/">Trang chủ</a><span>›</span><span>${escapeHtml(page.category)}</span></div>
    <div class="article-kicker">CHƯƠNG ${String(state.categories.findIndex((item) => item.category === page.categoryId) + 1).padStart(2, "0")} <span>·</span> BÀI ${String(index + 1).padStart(2, "0")}</div>
    <div class="article-body" id="article-body">${page.html}</div>
    <div class="article-end"><span>HẾT BÀI · ${String(index + 1).padStart(2, "0")} / ${state.pages.length}</span><span class="end-line"></span></div>
    <nav class="article-pager" aria-label="Bài liền kề">${previous ? `<a href="${pageLink(previous)}"><small>← BÀI TRƯỚC</small><strong>${escapeHtml(previous.title)}</strong></a>` : "<span></span>"}${next ? `<a href="${pageLink(next)}"><small>BÀI TIẾP THEO →</small><strong>${escapeHtml(next.title)}</strong></a>` : ""}</nav>
  </article><aside class="toc"><div class="toc-stick"><div class="toc-title">TRONG BÀI NÀY</div><nav>${links || '<span class="toc-empty">Bài học ngắn</span>'}</nav><a class="toc-top" href="${pageLink(page)}?anchor=article-body">↑ Về đầu bài</a></div></aside></div>`;
  document.title = `${page.title} · Securities Wiki`;
  $("#reading-progress").style.width = "0";
  for (const block of $("#article-body").querySelectorAll("pre:not(.mermaid)")) {
    const button = document.createElement("button");
    button.className = "copy-button";
    button.textContent = "Sao chép";
    button.addEventListener("click", async () => {
      await navigator.clipboard.writeText(block.querySelector("code")?.textContent ?? block.textContent);
      button.textContent = "Đã chép";
      setTimeout(() => { button.textContent = "Sao chép"; }, 1800);
    });
    block.append(button);
  }
  renderDiagrams();
  const anchor = new URLSearchParams(window.location.hash.split("?")[1] || "").get("anchor");
  if (anchor) requestAnimationFrame(() => document.getElementById(anchor)?.scrollIntoView());
}

let mermaidPromise;
async function renderDiagrams() {
  const blocks = [...document.querySelectorAll("pre.mermaid code")];
  if (!blocks.length) return;
  try {
    mermaidPromise ??= import("https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs");
    const { default: mermaid } = await mermaidPromise;
    mermaid.initialize({ startOnLoad: false, theme: document.documentElement.dataset.theme === "dark" ? "dark" : "neutral", securityLevel: "strict" });
    for (const [index, code] of blocks.entries()) {
      if (!code.isConnected) continue;
      const { svg } = await mermaid.render(`diagram-${Date.now()}-${index}`, code.textContent);
      const wrapper = document.createElement("div");
      wrapper.className = "diagram";
      wrapper.innerHTML = svg;
      code.parentElement.replaceWith(wrapper);
    }
  } catch (error) {
    console.warn("Mermaid diagram unavailable; source remains visible.", error);
  }
}

function renderRoute() {
  const id = routeId();
  renderNavigation(id);
  if (!id) renderHome();
  else if (state.pageById.has(id)) renderArticle(state.pageById.get(id));
  else $("#main").innerHTML = '<div class="not-found"><h1>Không tìm thấy bài học</h1><a href="#/">← Về trang chủ</a></div>';
  if (!window.location.hash.includes("?anchor=")) window.scrollTo(0, 0);
  closeMenu();
}

function search(query) {
  const terms = normalize(query.trim()).split(/\s+/).filter(Boolean);
  if (!terms.length) return [];
  return state.pages.map((page) => {
    const title = normalize(page.title);
    const category = normalize(page.category);
    const body = normalize(page.searchText);
    if (!terms.every((term) => title.includes(term) || category.includes(term) || body.includes(term))) return { page, score: 0 };
    const score = terms.reduce((sum, term) => sum + (title.includes(term) ? 10 : 0) + (category.includes(term) ? 4 : 0) + (body.includes(term) ? 1 : 0), 0);
    return { page, score };
  }).filter(({ score }) => score >= terms.length).sort((a, b) => b.score - a.score).slice(0, 12).map(({ page }) => page);
}

function showResults() {
  const query = $("#search-input").value;
  state.searchResults = search(query);
  $("#search-results").innerHTML = query.trim() ? (state.searchResults.length ? state.searchResults.map((page, index) => `<a href="${pageLink(page)}" data-result="${index}"><span class="result-icon">↗</span><span><strong>${escapeHtml(page.title)}</strong><small>${escapeHtml(page.category)}</small></span><span class="result-arrow">→</span></a>`).join("") : '<p class="no-results">Không tìm thấy bài phù hợp. Thử từ khóa khác.</p>') : '<p class="no-results">Tìm kiếm trong toàn bộ 38 bài học.</p>';
}

function openSearch() {
  $("#search-overlay").hidden = false;
  document.body.classList.add("modal-open");
  $("#search-input").focus();
  showResults();
}

function closeSearch() {
  $("#search-overlay").hidden = true;
  document.body.classList.remove("modal-open");
  $("#search-input").value = "";
}

function closeMenu() {
  $("#sidebar").classList.remove("mobile-open");
  $("#mobile-backdrop").hidden = true;
}

function updateProgress() {
  if (!state.pageById.has(routeId())) return;
  const max = document.documentElement.scrollHeight - window.innerHeight;
  $("#reading-progress").style.width = `${max > 0 ? Math.min(100, (window.scrollY / max) * 100) : 100}%`;
}

async function initialize() {
  try {
    const response = await fetch("./assets/content.json");
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    state.categories = data.categories;
    state.pages = data.pages;
    state.pageById = new Map(data.pages.map((page) => [page.id, page]));
    renderRoute();
  } catch (error) {
    $("#main").innerHTML = '<div class="not-found"><h1>Không tải được thư viện bài học</h1><p>Vui lòng tải lại trang.</p></div>';
    console.error(error);
  }
}

$("#search-trigger").addEventListener("click", openSearch);
$("#search-close").addEventListener("click", closeSearch);
$("#search-input").addEventListener("input", showResults);
$("#search-input").addEventListener("keydown", (event) => {
  if (event.key === "Enter" && state.searchResults[0]) {
    window.location.hash = pageLink(state.searchResults[0]);
    closeSearch();
  }
});
$("#search-overlay").addEventListener("click", (event) => {
  if (event.target === $("#search-overlay") || event.target.closest("[data-result]")) closeSearch();
});
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") { closeSearch(); closeMenu(); }
  if (event.key === "/" && !["INPUT", "TEXTAREA"].includes(document.activeElement.tagName)) {
    event.preventDefault(); openSearch();
  }
});
$("#menu-button").addEventListener("click", () => {
  $("#sidebar").classList.add("mobile-open");
  $("#mobile-backdrop").hidden = false;
});
$("#mobile-backdrop").addEventListener("click", closeMenu);
$("#theme-button").addEventListener("click", () => {
  const next = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
  document.documentElement.dataset.theme = next;
  localStorage.setItem("wiki-theme", next);
  if (state.pageById.has(routeId())) renderRoute();
});
document.documentElement.dataset.theme = localStorage.getItem("wiki-theme") || "light";
window.addEventListener("hashchange", renderRoute);
window.addEventListener("scroll", updateProgress, { passive: true });
initialize();

/**
 * SRC808 Web Components — Shared Header & Footer
 * Usage: <site-header></site-header> / <site-footer></site-footer>
 */

class SiteHeader extends HTMLElement {
  connectedCallback() {
    // Determine active page from current URL
    const path = window.location.pathname;
    const page = path.split("/").pop() || "index.html";

    const activeClass = (target) => {
      if (target === "index.html" && (page === "index.html" || page === "" || page === "SRC808" || path.endsWith("/"))) return ' class="active"';
      if (page === target) return ' class="active"';
      return "";
    };

    const proClass = (target) => {
      if (target === "pro.html") {
        const isActive = page === "pro.html";
        return ` class="nav-link-pro${isActive ? " active" : ""}"`;
      }
      return activeClass(target);
    };

    this.innerHTML = `
    <nav>
      <div class="nav-inner">
        <div class="nav-left">
          <a class="nav-brand" href="index.html">
            <span class="nav-dot"></span>
            <span class="nav-title">SRC808</span>
          </a>
          <a id="navDownloadBtn"
             href="https://github.com/0xlab-co/SRC808/releases/download/v1.6-beta-pro/SRC808-v1.6-beta-pro.dmg"
             class="btn btn-primary nav-cta">
            <span data-lang="en">Download</span>
            <span data-lang="zh">下載</span>
            <span data-lang="zh-CN">下载</span>
            <span data-lang="ja">ダウンロード</span>
            <span data-lang="ko">다운로드</span>
          </a>
        </div>
        <div class="nav-right">
          <ul class="nav-links" id="navLinks">
            <li>
              <a href="index.html"${activeClass("index.html")}>Core</a>
            </li>
            <li><a href="pro.html"${proClass("pro.html")}>Pro</a></li>
            <li><a href="labs.html"${activeClass("labs.html")}>Labs</a></li>
            <li>
              <a href="https://github.com/0xlab-co/SRC808"
                 target="_blank" rel="noopener noreferrer"
                 aria-label="GitHub Repository"
                 style="display:flex;align-items:center;justify-content:center;width:20px;height:20px">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
                  <path d="M12 2C6.477 2 2 6.477 2 12c0 4.42 2.865 8.166 6.839 9.489.5.092.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.462-1.11-1.462-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.646.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.203 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.161 22 16.418 22 12c0-5.523-4.477-10-10-10z"></path>
                </svg>
              </a>
            </li>
          </ul>

          <!-- Language Dropdown -->
          <div class="lang-dropdown-wrapper">
            <button class="lang-toggle" id="langToggleBtn" aria-label="Select Language" title="Select Language">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:18px;height:18px">
                <path d="m12.65 15.67c.14-.36.05-.77-.23-1.05l-2.09-2.06.03-.03c1.74-1.94 2.98-4.17 3.71-6.53h1.94c.54 0 .99-.45.99-.99v-.02c0-.54-.45-.99-.99-.99h-6.01v-1c0-.55-.45-1-1-1s-1 .45-1 1v1h-6.01c-.54 0-.99.45-.99.99 0 .55.45.99.99.99h10.18c-.67 1.94-1.73 3.77-3.17 5.37-.81-.89-1.49-1.86-2.06-2.88-.16-.29-.45-.47-.78-.47-.69 0-1.13.75-.79 1.35.63 1.13 1.4 2.21 2.3 3.21l-4.37 4.31c-.4.39-.4 1.03 0 1.42.39.39 1.02.39 1.42 0l4.28-4.29 2.02 2.02c.51.51 1.38.32 1.63-.35zm4.85-5.67c-.6 0-1.14.37-1.35.94l-3.67 9.8c-.24.61.22 1.26.87 1.26.39 0 .74-.24.88-.61l.89-2.39h4.75l.9 2.39c.14.36.49.61.88.61.65 0 1.11-.65.88-1.26l-3.67-9.8c-.22-.57-.76-.94-1.36-.94zm-1.62 7 1.62-4.33 1.62 4.33z" fill="currentColor"></path>
              </svg>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width:14px;height:14px;opacity:0.7;margin-left:2px">
                <polyline points="6 9 12 15 18 9"></polyline>
              </svg>
            </button>
            <div class="lang-dropdown-menu" id="langDropdown">
              <button class="lang-option" data-value="zh" onclick="selectLang('zh')">繁體中文</button>
              <button class="lang-option" data-value="en" onclick="selectLang('en')">English</button>
              <button class="lang-option" data-value="zh-CN" onclick="selectLang('zh-CN')">简体中文</button>
              <button class="lang-option" data-value="ja" onclick="selectLang('ja')">日本語</button>
              <button class="lang-option" data-value="ko" onclick="selectLang('ko')">한국어</button>
            </div>
          </div>

          <div class="theme-toggle" id="themeToggle" onclick="toggleTheme()" title="Toggle Light/Dark">
            <span class="theme-icon moon">
              <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
              </svg>
            </span>
            <span class="theme-icon sun">
              <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>
              </svg>
            </span>
            <div class="theme-knob"></div>
          </div>
          <button class="menu-toggle" id="menuToggle" aria-label="Toggle navigation" aria-expanded="false">☰</button>
        </div>
      </div>
    </nav>`;
  }
}

class SiteFooter extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
    <footer>
      <div class="container">
        <p style="margin-bottom:24px">
          <span data-lang="en">Like the project? Give us a star on <a href="https://github.com/0xlab-co/src808" target="_blank" rel="noopener noreferrer" style="font-weight:600;text-decoration:underline">GitHub</a>!</span>
          <span data-lang="zh">喜歡這個專案嗎？歡迎到 <a href="https://github.com/0xlab-co/src808" target="_blank" rel="noopener noreferrer" style="font-weight:600;text-decoration:underline">GitHub 為專案點亮 ⭐</a></span>
          <span data-lang="zh-CN">喜欢这个项目吗？欢迎到 <a href="https://github.com/0xlab-co/src808" target="_blank" rel="noopener noreferrer" style="font-weight:600;text-decoration:underline">GitHub 为项目点亮 ⭐</a></span>
          <span data-lang="ja">プロジェクトが気に入りましたか？ <a href="https://github.com/0xlab-co/src808" target="_blank" rel="noopener noreferrer" style="font-weight:600;text-decoration:underline">GitHubで星をつけてください ⭐</a></span>
          <span data-lang="ko">이 프로젝트가 마음에 드시나요? <a href="https://github.com/0xlab-co/src808" target="_blank" rel="noopener noreferrer" style="font-weight:600;text-decoration:underline">GitHub에서 별을 남겨주세요 ⭐</a></span>
        </p>
        <div style="display:flex;align-items:center;justify-content:center;gap:16px">
          <a href="https://github.com/0xlab-co" target="_blank" rel="noopener noreferrer" class="logo-link">
            <svg width="84" viewBox="0 0 2099.05 628.97" xmlns="http://www.w3.org/2000/svg" class="company-logo">
              <g><rect x="62.92" y="62.92" width="62.69" height="125.61"/><rect x="251.68" y="62.92" width="62.69" height="125.61"/><polygon points="0 440.21 62.69 440.21 62.69 314.6 62.69 314.37 62.69 188.76 0 188.76 0 440.21"/><rect x="188.76" y="188.76" width="62.69" height="125.61"/><rect x="125.84" y="314.6" width="62.69" height="125.61"/><polygon points="314.6 188.76 314.6 314.37 314.6 314.6 314.6 440.21 377.29 440.21 377.29 188.76 314.6 188.76"/><rect x="62.92" y="440.44" width="62.69" height="125.61"/><rect x="251.68" y="440.44" width="62.69" height="125.61"/><polygon points="188.53 0 125.84 0 125.84 62.69 188.53 62.69 188.76 62.69 251.45 62.69 251.45 0 188.76 0 188.53 0"/><polygon points="188.53 566.28 125.84 566.28 125.84 628.97 188.53 628.97 188.76 628.97 251.45 628.97 251.45 566.28 188.76 566.28 188.53 566.28"/></g>
              <g><polygon points="1155.48 566.28 1092.33 566.28 1092.33 440.44 1092.33 440.21 1092.33 314.6 1092.33 314.37 1092.33 188.76 1092.33 188.53 1092.33 62.92 1029.64 62.92 1029.64 188.53 1029.64 188.76 1029.64 314.37 1029.64 314.6 1029.64 440.21 1029.64 440.44 1029.64 566.28 966.72 566.28 966.49 566.28 903.57 566.28 840.88 566.28 840.88 628.97 840.88 628.97 840.88 628.97 840.88 628.97 903.57 628.97 966.49 628.97 966.72 628.97 1029.41 628.97 1029.64 628.97 1092.33 628.97 1092.56 628.97 1155.48 628.97 1218.17 628.97 1218.17 628.97 1218.17 566.28 1155.48 566.28"/><polygon points="966.72 62.69 1029.41 62.69 1029.41 0 966.72 0 966.49 0 903.8 0 903.8 62.69 966.49 62.69 966.72 62.69"/></g>
              <g><polygon points="1281.32 566.05 1344.01 566.05 1344.01 440.44 1344.01 440.21 1344.01 314.6 1281.32 314.6 1281.32 566.05"/><polygon points="1595.92 566.28 1595.92 628.97 1658.61 628.97 1658.61 628.97 1658.61 628.97 1658.61 566.28 1595.92 566.28"/><rect x="1281.32" y="62.92" width="62.69" height="125.61"/><polygon points="1469.85 0 1407.16 0 1406.93 0 1344.24 0 1344.24 62.69 1406.93 62.69 1407.16 62.69 1469.85 62.69 1470.08 62.69 1532.77 62.69 1532.77 0 1470.08 0 1469.85 0"/><polygon points="1406.93 566.28 1344.24 566.28 1344.24 628.97 1406.93 628.97 1407.16 628.97 1469.85 628.97 1469.85 566.28 1407.16 566.28 1406.93 566.28"/><rect x="1344.01" y="188.76" width="125.84" height="125.84"/><rect x="1533" y="62.92" width="62.69" height="503.13"/><rect x="1470.08" y="314.37" width="125.61" height="251.68"/></g>
              <g><polygon points="1784.45 0 1721.76 0 1721.76 62.69 1784.68 62.69 1784.68 566.05 1847.37 566.05 1847.37 0 1784.45 0"/><rect x="1784.68" y="314.37" width="125.61" height="251.68"/><polygon points="1973.21 188.76 1910.52 188.76 1910.52 314.37 1973.21 314.37 1973.44 314.37 2036.13 314.37 2036.13 188.76 1973.44 188.76 1973.21 188.76"/><rect x="1721.76" y="566.28" width="62.69" height="62.69"/><rect x="2036.36" y="314.6" width="62.69" height="251.45"/><rect x="1910.52" y="566.28" width="125.61" height="62.69"/></g>
              <g><rect x="444.04" y="188.76" width="54.85" height="43.88"/><rect x="719.28" y="188.76" width="54.85" height="43.88"/><rect x="499.09" y="232.8" width="54.85" height="87.91"/><rect x="664.23" y="232.8" width="54.85" height="87.91"/><rect x="609.19" y="320.87" width="54.85" height="87.91"/><rect x="554.14" y="408.94" width="54.85" height="87.91"/><rect x="499.09" y="497.02" width="54.85" height="87.91"/><rect x="664.23" y="497.02" width="54.85" height="87.91"/><rect x="444.04" y="585.09" width="54.85" height="43.88"/><rect x="719.28" y="585.09" width="54.85" height="43.88"/></g>
            </svg>
          </a>
          <div style="width:1px;height:16px;background-color:var(--border)"></div>
          <p>
            <a href="https://github.com/0xlab-co/SRC808/issues" target="_blank" rel="noopener noreferrer" style="color:var(--muted);text-decoration:none;font-size:0.9rem;transition:color 0.2s;margin-right:12px">Report Issue</a>
            <a href="#" id="contactEmail" style="color:var(--muted);text-decoration:none;font-size:0.9rem;transition:color 0.2s">Contact &amp; Support</a>
          </p>
        </div>
      </div>
    </footer>`;
  }
}

customElements.define("site-header", SiteHeader);
customElements.define("site-footer", SiteFooter);

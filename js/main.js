const menuToggle = document.getElementById("menuToggle");
      const navLinks = document.getElementById("navLinks");

      function closeMobileMenu() {
        if (!navLinks || !menuToggle) return;
        navLinks.classList.remove("open");
        menuToggle.setAttribute("aria-expanded", "false");
      }

      if (menuToggle && navLinks) {
        menuToggle.addEventListener("click", () => {
          const isOpen = navLinks.classList.toggle("open");
          menuToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
        });

        navLinks.querySelectorAll("a").forEach((link) => {
          link.addEventListener("click", () => closeMobileMenu());
        });

        window.addEventListener("resize", () => {
          if (window.innerWidth > 900) closeMobileMenu();
        });
      }

      // --- Language Selection Logic ---
      const langToggleBtn = document.getElementById("langToggleBtn");
      const langDropdown = document.getElementById("langDropdown");

      // 處理語言選單的開關 (Dropdown toggle)
      if (langToggleBtn && langDropdown) {
        langToggleBtn.addEventListener("click", (e) => {
          e.stopPropagation();
          langDropdown.classList.toggle("show");
        });

        // 點擊畫面其他地方自動關閉下拉選單與漢堡選單
        document.addEventListener("click", (e) => {
          if (!langDropdown.contains(e.target)) {
            langDropdown.classList.remove("show");
          }
          if (
            window.innerWidth <= 900 &&
            navLinks &&
            !navLinks.contains(e.target) &&
            !menuToggle.contains(event.target)
          ) {
            closeMobileMenu();
          }
        });
      }

      function setLang(lang) {
        // 更新網頁語系 class
        document.body.className = "lang-" + lang;
        localStorage.setItem("src808-lang", lang);

        // 更新選單項目的 active 狀態
        if (langDropdown) {
          langDropdown.querySelectorAll(".lang-option").forEach((btn) => {
            if (btn.dataset.value === lang) {
              btn.classList.add("active");
            } else {
              btn.classList.remove("active");
            }
          });
        }
      }

      function selectLang(lang) {
        setLang(lang);
        if (langDropdown) {
          langDropdown.classList.remove("show");
        }
      }

      // Restore saved language preference
      const saved = localStorage.getItem("src808-lang") || "en";
      setLang(saved);

      // --- Theme Toggle ---
      function setTheme(theme) {
        document.documentElement.setAttribute("data-theme", theme);
        localStorage.setItem("src808-theme", theme);
      }

      function toggleTheme() {
        const current =
          document.documentElement.getAttribute("data-theme") || "dark";
        setTheme(current === "dark" ? "light" : "dark");
      }

      // Restore saved theme preference (default to dark)
      const savedTheme = localStorage.getItem("src808-theme") || "dark";
      setTheme(savedTheme);

      // Sticky nav CTA visibility on scroll
      const navBar = document.querySelector("nav");
      const featuresSec = document.getElementById("features");
      if (navBar && featuresSec) {
        window.addEventListener("scroll", () => {
          if (window.scrollY >= featuresSec.offsetTop - 80) {
            navBar.classList.add("show-cta");
          } else {
            navBar.classList.remove("show-cta");
          }
        });
      }

      // Contact Email Copy to Clipboard
      const contactEmail = document.getElementById("contactEmail");
      if (contactEmail) {
        contactEmail.addEventListener("click", (e) => {
          e.preventDefault();
          const email = "0xlab.co+src808@gmail.com";

          // iFrame fallback method ensuring cross-platform stability
          const textArea = document.createElement("textarea");
          textArea.value = email;
          textArea.style.position = "fixed";
          textArea.style.left = "-9999px";
          document.body.appendChild(textArea);
          textArea.select();

          try {
            document.execCommand("copy");
            const originalText = contactEmail.innerText;
            contactEmail.innerText = "Copied!";
            setTimeout(() => {
              contactEmail.innerText = originalText;
            }, 2000);
          } catch (err) {
            console.error("Copy failed", err);
          } finally {
            document.body.removeChild(textArea);
          }
        });
      }

      // GitHub Release Automation
      async function initDownloadAutomation() {
        try {
          const response = await fetch(
            "https://api.github.com/repos/0xlab-co/SRC808/releases",
          );
          if (!response.ok) return;
          const releases = await response.json();
          if (!releases || releases.length === 0) return;
          const data = releases[0]; // Take the most recent release (includes pre-releases)

          // Prefer .dmg, but fall back to an uploaded app .zip (not GitHub source archives)
          const releaseAsset =
            data.assets.find((a) => a.name.toLowerCase().endsWith(".dmg")) ||
            data.assets.find((a) => {
              const name = a.name.toLowerCase();
              return (
                name.endsWith(".zip") &&
                name.includes("src808") &&
                !name.includes("source code")
              );
            });
          if (!releaseAsset) return;

          const downloadUrl = releaseAsset.browser_download_url;
          const tagName = data.tag_name;

          // Update Button Links
          ["navDownloadBtn", "heroDownloadBtn"].forEach((id) => {
            const btn = document.getElementById(id);
            if (btn) btn.href = downloadUrl;
          });

          // Update Hero Download Button Text by Locale
          const versionTextMap = {
            en: `Download ${tagName}`,
            zh: `下載 ${tagName}`,
            "zh-CN": `下载 ${tagName}`,
            ja: `${tagName} ダウンロード`,
            ko: `${tagName} 다운로드`,
          };
          document.querySelectorAll("[data-version-text]").forEach((el) => {
            const lang = el.getAttribute("data-lang");
            el.textContent = versionTextMap[lang] || tagName;
          });
        } catch (err) {
          console.error("Failed to sync latest release info:", err);
        }
      }
      initDownloadAutomation();
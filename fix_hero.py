import os

with open('/tmp/original_index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Grab mockup-pro
s_pro = orig.find('<div class="mockup mockup-pro">')
# The mockup structure ends with the STANDBY section Slack row
e_pro = orig.find('<div class="m-app-pct">50%</div>', s_pro)
e_pro = orig.find('</div>', e_pro)
e_pro = orig.find('</div>', e_pro+6)
e_pro = orig.find('</div>', e_pro+6)
e_pro = orig.find('</div>', e_pro+6) + 6

mockup_pro_str = orig[s_pro:e_pro]
if "<div" in mockup_pro_str: print("Found mockup-pro")

with open('pro.html', 'r', encoding='utf-8') as f:
    pro_html = f.read()

s_hero = pro_html.find('<div class="mockup">')
e_hero = pro_html.find('<div class="m-app-pct">50%</div>', s_hero)
e_hero = pro_html.find('</div>', e_hero)
e_hero = pro_html.find('</div>', e_hero+6)
e_hero = pro_html.find('</div>', e_hero+6)
e_hero = pro_html.find('</div>', e_hero+6) + 6

hero_str = pro_html[s_hero:e_hero]
if "<div" in hero_str: print("Found hero mockup")

pro_html = pro_html.replace(hero_str, mockup_pro_str)

with open('pro.html', 'w', encoding='utf-8') as f:
    f.write(pro_html)

print("Pro updated.")

# Now build the new labs.html mockup
labs_mockup = """
        <div class="mockup mockup-pro">
          <div class="mockup-bar">
            <div class="mockup-brand">
              <span class="nav-dot" style="width: 6px; height: 6px"></span>
              <span class="mockup-title"
                >SRC808
                <span
                  style="
                    color: #1ed760;
                    font-size: 10px;
                    margin-left: 4px;
                    padding: 2px 6px;
                    border: 1px solid #1ed760;
                    border-radius: 10px;
                  "
                  >PRO</span
                ></span
              >
            </div>
            <div class="mockup-icons">
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <circle cx="12" cy="12" r="3" />
                <path
                  d="M19.07 4.93a10 10 0 0 1 0 14.14M4.93 4.93a10 10 0 0 0 0 14.14"
                />
              </svg>
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <circle cx="12" cy="12" r="10" />
                <line x1="12" y1="8" x2="12" y2="16" />
                <line x1="8" y1="12" x2="16" y2="12" />
              </svg>
            </div>
          </div>

          <div class="mockup-body">
            <!-- Media 1 -->
            <div class="media-player-card">
              <div class="m-cover" style="background: white;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/e/e1/Google_Chrome_icon_%28February_2022%29.svg" style="width: 24px; height: 24px;" alt="Chrome">
              </div>
              <div class="m-info">
                <div class="m-song">【舞台纯享】就是这个苏味儿！苏运莹演唱《藏无可藏》声线好美 | 剧好听...</div>
                <div class="m-artist">优酷综艺-APP抢先看</div>
              </div>
              <div class="m-controls">
                <div class="m-pro-btn">
                  <svg viewBox="0 0 24 24">
                    <polygon points="19 20 9 12 19 4 19 20"></polygon>
                    <line x1="5" y1="19" x2="5" y2="5" stroke="currentColor" stroke-width="2"></line>
                  </svg>
                </div>
                <div class="m-pro-btn play">
                  <svg viewBox="0 0 24 24" style="fill: #000; margin-left: 2px">
                    <polygon points="5 3 19 12 5 21 5 3"></polygon>
                  </svg>
                </div>
                <div class="m-pro-btn">
                  <svg viewBox="0 0 24 24">
                    <polygon points="5 4 15 12 5 20 5 4"></polygon>
                    <line x1="19" y1="5" x2="19" y2="19" stroke="currentColor" stroke-width="2"></line>
                  </svg>
                </div>
              </div>
            </div>

            <!-- Media 2 -->
            <div class="media-player-card">
              <div class="m-cover" style="background: white;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/e/e1/Google_Chrome_icon_%28February_2022%29.svg" style="width: 24px; height: 24px;" alt="Chrome">
              </div>
              <div class="m-info">
                <div class="m-song">越南邪术-捆魂咒！真实灵异案件 | 老王说</div>
                <div class="m-artist">老王</div>
              </div>
              <div class="m-controls">
                <div class="m-pro-btn">
                  <svg viewBox="0 0 24 24">
                    <polygon points="19 20 9 12 19 4 19 20"></polygon>
                    <line x1="5" y1="19" x2="5" y2="5" stroke="currentColor" stroke-width="2"></line>
                  </svg>
                </div>
                <div class="m-pro-btn play">
                  <svg viewBox="0 0 24 24" style="fill: #000;">
                    <rect x="6" y="4" width="4" height="16"></rect>
                    <rect x="14" y="4" width="4" height="16"></rect>
                  </svg>
                </div>
                <div class="m-pro-btn">
                  <svg viewBox="0 0 24 24">
                    <polygon points="5 4 15 12 5 20 5 4"></polygon>
                    <line x1="19" y1="5" x2="19" y2="19" stroke="currentColor" stroke-width="2"></line>
                  </svg>
                </div>
              </div>
            </div>

            <!-- Media 3 -->
            <div class="media-player-card">
              <div class="m-cover">
                <svg viewBox="0 0 24 24" style="fill: #000; width: 24px; height: 24px">
                  <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.54.659.301 1.02zm1.44-3.3c-.301.42-.84.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.801.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.6.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.419 1.56-.239.54-.959.72-1.56.3z" />
                </svg>
              </div>
              <div class="m-info">
                <div class="m-song">把风唱给你听</div>
                <div class="m-artist">KeyKey</div>
              </div>
              <div class="m-controls">
                <div class="m-pro-btn">
                  <svg viewBox="0 0 24 24">
                    <polygon points="19 20 9 12 19 4 19 20"></polygon>
                    <line x1="5" y1="19" x2="5" y2="5" stroke="currentColor" stroke-width="2"></line>
                  </svg>
                </div>
                <div class="m-pro-btn play">
                  <svg viewBox="0 0 24 24" style="fill: #000; margin-left: 2px">
                    <polygon points="5 3 19 12 5 21 5 3"></polygon>
                  </svg>
                </div>
                <div class="m-pro-btn">
                  <svg viewBox="0 0 24 24">
                    <polygon points="5 4 15 12 5 20 5 4"></polygon>
                    <line x1="19" y1="5" x2="19" y2="19" stroke="currentColor" stroke-width="2"></line>
                  </svg>
                </div>
              </div>
            </div>

            <div class="m-card">
              <div class="m-label">▲ OUTPUT</div>
              <div class="m-output-row">
                <div class="m-icon">📺</div>
                <div class="m-device">
                  <div class="m-device-name">MSI MD272UPS</div>
                  <div class="m-device-sub">System Output</div>
                </div>
                <div class="m-vol-wrap">
                  <div class="m-icon" style="font-size: 14px; width: auto;">🔊</div>
                  <div class="m-track" style="height: 24px; border-radius: 4px; border: 1px solid #333; overflow: hidden; position: relative;">
                    <div class="m-fill fill-green" style="width: 35%; position: absolute; left: 0; top: 0; bottom: 0;"></div>
                  </div>
                  <div class="m-pct" style="font-weight: bold; color: white;">35%</div>
                </div>
              </div>
            </div>

            <div class="m-row">
              <div class="m-card">
                <div class="m-label" style="display: flex; justify-content: space-between;">
                  <span style="color: #4ade80;">▶ ACTIVE</span>
                  <span style="background: #09090b; padding: 2px 6px; border-radius: 4px;">3</span>
                </div>
                <div class="m-app-row">
                  <div class="m-app-icon" style="background: transparent; border: none; font-size: 18px;">🌈</div>
                  <div class="m-app-track" style="height: 24px; background: transparent; position: relative;">
                     <div class="m-app-fill fill-green" style="width: 100%; height: 24px; border-radius: 4px;"></div>
                     <span style="position: absolute; left: 8px; top: 4px; color: black; font-weight: bold; font-family: sans-serif; font-size: 11px;">Arc</span>
                     <span style="position: absolute; right: 8px; top: 4px; color: black; font-weight: bold; font-family: monospace; font-size: 10px;">100%</span>
                  </div>
                  <div class="m-app-pct" style="width: auto; font-size: 14px; color: #f8e71c;">📌</div>
                </div>
                <div class="m-app-row">
                  <div class="m-app-icon" style="background: transparent; border: none; font-size: 18px;">🎵</div>
                  <div class="m-app-track" style="height: 24px; background: transparent; position: relative;">
                     <div class="m-app-fill fill-green" style="width: 45%; height: 24px; border-radius: 4px;"></div>
                     <span style="position: absolute; left: 8px; top: 4px; color: white; font-weight: bold; font-family: sans-serif; font-size: 11px; text-shadow: 0 1px 2px black;">Spotify</span>
                     <span style="position: absolute; right: 8px; top: 4px; color: white; font-weight: bold; font-family: monospace; font-size: 10px;">45%</span>
                  </div>
                  <div class="m-app-pct" style="width: auto; font-size: 14px; color: #f8e71c;">📌</div>
                </div>
                <div class="m-app-row">
                  <div class="m-app-icon" style="background: transparent; border: none; font-size: 18px;">✈️</div>
                  <div class="m-app-track" style="height: 24px; background: transparent; position: relative;">
                     <div class="m-app-fill fill-green" style="width: 3%; height: 24px; border-radius: 4px;"></div>
                     <span style="position: absolute; left: 8px; top: 4px; color: white; font-weight: bold; font-family: sans-serif; font-size: 11px;">Telegram</span>
                     <span style="position: absolute; right: 8px; top: 4px; color: white; font-weight: bold; font-family: monospace; font-size: 10px;">3%</span>
                  </div>
                  <div class="m-app-pct" style="width: auto; font-size: 14px; color: #f8e71c;">📌</div>
                </div>
              </div>
              <div class="m-card">
                <div class="m-label" style="display: flex; justify-content: space-between;">
                  <span>◼ STANDBY</span>
                  <span style="background: #09090b; padding: 2px 6px; border-radius: 4px;">4</span>
                </div>
                <div class="m-app-row">
                  <div class="m-app-icon" style="background: transparent; border: none; font-size: 18px;">💬</div>
                  <div class="m-app-track" style="height: 24px; background: #3b82f6; opacity: 0.8; position: relative; border-radius: 4px;">
                     <span style="position: absolute; left: 8px; top: 4px; color: white; font-weight: bold; font-family: sans-serif; font-size: 11px;">LINE</span>
                     <span style="position: absolute; right: 8px; top: 4px; color: white; font-weight: bold; font-family: monospace; font-size: 10px;">100%</span>
                  </div>
                  <div class="m-app-pct" style="width: auto;"></div>
                </div>
                <div class="m-app-row">
                  <div class="m-app-icon" style="background: transparent; border: none; font-size: 18px;">🖼️</div>
                  <div class="m-app-track" style="height: 24px; background: #3b82f6; opacity: 0.8; position: relative; border-radius: 4px;">
                     <span style="position: absolute; left: 8px; top: 4px; color: white; font-weight: bold; font-family: sans-serif; font-size: 11px;">Preview</span>
                     <span style="position: absolute; right: 8px; top: 4px; color: white; font-weight: bold; font-family: monospace; font-size: 10px;">100%</span>
                  </div>
                  <div class="m-app-pct" style="width: auto;"></div>
                </div>
                <div class="m-app-row">
                  <div class="m-app-icon" style="background: transparent; border: none; font-size: 18px;">⚙️</div>
                  <div class="m-app-track" style="height: 24px; background: #3b82f6; opacity: 0.8; position: relative; border-radius: 4px;">
                     <span style="position: absolute; left: 8px; top: 4px; color: white; font-weight: bold; font-family: sans-serif; font-size: 11px;">System Settings</span>
                     <span style="position: absolute; right: 8px; top: 4px; color: white; font-weight: bold; font-family: monospace; font-size: 10px;">100%</span>
                  </div>
                  <div class="m-app-pct" style="width: auto;"></div>
                </div>
                <div class="m-app-row">
                  <div class="m-app-icon" style="background: transparent; border: none; font-size: 18px;">🖥️</div>
                  <div class="m-app-track" style="height: 24px; background: #3b82f6; opacity: 0.8; position: relative; border-radius: 4px;">
                     <span style="position: absolute; left: 8px; top: 4px; color: white; font-weight: bold; font-family: sans-serif; font-size: 11px;">VMware Fusion</span>
                     <span style="position: absolute; right: 8px; top: 4px; color: white; font-weight: bold; font-family: monospace; font-size: 10px;">100%</span>
                  </div>
                  <div class="m-app-pct" style="width: auto;"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
"""

with open('labs.html', 'r', encoding='utf-8') as f:
    labs_html = f.read()

s_hero = labs_html.find('<div class="mockup">')
e_hero = labs_html.find('<div class="m-app-pct">50%</div>', s_hero)
e_hero = labs_html.find('</div>', e_hero)
e_hero = labs_html.find('</div>', e_hero+6)
e_hero = labs_html.find('</div>', e_hero+6)
e_hero = labs_html.find('</div>', e_hero+6) + 6

hero_str = labs_html[s_hero:e_hero]
if "<div" in hero_str: print("Found labs mockup")

labs_html = labs_html.replace(hero_str, labs_mockup)

with open('labs.html', 'w', encoding='utf-8') as f:
    f.write(labs_html)

print("Labs updated.")

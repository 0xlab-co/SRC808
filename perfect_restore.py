import os

with open('/tmp/original_index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Split out sections
pre_main = orig[:orig.find('    <!-- Hero -->')]
post_main = orig[orig.find('    <!-- Footer -->'):]

main_content = orig[orig.find('    <!-- Hero -->'):orig.find('</section>', orig.find('<section id="privacy">')) + len('</section>')]

def get_sec(c, id_name):
    start = c.find(f'<section id="{id_name}">')
    if start == -1: start = c.find(f'<section class="{id_name}">')
    if start == -1: return ""
    end = c.find('</section>', start) + len('</section>')
    return c[start:end]

hero_sec = get_sec(main_content, 'hero')
pro_sec = get_sec(main_content, 'pro')

# Extract mockup-pro from pro_sec
start_pro = pro_sec.find('<div class="mockup mockup-pro">')
# the mockup ends right before <div class="features">
end_pro = pro_sec.find('</div>\n\n        <div class="features">', start_pro)
if end_pro == -1:
    end_pro = pro_sec.find('<div class="features">', start_pro) - 8

mockup_pro_html = pro_sec[start_pro:end_pro]

# Remove mockup-pro from pro_sec
pro_sec_clean = pro_sec[:start_pro] + pro_sec[end_pro:]

# Replace hero mockup with mockup-pro
start_hero = hero_sec.find('<div class="mockup">')
end_hero = hero_sec.find('</div>\n      </section>', start_hero)
if end_hero == -1:
    end_hero = hero_sec.find('</section>', start_hero) - 6

hero_sec_clean = hero_sec[:start_hero] + mockup_pro_html + hero_sec[end_hero:]

# Assemble new pro.html
new_html = pre_main + hero_sec_clean + "\n\n" + pro_sec_clean + post_main

# Nav replacement
new_nav = """<ul class="nav-links" id="navLinks">
            <li>
              <a href="index.html">
                <span data-lang="en">Core</span>
                <span data-lang="zh">Core (核心)</span>
                <span data-lang="zh-CN">Core (核心)</span>
                <span data-lang="ja">Core (コア)</span>
                <span data-lang="ko">Core (코어)</span>
              </a>
            </li>
            <li><a href="pro.html" class="nav-link-pro">Pro</a></li>
            <li><a href="labs.html">Labs</a></li>
            <li>
              <a href="changelog.html">
                <span data-lang="en">Updates</span>
                <span data-lang="zh">更新記錄</span>
                <span data-lang="zh-CN">更新记录</span>
                <span data-lang="ja">更新情報</span>
                <span data-lang="ko">업데이트</span>
              </a>
            </li>
            <li>
              <a href="guide/installation.html">"""

start_nav = new_html.find('<ul class="nav-links" id="navLinks">')
end_nav = new_html.find('<a href="guide/installation.html">', start_nav)
if start_nav != -1 and end_nav != -1:
    new_html = new_html[:start_nav] + new_nav + new_html[end_nav + len('<a href="guide/installation.html">'):]

# Tag replacement
new_html = new_html.replace('tag-free', 'tag-core')
new_html = new_html.replace('<span class="feature-tag tag-core">Free</span>', '<span class="feature-tag tag-core">Core</span>')

# Hero zh replacement for pro.html
new_html = new_html.replace('<h1 data-lang="zh">所有音訊<br /><span>集中一起</span>控制</h1>', '<h1 data-lang="zh">突破極限的控制<br /><span>SRC808 Pro</span></h1>')
old_sub_zh = '<p class="hero-sub" data-lang="zh">\n          把每個 App、每個裝置的音量記憶，<br />\n          集中在同一個選單列面板裡\n        </p>'
new_sub_zh = '<p class="hero-sub" data-lang="zh">\n          基於 DriverKit 技術的底層音訊進化，<br />\n          解鎖更進階、更無縫的 macOS 原生控制體驗。\n        </p>'
new_html = new_html.replace(old_sub_zh, new_sub_zh)

with open('pro.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("pro.html perfectly restored.")

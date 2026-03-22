import re

with open('/tmp/original_index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Split sections for pro.html (from split_site.py logic)
pre_main = orig[:orig.find('    <!-- Hero -->')]
post_main = orig[orig.find('    <!-- Footer -->'):]

main_start = orig.find('    <!-- Hero -->')
main_end = orig.find('</section>', orig.find('<section id="privacy">')) + len('</section>')
main_content = orig[main_start:main_end]

def get_section(content, sec_id):
    if sec_id == 'hero':
        start = content.find('<section class="hero">')
    else:
        start = content.find(f'<section id="{sec_id}">')
    if start == -1: return ""
    end = content.find('</section>', start) + len('</section>')
    return content[start:end]

hero_sec = get_section(main_content, 'hero')
pro_sec = get_section(main_content, 'pro')

# Combine sections to create basic pro.html content
new_pro_html = pre_main + hero_sec + "\n\n" + pro_sec + post_main

# 1. Update navigation links (like fix_nav.py did)
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
pattern = r'<ul class="nav-links" id="navLinks">.*?<a\s+href="guide/installation.html">'
new_pro_html = re.sub(pattern, new_nav, new_pro_html, flags=re.DOTALL)

# 2. Free to Core
new_pro_html = new_pro_html.replace('.tag-free', '.tag-core')
new_pro_html = new_pro_html.replace('tag-free', 'tag-core')
new_pro_html = re.sub(r'<span class="feature-tag tag-core">Free</span>', r'<span class="feature-tag tag-core">Core</span>', new_pro_html)

# 3. zh Translation custom strings
old_h1_zh = r'<h1 data-lang="zh">所有音訊<br /><span>集中一起</span>控制</h1>'
new_h1_zh = r'<h1 data-lang="zh">突破極限的控制<br /><span>SRC808 Pro</span></h1>'
new_pro_html = re.sub(old_h1_zh, new_h1_zh, new_pro_html)

old_sub_zh = r'<p class="hero-sub" data-lang="zh">\s*把每個 App、每個裝置的音量記憶，<br />\s*集中在同一個選單列面板裡\s*</p>'
new_sub_zh = r'<p class="hero-sub" data-lang="zh">\n        基於 DriverKit 技術的底層音訊進化，<br />\n        解鎖更進階、更無縫的 macOS 原生控制體驗。\n      </p>'
new_pro_html = re.sub(old_sub_zh, new_sub_zh, new_pro_html)

# 4. Safely swap mockup-pro to hero section
# Find the mockup in hero
m_hero = re.search(r'(<div class="mockup">.*?)</div>\s*</section>', new_pro_html, re.DOTALL)
m_pro = re.search(r'(<div class="mockup mockup-pro">.*?)</div>\n        <div class="features">', new_pro_html, re.DOTALL)

if m_hero and m_pro:
    str_hero = m_hero.group(1)
    str_pro = m_pro.group(1)
    
    # Replace the regular mockup in hero with the pro mockup
    new_pro_html = new_pro_html.replace(str_hero, str_pro, 1)
    # Remove the mockup from the pro section
    new_pro_html = new_pro_html.replace(str_pro, '', 1)

with open('pro.html', 'w', encoding='utf-8') as f:
    f.write(new_pro_html)

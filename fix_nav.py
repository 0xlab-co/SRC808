import re

files = ['index.html', 'pro.html', 'labs.html', 'changelog.html']

new_nav = """<ul class="nav-links" id="navLinks">
            <li>
              <a href="index.html">
                <span data-lang="en">Core</span>
                <span data-lang="zh">Core</span>
                <span data-lang="zh-CN">Core</span>
                <span data-lang="ja">Core</span>
                <span data-lang="ko">Core</span>
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

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    pattern = r'<ul class="nav-links" id="navLinks">.*?<a\s+href="guide/installation.html">'
    html = re.sub(pattern, new_nav, html, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Nav updated")

import re
import shutil

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the navigation links globally in the template first
old_nav = """          <li>
            <a href="#features">
              <span data-lang="en">Core</span>
              <span data-lang="zh">Core (核心)</span>
              <span data-lang="zh-CN">Core (核心)</span>
              <span data-lang="ja">Core (コア)</span>
              <span data-lang="ko">Core (코어)</span>
            </a>
          </li>
          <li><a href="#pro" class="nav-link-pro">Pro</a></li>
          <li><a href="#labs">Labs</a></li>
          <li>
            <a href="#changelog">
              <span data-lang="en">Changelog</span>
              <span data-lang="zh">更新日誌</span>
              <span data-lang="zh-CN">更新日志</span>
              <span data-lang="ja">変更履歴</span>
              <span data-lang="ko">변경 내역</span>
            </a>
          </li>
          <li>
            <a href="#known-issues">
              <span data-lang="en">Known Issues</span>
              <span data-lang="zh">已知問題</span>
              <span data-lang="zh-CN">已知问题</span>
              <span data-lang="ja">既知の問題</span>
              <span data-lang="ko">알려진 문제</span>
            </a>
          </li>
          <li>
            <a href="#roadmap">
              <span data-lang="en">Roadmap</span>
              <span data-lang="zh">路線圖</span>
              <span data-lang="zh-CN">路线图</span>
              <span data-lang="ja">ロードマップ</span>
              <span data-lang="ko">로드맵</span>
            </a>
          </li>"""

new_nav = """          <li>
            <a href="index.html#features">
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
          </li>"""

html = html.replace(old_nav, new_nav)

# Extract sections
def extract_section(section_id):
    pattern = r'(<section id="' + section_id + r'">.*?</section>)'
    match = re.search(pattern, html, flags=re.DOTALL)
    return match.group(1) if match else ""

features_sec = extract_section("features")
pro_sec = extract_section("pro")
labs_sec = extract_section("labs")
changelog_sec = extract_section("changelog")
known_issues_sec = extract_section("known-issues")
roadmap_sec = extract_section("roadmap")
requirements_sec = extract_section("requirements")
privacy_sec = extract_section("privacy")

# Base layout (hero + main container)
# Find the start of the first section to know where <main> content starts
main_start = html.find('<section id="features">')
# Find the end of privacy to know where <main> ends (before grid-bg)
main_end = html.find('</section>', html.find('<section id="privacy">')) + len('</section>')

if main_start == -1 or main_end == -1:
    print("Failed to find main boundaries")
    exit(1)

pre_main = html[:main_start]
post_main = html[main_end:]

# Also identify the hero section which is inside the header or main, wait, let's extract hero
# Actually, the Hero is just everything from `<div class="hero"` or `<main...>` to `<section id="features">`
# I'll just keep pre_main for the base template.

# Create index.html (Core)
index_html = pre_main + features_sec + "\n\n" + requirements_sec + "\n\n" + privacy_sec + post_main
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# Create pro.html (Pro)
pro_html = pre_main + pro_sec + post_main
with open('pro.html', 'w', encoding='utf-8') as f:
    f.write(pro_html)

# Create labs.html (Labs)
labs_html = pre_main + labs_sec + post_main
with open('labs.html', 'w', encoding='utf-8') as f:
    f.write(labs_html)

# Create changelog.html (Updates)
changelog_html = pre_main + changelog_sec + "\n\n" + known_issues_sec + "\n\n" + roadmap_sec + post_main
with open('changelog.html', 'w', encoding='utf-8') as f:
    f.write(changelog_html)

print("done")

import re

files = ['index.html', 'pro.html', 'labs.html', 'changelog.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Change "Free" to "Core" in tags and text
    html = html.replace('.tag-free', '.tag-core')
    html = html.replace('tag-free', 'tag-core')
    # Use regex to change the text inside the feature tag
    html = re.sub(r'<span class="feature-tag tag-core">Free</span>', r'<span class="feature-tag tag-core">Core</span>', html)
    
    # Specific changes for Hero section Traditional Chinese text
    
    if file == 'pro.html':
        old_h1_zh = r'<h1 data-lang="zh">所有音訊<br /><span>集中一起</span>控制</h1>'
        new_h1_zh = r'<h1 data-lang="zh">突破極限的控制<br /><span>SRC808 Pro</span></h1>'
        html = re.sub(old_h1_zh, new_h1_zh, html)

        old_sub_zh = r'<p class="hero-sub" data-lang="zh">\s*把每個 App、每個裝置的音量記憶，<br />\s*集中在同一個選單列面板裡\s*</p>'
        new_sub_zh = r'<p class="hero-sub" data-lang="zh">\n        基於 DriverKit 技術的底層音訊進化，<br />\n        解鎖更進階、更無縫的 macOS 原生控制體驗。\n      </p>'
        html = re.sub(old_sub_zh, new_sub_zh, html)

    if file == 'labs.html':
        old_h1_zh = r'<h1 data-lang="zh">所有音訊<br /><span>集中一起</span>控制</h1>'
        new_h1_zh = r'<h1 data-lang="zh">探索前衛整合<br /><span>SRC808 Labs</span></h1>'
        html = re.sub(old_h1_zh, new_h1_zh, html)

        old_sub_zh = r'<p class="hero-sub" data-lang="zh">\s*把每個 App、每個裝置的音量記憶，<br />\s*集中在同一個選單列面板裡\s*</p>'
        new_sub_zh = r'<p class="hero-sub" data-lang="zh">\n        實驗性的擴充套件與進階功能整合，<br />\n        體驗 SRC808 未來可能性的第一線。\n      </p>'
        html = re.sub(old_sub_zh, new_sub_zh, html)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updates applied")

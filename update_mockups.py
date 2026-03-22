import re

# 1. Update pro.html
with open('pro.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract mockup-pro
m_pro_match = re.search(r'<div class="mockup mockup-pro">.*?</div>\s*</div>\s*</div>', html, re.DOTALL)
if m_pro_match:
    mockup_pro_html = m_pro_match.group(0)
    
    # Remove mockup-pro from its original place
    html = html.replace(mockup_pro_html, '', 1)
    
    # Replace the hero mockup with mockup_pro_html
    m_hero_match = re.search(r'<div class="mockup">.*?</div>\s*</div>\s*</div>', html, re.DOTALL)
    if m_hero_match:
        html = html.replace(m_hero_match.group(0), mockup_pro_html, 1)

with open('pro.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated pro.html")

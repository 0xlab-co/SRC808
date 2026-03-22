import re

with open('pro.html', 'r', encoding='utf-8') as f:
    html = f.read()

# find mockup-pro
start_pro = html.find('<div class="mockup mockup-pro">')
if start_pro == -1:
    print("Could not find mockup-pro")
else:
    # Find matching closing div for mockup-pro
    # Usually it's followed by </div> </div> </div>
    end_pro = html.find('</div>\n\n        <div class="features">', start_pro)
    if end_pro == -1:
        end_pro = html.find('<div class="features">', start_pro) - len('</div>')
    
    # We can manually find the end by matching tags, but it's easier:
    end_pro_manual = html.find('</div>\n          </div>\n        </div>', start_pro) + len('</div>\n          </div>\n        </div>')
    
    mockup_pro_str = html[start_pro:end_pro_manual]
    print(f"Found mockup-pro, length {len(mockup_pro_str)}")
    
    # remove it
    html = html.replace(mockup_pro_str, '')
    
    # replace first mockup
    start_hero = html.find('<div class="mockup">')
    end_hero = html.find('</div>\n          </div>\n        </div>', start_hero) + len('</div>\n          </div>\n        </div>')
    
    if start_hero != -1:
        hero_str = html[start_hero:end_hero]
        html = html.replace(hero_str, mockup_pro_str)
        print("Replaced hero mockup")
    else:
        print("Could not find hero mockup")

with open('pro.html', 'w', encoding='utf-8') as f:
    f.write(html)

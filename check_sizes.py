import os
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
tags = soup.find_all(['img', 'script', 'link'])

for t in tags:
    src = t.get('src') or t.get('href')
    if src and not src.startswith(('http', 'data:', '/style')):
        clean_src = src.replace('./', '')
        if os.path.exists(clean_src):
            size = os.path.getsize(clean_src) / 1024
            print(f"{src}: {size:.2f} KB")
        else:
            print(f"{src}: not found locally")

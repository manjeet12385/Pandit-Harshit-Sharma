from bs4 import BeautifulSoup
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
tags = soup.find_all(['img', 'script', 'link'])

for t in tags:
    src = t.get('src') or t.get('href')
    if src and src.startswith('http'):
        print(f"{t.name}: {src}")

import glob

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content.replace('<link rel="preconnect" href="https://translate.googleapis.com">', '<link rel="preconnect" href="https://translate.googleapis.com" crossorigin>')
    content = content.replace('<link rel="preconnect" href="https://translate-pa.googleapis.com">', '<link rel="preconnect" href="https://translate-pa.googleapis.com" crossorigin>')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

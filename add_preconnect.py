import glob

html_files = glob.glob('*.html')
preconnect_tags = """
  <link rel="preconnect" href="https://translate.googleapis.com">
  <link rel="preconnect" href="https://translate-pa.googleapis.com">
"""

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if '<link rel="preconnect" href="https://translate.googleapis.com">' not in content:
        content = content.replace('</head>', f'{preconnect_tags}</head>')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)

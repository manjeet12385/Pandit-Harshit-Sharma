import glob

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace font loading hack with standard loading
    content = content.replace('<link rel="preload" href="https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,400..700;1,400..700&amp;family=Plus+Jakarta+Sans:ital,wght@0,400..800;1,400..800&amp;display=swap" as="style" onload="this.onload=null;this.rel=\'stylesheet\'"/>', '<link href="https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,400..700;1,400..700&amp;family=Plus+Jakarta+Sans:ital,wght@0,400..800;1,400..800&amp;display=swap" rel="stylesheet">')
    content = content.replace('<link rel="preload" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght@400&amp;display=swap" as="style" onload="this.onload=null;this.rel=\'stylesheet\'"/>', '<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght@400&amp;display=swap" rel="stylesheet">')
    
    # Remove noscript fallbacks since we aren't deferring anymore
    content = content.replace('<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,400..700;1,400..700&amp;family=Plus+Jakarta+Sans:ital,wght@0,400..800;1,400..800&amp;display=swap"/></noscript>', '')
    content = content.replace('<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght@400&amp;display=swap"/></noscript>', '')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

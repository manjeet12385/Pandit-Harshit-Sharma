import os
import re

files = ['index.html', 'services.html', 'contact.html', 'gallery.html']
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove Tailwind CDN script
    content = content.replace('<script src="https://cdn.tailwindcss.com"></script>', '')
    
    # Remove tailwind config block
    content = re.sub(r'<script id="tailwind-config">.*?</script>', '', content, flags=re.DOTALL)
    
    # Replace the inline style block with the external css link
    content = re.sub(r'<style>@layer base.*?</style>', '<link rel="stylesheet" href="/style.css" />', content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Cleaned {f}")

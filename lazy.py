import re

files = ['index.html', 'services.html', 'contact.html', 'gallery.html']
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    def add_lazy(match):
        img = match.group(0)
        if 'logo' in img.lower() or 'loading=' in img:
            return img
        return img.replace('<img ', '<img loading="lazy" decoding="async" ')

    content = re.sub(r'<img [^>]+>', add_lazy, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Processed {f}')

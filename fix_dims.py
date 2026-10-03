import glob

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Add width and height to SVG icons
    content = content.replace('src="https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg" alt="YouTube" class="h-6"', 'width="24" height="24" src="https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg" alt="YouTube" class="h-6"')
    content = content.replace('src="https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg" alt="YouTube" class="h-5 md:h-6', 'width="24" height="24" src="https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg" alt="YouTube" class="h-5 md:h-6')
    content = content.replace('src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg" alt="Instagram" class="h-6"', 'width="24" height="24" src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg" alt="Instagram" class="h-6"')
    content = content.replace('src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg" alt="Instagram" class="h-7', 'width="28" height="28" src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg" alt="Instagram" class="h-7')
    content = content.replace('src="https://upload.wikimedia.org/wikipedia/commons/b/b8/2021_Facebook_icon.svg" alt="Facebook" class="h-6"', 'width="24" height="24" src="https://upload.wikimedia.org/wikipedia/commons/b/b8/2021_Facebook_icon.svg" alt="Facebook" class="h-6"')
    
    # Fix the missing width on line 478 image
    content = content.replace('alt="माँ बगलामुखी मंदिर नलखेड़ा - तीन देवियों की प्रतिमा" class="w-full" src="./image copy 5.webp" style="display:block; width:; height:auto;', 'width="425" height="563" alt="माँ बगलामुखी मंदिर नलखेड़ा - तीन देवियों की प्रतिमा" class="w-full" src="./image copy 5.webp" style="display:block; height:auto;')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

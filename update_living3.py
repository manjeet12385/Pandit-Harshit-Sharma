import re

with open('living-bedroom.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update onclicks in the sidebar
html = html.replace("onclick=\"showSection('super-saver')\"", "onclick=\"showSection('all-services-container'); setTimeout(() => document.getElementById('super-saver').scrollIntoView({behavior: 'smooth', block: 'start'}), 100);\"")
html = html.replace("onclick=\"showSection('cleaning-stain')\"", "onclick=\"showSection('all-services-container'); setTimeout(() => document.getElementById('cleaning-stain').scrollIntoView({behavior: 'smooth', block: 'start'}), 100);\"")
html = html.replace("onclick=\"showSection('sofa-carpet')\"", "onclick=\"showSection('all-services-container'); setTimeout(() => document.getElementById('sofa-carpet').scrollIntoView({behavior: 'smooth', block: 'start'}), 100);\"")

# 2. Wrap the sections in all-services-container and ensure they are display: block
# First, change display: none to display: block for these sections
html = html.replace('<div id="super-saver" style="display: none; padding: 10px 0;">', '<div id="super-saver" style="display: block; padding: 10px 0;">')
html = html.replace('<div id="cleaning-stain" style="display: none; padding: 10px 0;">', '<div id="cleaning-stain" style="display: block; padding: 10px 0;">')
html = html.replace('<div id="sofa-carpet" style="display: none; padding: 10px 0;">', '<div id="sofa-carpet" style="display: block; padding: 10px 0;">')

# Now wrap them
wrapper_start = '<div id="all-services-container" style="display: none;">\n'
wrapper_end = '\n</div><!-- END all-services-container -->'

# Find where super-saver starts and sofa-carpet ends
html = re.sub(
    r'(<div id="super-saver".*?<!-- Card 5 -->.*?</div>\s*</div>\s*</div>)',
    wrapper_start + r'\1' + wrapper_end,
    html,
    flags=re.DOTALL
)

# 3. Update the showSection script
new_script = '''    <script>
        function showSection(sectionId) {
            const allSections = ['default-banner', 'all-services-container'];
            
            allSections.forEach(id => {
                const el = document.getElementById(id);
                if (el) el.style.display = 'none';
            });
            
            const targetSection = document.getElementById(sectionId);
            if (targetSection) targetSection.style.display = 'block';
        }
    </script>'''

html = re.sub(r'<script>\s*function showSection\(sectionId\).*?</script>', new_script, html, flags=re.DOTALL)

with open('living-bedroom.html', 'w', encoding='utf-8') as f:
    f.write(html)

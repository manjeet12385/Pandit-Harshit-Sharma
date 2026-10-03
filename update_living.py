import re

with open('kitchen-cleaning.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Page Title
html = re.sub(r'<h1 class="kitchen-title">.*?</h1>', '<h1 class="kitchen-title">Living &amp;<br>Bedroom...</h1>', html, flags=re.IGNORECASE|re.DOTALL)
html = re.sub(r'<title>.*?</title>', '<title>Living & Bedroom Cleaning - Joamex</title>', html, flags=re.IGNORECASE)

# Replace rating
html = re.sub(r'<strong>4\.82</strong>\s*<span>\(3\.9 M bookings\)</span>', '<strong>4.86</strong>\\n                          <span>(523K bookings)</span>', html)
html = re.sub(r'<div style="font-size: 12px; margin-top: 2px; font-weight: bold;">Mon, 3:30 PM</div>', '<div style="font-size: 12px; margin-top: 2px; font-weight: bold;">Thu, 3:00 PM</div>', html)

# Sidebar items
sidebar_html = '''
                    <div class="service-option" onclick="showSection('super-saver')">
                        <div class="service-option-icon">
                            <span style="color: #1e8f52; font-weight: 800; font-size: 24px; text-align: center; line-height: 1.1;">%</span>
                        </div>
                        <div class="service-option-text">Super saver deals</div>
                    </div>
                    <div class="service-option" onclick="showSection('cleaning-stain')">
                        <div class="service-option-icon">
                            <img src="images/cleaning.jpg" alt="Cleaning & stain protection">
                        </div>
                        <div class="service-option-text">Cleaning & stain protection</div>
                    </div>
                    <div class="service-option" onclick="showSection('sofa-carpet')">
                        <div class="service-option-icon">
                            <img src="images/cleaning.jpg" alt="Sofa & carpet">
                        </div>
                        <div class="service-option-text">Sofa & carpet</div>
                    </div>
                    <div class="service-option" onclick="showSection('curtain')">
                        <div class="service-option-icon">
                            <img src="images/cleaning.jpg" alt="Curtain">
                        </div>
                        <div class="service-option-text">Curtain</div>
                    </div>
                    <div class="service-option" onclick="showSection('living-care')">
                        <div class="service-option-icon">
                            <img src="images/cleaning.jpg" alt="Living room care">
                        </div>
                        <div class="service-option-text">Living room care</div>
                    </div>
                    <div class="service-option" onclick="showSection('bedroom-care')">
                        <div class="service-option-icon">
                            <img src="images/cleaning.jpg" alt="Bedroom care">
                        </div>
                        <div class="service-option-text">Bedroom care</div>
                    </div>
                    <div class="service-option" onclick="showSection('mattress-bed')">
                        <div class="service-option-icon">
                            <img src="images/cleaning.jpg" alt="Mattress & bed">
                        </div>
                        <div class="service-option-text">Mattress & bed</div>
                    </div>
                    <div class="service-option" onclick="showSection('dining-table')">
                        <div class="service-option-icon">
                            <img src="images/cleaning.jpg" alt="Dining table & chairs">
                        </div>
                        <div class="service-option-text">Dining table & chairs</div>
                    </div>
                    <div class="service-option" onclick="showSection('other-furniture')">
                        <div class="service-option-icon">
                            <img src="images/cleaning.jpg" alt="Other furniture">
                        </div>
                        <div class="service-option-text">Other furniture</div>
                    </div>
                    <div class="service-option" onclick="showSection('windows-fan')">
                        <div class="service-option-icon">
                            <img src="images/cleaning.jpg" alt="Windows & fan">
                        </div>
                        <div class="service-option-text">Windows & fan</div>
                    </div>
'''

html = re.sub(r'<div class="service-grid-box">.*?</div>\s*</div>\s*</div>\s*<!-- Right Content', f'<div class="service-grid-box">{sidebar_html}</div>\n                </div>\n            </div>\n\n            <!-- Right Content', html, flags=re.DOTALL|re.IGNORECASE)

# Main sections
main_content = '''
            <!-- Default Banner -->
            <div id="default-banner" style="position: relative; border-radius: 16px; overflow: hidden; min-height: 450px; background: #000;">
                <img src="images/cleaning.jpg" alt="Living & Bedroom Banner" class="kitchen-banner-img" style="opacity: 0.6; height: 450px;">
                <div style="position: absolute; bottom: 120px; left: 30px;">
                    <h2 style="color: #fff; font-size: 36px; font-weight: 700;">No stain tough to clean</h2>
                </div>
            </div>

            <!-- Super Saver Deals Section -->
            <div id="super-saver" style="display: none; padding: 10px 0;">
                <h2 style="font-size: 28px; font-weight: 700; color: #0f172a; margin-bottom: 25px; line-height: 1.2;">Super saver deals</h2>
                
                <div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 30px; background: #2f4f4f; color: white; padding: 20px;">
                    <div style="background: #1e8f52; display: inline-block; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; margin-bottom: 15px;">20% OFF</div>
                    <h3 style="font-size: 22px; font-weight: 700; margin-bottom: 15px; max-width: 60%;">2-visits sofa cleaning pack</h3>
                    <div style="font-size: 14px;">Starts at <span style="text-decoration: line-through; margin-right: 5px;">₹398</span> <span style="font-size: 18px; font-weight: bold;">₹319</span> per visit</div>
                    <img src="images/cleaning.jpg" style="position: absolute; right: 0; bottom: 0; width: 40%; height: 100%; object-fit: cover; opacity: 0.8;" alt="Dog on sofa">
                </div>
            </div>
'''

html = re.sub(r'<!-- Default Banner -->.*?(?=\s*</div>\s*</div>\s*</main>)', main_content, html, flags=re.DOTALL)

js_code = '''
        function showSection(sectionId) {
            const allSections = [
                'default-banner', 'super-saver', 'cleaning-stain', 'sofa-carpet', 
                'curtain', 'living-care', 'bedroom-care', 'mattress-bed', 
                'dining-table', 'other-furniture', 'windows-fan'
            ];
            
            allSections.forEach(id => {
                const el = document.getElementById(id);
                if (el) el.style.display = 'none';
            });
            
            const targetSection = document.getElementById(sectionId);
            if (targetSection) targetSection.style.display = 'block';
        }
'''
html = re.sub(r'function showSection\(sectionId\) \{.*?\}', js_code, html, flags=re.DOTALL)

with open('living-bedroom.html', 'w', encoding='utf-8') as f:
    f.write(html)

import re

html_to_inject = """
            <!-- Cleaning & Stain Protection Section -->
            <div id="cleaning-stain" style="display: none; padding: 10px 0;">
                <h2 style="font-size: 28px; font-weight: 700; color: #0f172a; margin-bottom: 25px; line-height: 1.2;">Cleaning & stain protection</h2>
                
                <div style="padding-bottom: 30px; margin-bottom: 30px; border-bottom: 1px dashed #cbd5e1;">
                    <div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 15px; background: #eaddd3; height: 200px; display: flex; justify-content: center; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Sofa cleaning video" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.8;">
                        <div style="width: 50px; height: 50px; background: rgba(0,0,0,0.5); border-radius: 50%; display: flex; justify-content: center; align-items: center; cursor: pointer; z-index: 2;">
                            <i class="fa-solid fa-play" style="color: white; font-size: 20px; margin-left: 4px;"></i>
                        </div>
                    </div>
                    
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <div style="flex: 1; padding-right: 20px;">
                            <h3 style="font-size: 18px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Sofa cleaning & stain protection coating</h3>
                            <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                                <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                                <span style="font-weight: 500; color: #475569;">4.84</span>
                                <span style="text-decoration: underline dashed;">(56 reviews)</span>
                            </div>
                            <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                                Starts at ₹1,499 <span style="color: #475569; font-weight: 400;">• 45 mins</span>
                            </div>
                        </div>
                        <div>
                            <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 8px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">Add</button>
                        </div>
                    </div>
                    
                    <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                        <li>Nano-coating that repels spills & resists stains up to 12 months</li>
                        <li>Includes vacuuming & foam-based shampooing before coating</li>
                    </ul>
                    <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                </div>
            </div>

            <!-- Sofa & Carpet Section -->
            <div id="sofa-carpet" style="display: none; padding: 10px 0;">
                <h2 style="font-size: 28px; font-weight: 700; color: #0f172a; margin-bottom: 25px; line-height: 1.2;">Sofa & carpet</h2>
                
                <!-- Card 1 -->
                <div style="padding-bottom: 30px; margin-bottom: 30px; border-bottom: 1px dashed #cbd5e1; display: flex; justify-content: space-between;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 18px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Fabric sofa cleaning</h3>
                        <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                            <span style="font-weight: 500; color: #475569;">4.87</span>
                            <span style="text-decoration: underline dashed;">(261K reviews)</span>
                        </div>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            Starts at ₹399 <span style="color: #475569; font-weight: 400;">• 45 mins</span>
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Vacuuming & foam based shampooing for stain removal</li>
                            <li>Recliner is not included & to be booked separately</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="position: relative; width: 140px; height: 140px; border-radius: 12px; overflow: visible;">
                        <img src="images/cleaning.jpg" alt="Fabric sofa cleaning" style="width: 100%; height: 100%; object-fit: cover; border-radius: 12px;">
                        <button style="position: absolute; bottom: -15px; left: 50%; transform: translateX(-50%); background: #fff; color: #7c3aed; font-weight: 600; padding: 8px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.05); z-index: 2;">Add</button>
                    </div>
                </div>
                
                <!-- Card 2 -->
                <div style="padding-bottom: 30px; margin-bottom: 30px; border-bottom: 1px dashed #cbd5e1;">
                    <div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 15px; background: #eaddd3; height: 200px; display: flex; justify-content: center; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Sofa cleaning video" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.8;">
                        <div style="width: 50px; height: 50px; background: rgba(0,0,0,0.5); border-radius: 50%; display: flex; justify-content: center; align-items: center; cursor: pointer; z-index: 2;">
                            <i class="fa-solid fa-play" style="color: white; font-size: 20px; margin-left: 4px;"></i>
                        </div>
                    </div>
                    
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <div style="flex: 1; padding-right: 20px;">
                            <h3 style="font-size: 18px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Sofa cleaning & stain protection coating</h3>
                            <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                                <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                                <span style="font-weight: 500; color: #475569;">4.84</span>
                                <span style="text-decoration: underline dashed;">(56 reviews)</span>
                            </div>
                            <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                                Starts at ₹1,499 <span style="color: #475569; font-weight: 400;">• 45 mins</span>
                            </div>
                        </div>
                        <div>
                            <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 8px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">Add</button>
                        </div>
                    </div>
                    
                    <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                        <li>Nano-coating that repels spills & resists stains up to 12 months</li>
                        <li>Includes vacuuming & foam-based shampooing before coating</li>
                    </ul>
                    <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                </div>

                <!-- Card 3 -->
                <div style="padding-bottom: 30px; margin-bottom: 30px; border-bottom: 1px dashed #cbd5e1; display: flex; justify-content: space-between;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 18px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Leather sofa cleaning & polishing</h3>
                        <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                            <span style="font-weight: 500; color: #475569;">4.87</span>
                            <span style="text-decoration: underline dashed;">(60K reviews)</span>
                        </div>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            Starts at ₹399 <span style="color: #475569; font-weight: 400;">• 45 mins</span>
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Recliner is not included & to be booked separately</li>
                            <li>Leather moisturization to enhance appearance</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="position: relative; width: 140px; height: 140px; border-radius: 12px; overflow: visible;">
                        <img src="images/cleaning.jpg" alt="Leather sofa cleaning" style="width: 100%; height: 100%; object-fit: cover; border-radius: 12px;">
                        <button style="position: absolute; bottom: -15px; left: 50%; transform: translateX(-50%); background: #fff; color: #7c3aed; font-weight: 600; padding: 8px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.05); z-index: 2;">Add</button>
                    </div>
                </div>
                
                <!-- Card 4 -->
                <div style="padding-bottom: 30px; margin-bottom: 30px; border-bottom: 1px dashed #cbd5e1; display: flex; justify-content: space-between;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 18px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Sofa cum bed</h3>
                        <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                            <span style="font-weight: 500; color: #475569;">4.88</span>
                            <span style="text-decoration: underline dashed;">(58K reviews)</span>
                        </div>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            Starts at ₹399 <span style="color: #475569; font-weight: 400;">• 40 mins</span>
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Vacuuming & foam based shampooing for stain removal</li>
                            <li>Applying shiner to wooden surface for a fresh look</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="position: relative; width: 140px; height: 140px; border-radius: 12px; overflow: visible;">
                        <img src="images/cleaning.jpg" alt="Sofa cum bed" style="width: 100%; height: 100%; object-fit: cover; border-radius: 12px;">
                        <button style="position: absolute; bottom: -15px; left: 50%; transform: translateX(-50%); background: #fff; color: #7c3aed; font-weight: 600; padding: 8px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.05); z-index: 2;">Add</button>
                    </div>
                </div>
                
                <!-- Card 5 -->
                <div style="padding-bottom: 30px; margin-bottom: 30px; display: flex; justify-content: space-between;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 18px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Carpet cleaning</h3>
                        <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                            <span style="font-weight: 500; color: #475569;">4.83</span>
                            <span style="text-decoration: underline dashed;">(41K reviews)</span>
                        </div>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            Starts at ₹399 <span style="color: #475569; font-weight: 400;">• 45 mins</span>
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Vacuuming & foam based shampooing for stain removal</li>
                            <li>2-3 hrs of dry time under the fan</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="position: relative; width: 140px; height: 140px; border-radius: 12px; overflow: visible;">
                        <img src="images/cleaning.jpg" alt="Carpet cleaning" style="width: 100%; height: 100%; object-fit: cover; border-radius: 12px;">
                        <button style="position: absolute; bottom: -15px; left: 50%; transform: translateX(-50%); background: #fff; color: #7c3aed; font-weight: 600; padding: 8px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.05); z-index: 2;">Add</button>
                    </div>
                </div>
            </div>
"""

with open('living-bedroom.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the old injection if it was already injected
html = re.sub(r'<!-- Cleaning & Stain Protection Section -->.*?<!-- Card 5 -->.*?</div>\s*</div>', '', html, flags=re.DOTALL)

# Inject the new sections right after the super-saver section ends.
# Look for "<!-- Super Saver Deals Section --> ... </div>\n            </div>"
html = re.sub(
    r'(<!-- Super Saver Deals Section -->.*?</div>\s*</div>)', 
    r'\1\n\n' + html_to_inject, 
    html, 
    flags=re.DOTALL
)

with open('living-bedroom.html', 'w', encoding='utf-8') as f:
    f.write(html)

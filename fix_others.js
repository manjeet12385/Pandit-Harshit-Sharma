const fs = require('fs');
const files = ['services.html', 'gallery.html', 'contact.html'];
for (const file of files) {
  if (!fs.existsSync(file)) continue;
  let html = fs.readFileSync(file, 'utf-8');
  let imageCount = 0;
  html = html.replace(/<img([^>]+)>/g, (match, attrs) => {
    imageCount++;
    if (imageCount <= 2) return match; // skip logo/hero
    if (!attrs.includes('loading="lazy"')) {
      return `<img loading="lazy" ${attrs}>`;
    }
    return match;
  });
  fs.writeFileSync(file, html);
}
console.log('Fixed other html files');

const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf-8');
const images = html.match(/<img[^>]+>/g) || [];
console.log('Total images:', images.length);
console.log('Eager images:', images.filter(i => !i.includes('loading="lazy"')).length);

// Let's add lazy loading to all images except the first two
let newHtml = html;
let imageCount = 0;
newHtml = newHtml.replace(/<img([^>]+)>/g, (match, attrs) => {
  imageCount++;
  // Skip the first 2 images (logo and hero)
  if (imageCount <= 2) return match;
  if (!attrs.includes('loading="lazy"')) {
    return `<img loading="lazy" ${attrs}>`;
  }
  return match;
});
fs.writeFileSync('index.html', newHtml);
console.log('Added lazy loading to offscreen images in index.html');

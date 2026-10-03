const fs = require('fs');
const path = require('path');

const distPath = path.join(__dirname, 'dist');
const assetsPath = path.join(distPath, 'assets');

if (!fs.existsSync(distPath)) {
  console.log('dist directory not found.');
  process.exit(0);
}

// Find the CSS file in dist/assets
let cssContent = '';
if (fs.existsSync(assetsPath)) {
  const files = fs.readdirSync(assetsPath);
  const cssFile = files.find(f => f.endsWith('.css'));
  if (cssFile) {
    cssContent = fs.readFileSync(path.join(assetsPath, cssFile), 'utf-8');
  }
}

// Find LCP image in dist/assets
let lcpImageFile = '';
if (fs.existsSync(assetsPath)) {
  const files = fs.readdirSync(assetsPath);
  lcpImageFile = files.find(f => f.startsWith('image copy 5-') && f.endsWith('.webp'));
}

// Process all HTML files in dist
const processHtmlFiles = (dir) => {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      processHtmlFiles(fullPath);
    } else if (file.endsWith('.html')) {
      let html = fs.readFileSync(fullPath, 'utf-8');
      
      // 1. Inline CSS
      if (cssContent) {
        html = html.replace(/<link rel="stylesheet"[^>]*href="\/assets\/style-[^>]*\.css"[^>]*>/i, `<style>${cssContent}</style>`);
        html = html.replace(/<link[^>]*href="\/assets\/style-[^>]*\.css"[^>]*rel="stylesheet"[^>]*>/i, `<style>${cssContent}</style>`);
      }
      
      // 2. Preload LCP Image
      if (lcpImageFile && !html.includes(`rel="preload" as="image" href="/assets/${lcpImageFile}"`)) {
        html = html.replace('</head>', `\n<link rel="preload" as="image" href="/assets/${lcpImageFile}">\n</head>`);
      }

      // 3. Make Google Fonts Async
      html = html.replace(/<link href="https:\/\/fonts\.googleapis\.com\/css2\?[^"]+" rel="stylesheet">/g, (match) => {
        const urlMatch = match.match(/href="([^"]+)"/);
        if (urlMatch) {
          const url = urlMatch[1];
          return `<link rel="preload" as="style" href="${url}" onload="this.onload=null;this.rel='stylesheet'"><noscript><link rel="stylesheet" href="${url}"></noscript>`;
        }
        return match;
      });

      // 4. Lazy Load Google Translate Script
      const lazyTranslate = `
<script>
  window.addEventListener('load', function() {
    setTimeout(function() {
      var script = document.createElement('script');
      script.src = "//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit";
      document.body.appendChild(script);
    }, 3000);
  });
</script>`;
      html = html.replace(/<script type="text\/javascript" src="\/\/translate\.google\.com\/translate_a\/element\.js\?cb=googleTranslateElementInit" defer><\/script>/g, lazyTranslate);
      html = html.replace(/<script type="text\/javascript" src="\/\/translate\.google\.com\/translate_a\/element\.js\?cb=googleTranslateElementInit" defer=""><\/script>/g, lazyTranslate);

      fs.writeFileSync(fullPath, html);
    }
  }
};

processHtmlFiles(distPath);
console.log('Hardcore optimizations applied successfully.');

const https = require('https');
https.get('https://pandit-harshit-sharma.vercel.app/', (res) => {
  let data = '';
  res.on('data', (chunk) => { data += chunk; });
  res.on('end', () => {
    console.log('Has inline style block:', data.includes('<style>'));
    console.log('Has style.css link:', data.includes('rel="stylesheet" crossorigin href="/assets/style'));
    console.log('Has preload image:', data.includes('rel="preload" as="image"'));
    console.log('Has defer Google Translate:', data.includes('setTimeout(function() {'));
  });
});

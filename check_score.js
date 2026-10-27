const https = require('https');
const url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://pandit-harshit-sharma.vercel.app/&strategy=mobile';

https.get(url, (res) => {
  let data = '';
  res.on('data', (chunk) => { data += chunk; });
  res.on('end', () => {
    try {
      const j = JSON.parse(data);
      if (j.error) {
        console.log('Error:', j.error.message);
      } else {
        console.log('Score:', j.lighthouseResult.categories.performance.score * 100);
        console.log('FCP:', j.lighthouseResult.audits['first-contentful-paint'].displayValue);
        console.log('LCP:', j.lighthouseResult.audits['largest-contentful-paint'].displayValue);
        console.log('Speed Index:', j.lighthouseResult.audits['speed-index'].displayValue);
        console.log('TBT:', j.lighthouseResult.audits['total-blocking-time'].displayValue);
      }
    } catch (e) {
      console.log('Failed to parse:', e.message);
    }
  });
}).on('error', (e) => console.error(e));

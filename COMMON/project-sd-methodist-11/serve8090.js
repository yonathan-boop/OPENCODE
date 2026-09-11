const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname);
const PORT = 8090;
const RATE_WINDOW = 60 * 1000;
const RATE_MAX = 600;
const hits = new Map();
const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.json': 'application/json',
  '.webp': 'image/webp',
  '.pdf': 'application/pdf',
  '.txt': 'text/plain; charset=utf-8',
};

http.createServer((req, res) => {
  const ip = req.headers['cf-connecting-ip'] || (req.headers['x-forwarded-for'] || '').split(',')[0].trim() || req.socket.remoteAddress;
  const now = Date.now();
  const rec = hits.get(ip);
  if (rec) {
    if (now - rec.start >= RATE_WINDOW) {
      rec.start = now;
      rec.count = 1;
    } else {
      rec.count++;
    }
    if (rec.count > RATE_MAX) {
      res.writeHead(429, { 'Retry-After': Math.ceil((rec.start + RATE_WINDOW - now) / 1000) });
      res.end('429 Too Many Requests - coba lagi nanti');
      return;
    }
  } else {
    hits.set(ip, { start: now, count: 1 });
    if (hits.size > 5000) {
      for (const [k, v] of hits) if (now - v.start >= RATE_WINDOW) hits.delete(k);
    }
  }
  let p = decodeURIComponent(req.url.split('?')[0]);
  if (p === '/') p = '/index.html';
  let file = path.join(ROOT, p);
  fs.stat(file, (err, st) => {
    if (!err && st.isDirectory()) file = path.join(file, 'index.html');
    fs.readFile(file, (e, data) => {
      if (e) { res.writeHead(404); res.end('404 Not Found'); return; }
      const ext = path.extname(file).toLowerCase();
      res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
      res.end(data);
    });
  });
}).listen(PORT, '0.0.0.0', () => console.log(`Serving ${ROOT} on port ${PORT}`));

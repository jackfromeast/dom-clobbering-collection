## UMeditor

### Meta

+ Library: UMeditor
+ Stars: 1.4K
+ Version: v1.2.2
+ Fingerprint: `typeof window.UM !== 'undefined' && UM.hasOwnProperty('version')`
+ Payload: ```<a id="UMEDITOR_HOME_URL" href="https://xxx.xxx.xxx/"></a>```
+ Impact: XSS
+ Status: Reported
+ CVE: N/A
+ Foundby: TheHulk

### Library

https://github.com/fex-team/umeditor

Self hosted.

### Vulnerable Code Snippet

```javascript
var URL = window.UMEDITOR_HOME_URL || ...
```

```javascript
window.UMEDITOR_CONFIG = {

        //为编辑器实例添加一个路径，这个不能被注释
        UMEDITOR_HOME_URL : URL

        ...
```

## PoC

see ../domc-gadgets-assets/umeditor/poc.html

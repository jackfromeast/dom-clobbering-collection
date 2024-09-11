import('./answer.js')
  .then(module => {
    module.hello();
  })
  .catch(err => {
    console.error('Failed to load module', err);
  });

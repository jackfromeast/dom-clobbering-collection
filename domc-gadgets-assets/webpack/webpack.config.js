const path = require('path');

module.exports = {
  entry: './entry.js', // Ensure the correct path to your entry file
  output: {
    filename: 'webpack-gadgets.bundle.js', // Output bundle file
    path: path.resolve(__dirname, 'dist'), // Output directory
    // publicPath: '/dist/', // this line will make __webpack_require__.p = "/dist/";
  },
  target: 'web',
  mode: 'development',
  optimization: {
    splitChunks: {
      chunks: 'all', // This will create separate chunk files for dynamic imports
    },
  },
};

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
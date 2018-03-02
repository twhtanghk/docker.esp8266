HtmlWebpackPlugin = require 'html-webpack-plugin'
CompressionPlugin = require 'compression-webpack-plugin'

module.exports =
  node:
    fs: 'empty'
  entry:
    'js/test.js': './test/main.coffee'
  output:
    path: "#{__dirname}/../dist"
    filename: '[name]'
  plugins: [
    new CompressionPlugin
      test: /\.js$/
      deleteOriginalAssets: true
  ]
  module:
    rules: [
      { test: /\.vue$/, loader: 'vue-loader' }
      { test: /\.coffee$/, loader: 'coffee-loader' }
    ]

{defineConfig} = require '@vue/cli-service'

module.exports = defineConfig
  devServer:
    proxy:
      '^/':
        target: 'http://192.168.43.26'
        changeOrigin: true
        logLevel: 'debug'
  outputDir: '../python/dist'
  transpileDependencies: true
  lintOnSave: false
  css:
    loaderOptions:
      sass:
        implementation: require 'sass'
  chainWebpack: (config) ->
    config
      .plugin 'polyfills'
      .use require 'node-polyfill-webpack-plugin'
  configureWebpack:
    devtool: 'eval-cheap-source-map'

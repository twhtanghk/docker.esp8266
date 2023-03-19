{defineConfig} = require '@vue/cli-service'
{VuetifyPlugin} = require 'webpack-plugin-vuetify'

module.exports = defineConfig
  outputDir: '../python/dist'
  lintOnSave: false
  devServer:
    proxy:
      '^/':
        target: 'http://192.168.43.26'
        ws: false
  css:
    loaderOptions:
      sass:
        implementation: require 'sass'
  pluginOptions:
    compression:
      gzip:
        filename: '[file].gz[query]'
        algorithm: 'gzip'
        include: /\.(js|css|html|svg|json)(\?.*)?$/i
        minRatio: 0.8
        deleteOriginalAssets: true
  configureWebpack:
    plugins: [
      new VuetifyPlugin()
    ]

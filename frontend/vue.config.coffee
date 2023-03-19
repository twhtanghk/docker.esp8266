{defineConfig} = require '@vue/cli-service'

module.exports = defineConfig
  outputDir: '../python/dist'
  lintOnSave: false
  pwa:
    iconPaths:
      favicon16: 'img/icons/favicon-16x16.png'
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

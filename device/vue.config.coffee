_ = require 'lodash'
CompressionWebpackPlugin = require 'compression-webpack-plugin'

module.exports =
  baseUrl: './'
  lintOnSave: false
  devServer:
    host: '0.0.0.0'
    disableHostCheck: true
  configureWebpack: (config) ->
    config.plugins.push new CompressionWebpackPlugin
      deleteOriginalAssets: true
      include: [
        /\.ico$/
        /\.html$/
        /\.js$/
        /\.css$/
        /\.map$/
      ]
    config.module.rules.push
        test: /\.coffee$/
        use: ['babel-loader', 'coffee-loader']
    _.extend config.optimization, minimize: false
    return

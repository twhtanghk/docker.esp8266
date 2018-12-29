_ = require 'lodash'
webpack = require 'webpack'
CompressionWebpackPlugin = require 'compression-webpack-plugin'
process.env.VUE_APP_BASE_URL ?= '.'

module.exports =
  baseUrl: './'
  lintOnSave: false
  devServer:
    host: '0.0.0.0'
    disableHostCheck: true
  configureWebpack: (config) ->
    if process.env.NODE_ENV == 'production'
      config.plugins.push new CompressionWebpackPlugin
        deleteOriginalAssets: true
        include: [
          /\.eot$/
          /\.woff2$/
          /\.woff$/
          /\.ttf$/
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

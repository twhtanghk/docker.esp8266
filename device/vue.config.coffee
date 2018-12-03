_ = require 'lodash'
webpack = require 'webpack'

module.exports =
  baseUrl: './'
  configureWebpack: (config) ->
    config.module.rules
      .push
        test: /\.coffee$/
        use: ['babel-loader', 'coffee-loader']
    _.extend config.optimization, minimize: false
    return

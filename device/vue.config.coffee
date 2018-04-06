webpack = require 'webpack'

module.exports =
  configureWebpack: (config) ->
    config.output.publicPath = './'
    return

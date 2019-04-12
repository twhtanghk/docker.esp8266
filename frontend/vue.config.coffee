_ = require 'lodash'
{EnvironmentPlugin} = require 'webpack'
CompressionWebpackPlugin = require 'compression-webpack-plugin'

module.exports =
  publicPath: './'
  outputDir: './dist'
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
      process.env.API_URL = '.'
    config.plugins.push new EnvironmentPlugin [
      'API_URL'
    ]
    config.module.rules.push
        test: /\.coffee$/
        use: ['babel-loader', 'coffee-loader']
    return

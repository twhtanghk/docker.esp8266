path = require 'path'
webpack = require 'webpack'
UglifyJsPlugin = require 'uglifyjs-webpack-plugin'

module.exports =
  entry:
    index: ['./www/index.coffee']
  output:
    path: path.join __dirname, 'www'
    filename: "[name].js"
  plugins: [
    new webpack.DefinePlugin
      'process.env.NODE_ENV': JSON.stringify 'production'
    new UglifyJsPlugin()
  ]
  module:
    loaders: [
      {
        test: /\.scss$/
        use: [
          'style-loader'
          'css-loader'
          'sass-loader'
        ]
      }
      {
        test: /\.css$/
        use: [
          'style-loader'
          'css-loader'
        ]
      }
      {
        test: /\.coffee$/
        use: [
          {
            loader: 'babel-loader'
            query:
              plugins: [
                [
                  'transform-runtime'
                  {
                    helpers: false
                    polyfill: true
                    regenerator: true
                    moduleName: 'babel-runtime'
                  }
                ]
              ]
              presets: [
                'es2015'
                'stage-2'
              ]
          }
          {
            loader: 'coffee-loader'
            options:
              sourceMap: true
          }
        ]
      }
    ]
  devtool: "#source-map"

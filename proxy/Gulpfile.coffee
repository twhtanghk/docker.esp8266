gulp = require 'gulp'
gutil = require 'gulp-util'
concat = require 'gulp-concat'
uglify = require 'gulp-uglify'
rename = require 'gulp-rename'
sh = require 'shelljs'
stream = require 'stream'
path = require 'path'
fs = require 'fs'
browserify = require 'browserify'
source = require 'vinyl-source-stream'
streamify = require 'gulp-streamify'
htmlmin = require 'gulp-htmlmin'

gulp.task 'default', ->
  browserify 'index.coffee'
    .transform 'coffeeify'
    .on 'error', gutil.log
    .ignore 'assert'
    .ignore 'buffer'
    .ignore 'console'
    .ignore 'constants'
    .ignore 'crypto'
    .ignore 'domain'
    .ignore 'events'
    .ignore 'http'
    .ignore 'https'
    .ignore 'os'
    .ignore 'path'
    .ignore 'punycode'
    .ignore 'querystring'
    .ignore 'stream'
    .ignore 'string_decoder'
    .ignore 'timers'
    .ignore 'tty'
    .ignore 'url'
    .ignore 'util'
    .ignore 'vm'
    .ignore 'zlib'
    .bundle()
    .pipe source 'index.js'
    .pipe gulp.dest './dest'
    .pipe streamify uglify compress: false
    .pipe rename extname: '.min.js'
    .pipe gulp.dest './dest'
    .on 'finish', ->
      sh.exec 'echo "E.setBootCode(\'"$(cat dest/index.min.js)"\', true);" > dest/boot.js'

gulp.task 'static', ->
  class Template extends stream.Transform
    constructor: (opts = objectMode: true) ->
      super opts
    _transform: (data, encoding, cb) ->
      @push "\"/#{path.basename data.path}\": \"#{data.contents.toString('base64
')}\""
      cb()

  gulp
    .src 'static/*'
    .pipe htmlmin collapseWhitespace: true
    .pipe new Template()
    .pipe source 'static.coffee'
    .pipe gulp.dest '.'
   
gulp.task 'clean', ->
  sh.exec "rm -rf dest node_modules static.coffee"

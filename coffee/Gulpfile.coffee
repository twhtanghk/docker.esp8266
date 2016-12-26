gulp = require 'gulp'
coffee = require 'gulp-coffee'
gutil = require 'gulp-util'
concat = require 'gulp-concat'
uglify = require 'gulp-uglify'
rename = require 'gulp-rename'
sh = require 'shelljs'
stream = require 'stream'
path = require 'path'
htmlmin = require 'gulp-htmlmin'
Promise = require 'bluebird'
fs = require 'fs'
browserify = require 'browserify'
templateCache = require 'gulp-angular-templatecache'
source = require 'vinyl-source-stream'
streamify = require 'gulp-streamify'

gulp.task 'default', ->
  gulp
    .src [
      'templates.js'
      'lodash.coffee'
      'controller.coffee'
      'router.coffee'
      'app.coffee'
    ]
    .pipe coffee bare: true
    .on 'error', gutil.log
    .pipe concat 'index.js'
    .pipe gulp.dest './dest'
    .pipe uglify compress: false
    .pipe rename extname: '.min.js'
    .pipe gulp.dest './dest'
    .on 'finish', ->
      sh.exec 'echo "E.setBootCode(\'"$(cat dest/index.min.js)"\', true);" > dest/boot.js'

gulp.task 'templates', ['client.coffee'], ->
  class Template extends stream.Transform
    constructor: (opts = objectMode: true) ->
      super opts
    _transform: (data, encoding, cb) ->
      @push "\"/#{path.basename data.path}\": \"#{data.contents.toString().replace(/"/g, '\\"')}\""
      cb()
      
  streamStr = (readable) ->
    new Promise (resolve, reject) ->
      ret = ''
      readable.on 'data', (chunk) ->
        ret += chunk
      readable.on 'end', ->
        resolve ret
      
  html = gulp
    .src 'www/index.html'
    .pipe htmlmin collapseWhitespace: true

  js = gulp
    .src 'www/index.js'
    .pipe uglify compress: false

  Promise
    .map [html, js], (file) ->
      streamStr file.pipe new Template()
    .then (templates) ->
      fs
        .createWriteStream 'templates.js'
        .end "templates={#{templates.join(',')}};"

gulp.task 'client.templates', ->
  gulp
    .src 'www/templates/*.html'
    .pipe templateCache(root: 'templates', standalone: true)
    .pipe gulp.dest 'www/'


gulp.task 'client.coffee', ['client.templates'], ->
  browserify entries: 'www/index.coffee'
    .transform 'coffeeify'
    .bundle()
    .pipe source 'index.js'
    .pipe gulp.dest 'www/'
    .pipe streamify uglify compress: false
    .pipe rename extname: '.min.js'
    .pipe gulp.dest 'www/'

gulp.task 'clean', ->
  sh.exec "rm -rf dest templates.js www/index.js www/index.min.js www/templates.js"

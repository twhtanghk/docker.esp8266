gulp = require 'gulp'
coffee = require 'gulp-coffee'
gutil = require 'gulp-util'
concat = require 'gulp-concat'
uglify = require 'gulp-uglify'
rename = require 'gulp-rename'
sh = require 'shelljs'

gulp.task 'default', ->
  gulp
    .src ['rest.coffee']
    .pipe coffee bare: true
    .on('error', gutil.log)
    .pipe concat 'index.js'
    .pipe gulp.dest './dest'
    .pipe uglify compress: false
    .pipe rename extname: '.min.js'
    .pipe gulp.dest './dest'
    .on 'finish', ->
      sh.exec 'echo "E.setBootCode(\'"$(cat dest/index.min.js)"\', true);" > dest/boot.js'

gulp.task 'clean', ->
  sh.exec "rm -rf dest"

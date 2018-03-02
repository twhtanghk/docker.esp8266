URL = 'http://192.168.43.99'

mocha.setup 
  ui: 'bdd'
  timeout: 0

qs = require 'querystring'

global.expect = require('chai').expect
global.opts = (obj = {}) ->
  obj['content-type'] = 'application/x-www-form-urlencoded'
  if 'body' of obj
    obj.body = qs.stringify obj.body
  obj
global.ok = (res) ->
  expect res.status
    .to.equal 200

require '../src/model.vue'
require './10-static.coffee'
require './20-ap.coffee'
require './30-sta.coffee'
require './40-pwm.coffee'
require './60-sys.coffee'

mocha.run()

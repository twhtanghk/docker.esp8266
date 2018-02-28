URL = 'http://192.168.43.99'
delay = 8000

mocha.setup 
  ui: 'bdd'
  timeout: delay + 1000

expect = require('chai').expect
qs = require 'querystring'

global.opts = (obj = {}) ->
  obj['content-type'] = 'application/x-www-form-urlencoded'
  if body of obj
    obj.body = qs.stringify obj.body
  obj
global.ok = (res) ->
  expect res.status
    .to.equal 200

beforeEach ->
  Promise = require 'bluebird'
  Promise.delay delay

require './10-static.coffee'
require './20-ap.coffee'
require './30-sta.coffee'
require './40-pwm.coffee'
require './60-sys.coffee'

mocha.run()

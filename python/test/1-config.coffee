req = require 'supertest'
_ = require 'lodash'
Promise = require 'bluebird'

describe 'config', ->
  read = ->
    req process.env.SERVER
      .get '/config/'
      .expect 200
      .then ({body}) ->
        console.log body

  it 'factory', ->
    req process.env.SERVER
      .get '/config/factory' 
      .expect 200
      .then ({body}) ->
        console.log body

  it 'reset', ->
    req process.env.SERVER
      .get '/config/reset'
      .timeout 10000

  it 'get', ->
    read()

  it 'put', ->
    req process.env.SERVER
      .put '/config/'
      .expect 200
      .set 'Content-Type', 'application/json'
      .send _.extend require('../config.json').factory,
        ap:
          essid: 'test'
          password: '87654321'
      .expect 200
      .then ({body}) ->
        console.log body

  it 'get', ->
    read() 

req = require 'supertest'
_ = require 'lodash'
Promise = require 'bluebird'

describe 'config', ->
  it 'factory', ->
    req process.env.SERVER
      .get '/config/factory' 
      .expect 200
      .then ({body}) ->
        console.log body

  it 'reset', ->
    req process.env.SERVER
      .get '/config/reset'
      .timeout 15000

  it 'get', ->
    req process.env.SERVER
      .get '/config/'
      .expect 200
      .then ({body}) ->
        console.log body

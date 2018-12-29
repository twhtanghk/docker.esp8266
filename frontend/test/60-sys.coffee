require('dotenv').config path: './.env.development'
req = require 'supertest'

describe 'config', ->
  it 'GET /cfg', ->
    req process.env.VUE_APP_BASE_URL
      .get '/cfg'
      .send()
      .then (res) ->
        console.log res.body

  it 'GET /cfg/factory', ->
    req process.env.VUE_APP_BASE_URL
      .get '/cfg/factory'
      .send()
      .then (res) ->
        console.log res.body

  it 'GET /cfg/reset', ->
    req process.env.VUE_APP_BASE_URL
      .get '/cfg/reset'
      .send()
      .then (res) ->
        console.log res.body

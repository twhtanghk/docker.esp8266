require('dotenv').config path: './.env.development'
req = require 'supertest'

describe 'sta', ->
  it 'GET /sta', ->
    req process.env.VUE_APP_BASE_URL
      .get '/sta'
      .send()
      .then (res) ->
        console.log res.body

  it 'PUT /sta', ->
    req process.env.VUE_APP_BASE_URL
      .put '/sta'
      .set 'Content-Type', 'application/x-www-form-urlencoded'
      .send
        essid: 'Testing'
        password: '12345678'
      .then (res) ->
        console.log res.body

  it 'GET /sta/scan', ->
    req process.env.VUE_APP_BASE_URL
      .get '/sta/scan'
      .send()
      .then (res) ->
        console.log res.body

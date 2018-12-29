require('dotenv').config path: './.env.development'
req = require 'supertest'

describe 'pwm', ->
  it 'GET /pwm', ->
    req process.env.VUE_APP_BASE_URL
      .get '/pwm'
      .send()
      .then (res) ->
        console.log res.body

  it 'GET /pwm/fan', ->
    req process.env.VUE_APP_BASE_URL
      .get '/pwm/fan'
      .send()
      .then (res) ->
        console.log res.body

  it 'PUT /pwm/fan', ->
    req process.env.VUE_APP_BASE_URL
      .put '/pwm/fan'
      .set 'Content-Type', 'application/x-www-form-urlencoded'
      .send
        pin: 12
        default: 600
      .then (res) ->
        console.log res.body

  it 'PUT /pwm/fan/duty', ->
    req process.env.VUE_APP_BASE_URL
      .put '/pwm/fan/duty'
      .set 'Content-Type', 'application/x-www-form-urlencoded'
      .send
        value: 0
      .then (res) ->
        console.log res.body

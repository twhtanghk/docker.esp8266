require('dotenv').config path: './.env.development'
req = require 'supertest'

describe 'ap', ->
  it 'GET /ap', ->
    req process.env.VUE_APP_BASE_URL
      .get '/ap'
      .send()
      .expect 200
      .then (res) ->
        console.log res.body

  it 'PUT /ap set essid and password', ->
    req process.env.VUE_APP_BASE_URL
      .put '/ap'
      .set 'Content-Type', 'application/x-www-form-urlencoded'
      .send
        essid: 'Testing'
        password: '12345678'
      .then (res) ->
        console.log res.body

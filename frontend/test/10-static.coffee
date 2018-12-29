require('dotenv').config path: './.env.development'
req = require 'supertest'

describe 'static', ->
  it 'GET /index.html', ->
    req process.env.VUE_APP_BASE_URL
      .get '/index.html'
      .send()
      .expect 200

req = require 'supertest'

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
      .expect 200
###
  it 'get', ->
    req process.env.SERVER
      .get '/config/'
      .expect 200
      .then ({body}) ->
        console.log body

  it 'put', ->
    req process.env.SERVER
      .put '/config/'
      .expect 200
      .set 'Content-Type', 'application/json'
      .send
        ap:
          essid: 'test'
          password: '87654321'
      .expect 200
      .then ({body}) ->
        console.log body
###

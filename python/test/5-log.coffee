req = require 'supertest'

describe 'syslog', ->
  url = process.env.SERVER

  it 'config', ->
    req url
      .get '/log/'
      .expect 200
      .then ({body}) ->
        console.log body

  it 'update', ->
    req url
      .put '/log/'
      .set 'Content-Type', 'application/json'
      .send ip: '192.168.4.2', port: 8888
      .expect 200
      .then ({body}) ->
        console.log body

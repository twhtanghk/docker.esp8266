req = require 'supertest'

describe 'ap', ->
  url = process.env.SERVER

  it 'get config', ->
    req url
      .get '/ap/'
      .expect 200
      .then ({body}) ->
        console.log body

  it 'set essid and password', ->
    req url
      .put '/ap/'
      .set 'Content-Type', 'application/json'
      .send essid: 'switch1', password: '87654321'
      .expect 200
      .then ({body}) ->
        console.log body

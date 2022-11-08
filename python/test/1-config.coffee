req = require 'supertest'

describe 'config', ->
  it 'factory', ->
    req process.env.SERVER
      .get '/config/factory' 
      .expect(200)
      .then ({body}) ->
        console.log body

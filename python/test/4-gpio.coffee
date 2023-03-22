req = require 'supertest'

describe 'gpio', ->
  url = process.env.SERVER

  it 'get config', ->
    req url
      .get '/gpio/'
      .expect 200
      .then ({body}) ->
        console.log body

  it 'switch on', ->
    req url
      .put '/gpio/switch/on'
      .expect 200
      .then ({body}) ->
        console.log body

  it 'switch off', ->
    req url
      .put '/gpio/switch/off'
      .expect 200
      .then ({body}) ->
        console.log body

  it 'get switch state', ->
    req url
      .get '/gpio/switch'
      .expect 200
      .then ({body}) ->
        console.log body

  it 'get all switch state', ->
    req url
      .get '/gpio/all'
      .expect 200
      .then ({body}) ->
        console.log body

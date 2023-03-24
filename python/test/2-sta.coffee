req = require 'supertest'

describe 'sta', ->
  url = process.env.SERVER

  it 'get config', ->
    req url
      .get '/sta/'
      .expect 200
      .then ({body}) ->
        console.log body

  it 'set dhcp_hostname', ->
    req url
      .put '/sta/'
      .set 'Content-Type', 'application/json'
      .send name: 'test'
      .expect 200
      .then ({body}) ->
        console.log body

  it 'wifi scan', ->
    req url
      .get '/sta/scan'
      .expect 200
      .then ({body}) ->
        console.log body

  it 'connect ap', ->
    req url
      .put '/sta/'
      .set 'Content-Type', 'application/json'
      .send
        ssid: 'TomMobile'
        passwd: process.env.PASSWD
      .expect 200

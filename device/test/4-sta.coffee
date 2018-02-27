describe 'sta', ->
  it 'GET /sta', ->
    req
      .get '/sta'
      .expect 200

  it 'PUT /sta', ->
    req
      .put '/sta'
      .field 'essid', 'Testing'
      .field 'password', 'Testing'
      .expect 200

  it 'GET /sta/scan', ->
    req
      .get '/sta/scan'
      .expect 200

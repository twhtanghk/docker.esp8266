describe 'ap', ->
  it 'GET /ap', ->
    req
      .get '/ap'
      .expect 200

  it 'PUT /ap', ->
    req
      .put '/ap'
      .field 'essid', 'Testing'
      .field 'password', 'Testing'
      .expect 200

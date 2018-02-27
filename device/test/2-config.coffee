describe 'config', ->
  it 'GET /cfg', ->
    req
      .get '/cfg'
      .expect 200

  it 'GET /cfg/reset', ->
    req
      .get '/cfg/reset'
      .expect 200

  it 'GET /cfg/factory', ->
    req
      .get '/cfg/factory'
      .expect 200

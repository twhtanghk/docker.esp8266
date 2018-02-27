describe 'pwm', ->
  it 'GET /pwm', ->
    req
      .get '/pwm'
      .expect 200

  it 'GET /pwm/fan', ->
    req
      .get '/pwm/fan'
      .expect 200

  it 'PUT /pwm/fan', ->
    req
      .put '/pwm/fan'
      .field 'pin', 12
      .field 'default', 600
      .expect 200

  it 'PUT /pwm/fan/duty', ->
    req
      .put '/pwm/fan/duty'
      .field 'value', 0
      .expect 200

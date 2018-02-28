describe 'pwm', ->
  it 'GET /pwm', ->
    fetch '/pwm'
      .then ok

  it 'GET /pwm/fan', ->
    fetch '/pwm/fan'
      .then ok

  it 'PUT /pwm/fan', ->
    data = opts
      method: 'PUT'
      body:
        pin: 12
        default: 600
    fetch '/pwm/fan', data
      .then ok

  it 'PUT /pwm/fan/duty', ->
    data = opts
      method: 'PUT'
      body:
        value: 0
    fetch '/pwm/fan/duty', data
      .then ok

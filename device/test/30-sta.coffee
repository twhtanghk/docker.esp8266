describe 'sta', ->
  it 'GET /sta', ->
    fetch '/sta'
      .then ok

  it 'PUT /sta', ->
    data = opts
      method: 'PUT'
      body:
        essid: 'Testing'
        password: 'Testing'
    fetch '/sta', data
      .then ok

  it 'GET /sta/scan', ->
    fetch '/sta/scan'
      .then ok

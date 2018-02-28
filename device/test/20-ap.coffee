describe 'ap', ->
  it 'GET /ap', ->
    fetch '/ap'
      .then ok

  it 'PUT /ap', ->
    data = opts
      method: 'PUT'
      body:
        essid: 'Testing'
        password: 'Testing'
    fetch '/ap', data
      .then ok

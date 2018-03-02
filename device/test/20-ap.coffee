describe 'ap', ->
  it 'GET /ap', ->
    fetch '/ap'
      .then ok

  it 'PUT /ap check min password length', ->
    data = opts
      method: 'PUT'
      body:
        essid: 'Testing'
        password: 'Testing'
    fetch '/ap', data
      .then (res) ->
        res.json()
      .then (res) ->
        expect res
          .to.equal 'password min length 8'

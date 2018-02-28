describe 'config', ->
  it 'GET /cfg', ->
    fetch '/cfg'
      .then ok

  it 'GET /cfg/factory', ->
    fetch '/cfg/factory'
      .then ok

  it 'GET /cfg/reset', ->
    fetch '/cfg/reset'
      .then ok

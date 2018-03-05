describe 'static', ->
  it 'GET /static/js/test.js', ->
    fetch '/static/js/test.js'
      .then ok

describe 'static', ->
  it 'GET /static/js/app.js', ->
    fetch '/static/js/test.js'
      .then ok

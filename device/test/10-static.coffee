describe 'static', ->
  it 'GET /static/js/app.js', ->
    fetch '/static/js/app.js'
      .then ok

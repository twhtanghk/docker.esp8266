describe 'static', ->
  it 'GET /static/js/app.js', ->
    req
      .get '/static/js/app.js'
      .expect 200

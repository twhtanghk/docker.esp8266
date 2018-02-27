before ->
  if 'URL' of process.env
    global.req = require('supertest')(process.env.URL)
  else
    throw new Error 'process.env.URL not defined'

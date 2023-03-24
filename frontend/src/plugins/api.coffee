_ = require 'lodash'
{Model} = require('model').default

class API extends Model
  constructor: (opts = {}) ->
    super opts
    @mw = [
      ({req, res}) => @json {req, res}
      ({req, res}) => @req {req, res}
      ({req, res}) => @res {req, res}
      ({req, res}) => @error {req, res}
    ]
    
class GPIO extends API
  constructor: (opts = {}) ->
    super _.defaults opts, baseUrl: '/gpio'

class STA extends API
  constructor: (opts = {}) ->
    super _.defaults opts, baseUrl: '/sta'

class AP extends API
  constructor: (opts = {}) ->
    super _.defaults opts, baseUrl: '/ap'

class CFG extends API
  constructor: (opts = {}) ->
    super _.defaults opts, baseUrl: '/config'

cfg = new CFG()
ap = new AP()
sta = new STA()
gpio = new GPIO()

export {cfg, ap, sta, gpio}
export default {cfg, ap, sta, gpio}

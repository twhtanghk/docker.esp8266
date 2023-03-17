_ = require 'lodash'
{Model} = require('model').default

class GPIO extends Model
  constructor: (opts = {}) ->
    super _.defaults opts, baseUrl: '/gpio'

class STA extends Model
  constructor: (opts = {}) ->
    super _.defaults opts, baseUrl: '/sta'

class AP extends Model
  constructor: (opts = {}) ->
    super _.defaults opts, baseUrl: '/ap'

class CFG extends Model
  constructor: (opts = {}) ->
    super _.defaults opts, baseUrl: '/cfg'

cfg = new CFG()
ap = new AP()
sta = new STA()
gpio = new GPIO()

export {cfg, ap, sta, gpio}
export default {cfg, ap, sta, gpio}

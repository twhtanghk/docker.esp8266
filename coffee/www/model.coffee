require 'angular-activerecord'

serverUrl = 'http://192.168.0.101'

angular

  .module 'model', ['ActiveRecord']

  .factory 'resource', (ActiveRecord, $http) ->
    class Model extends ActiveRecord
      constructor: (data, opts) ->
        super data, opts
    
    class Sys extends Model
      $urlRoot: "#{serverUrl}/sys"

    class AP extends Model
      $urlRoot: "#{serverUrl}/ap"

    class STA extends Model
      $urlRoot: "#{serverUrl}/sta"

    Sys: Sys
    AP: AP
    STA: STA

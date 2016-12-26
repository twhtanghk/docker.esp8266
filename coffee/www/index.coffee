require './templates'
require './model.coffee'

angular

  .module 'app', ['ionic', 'model']

  .controller 'statusCtrl', ($scope, $log, resource) ->
    resource.Sys
      .fetchOne 'status'
      .then (model) ->
        $scope.model = model
      .catch $log.error

  .controller 'apCtrl', ($scope, $log, resource) ->
    resource.Sys
      .fetchOne 'ap'
      .then (model) ->
        $scope.model = model
      .catch $log.error

  .controller 'staCtrl', ($scope, $log, resource) ->
    resource.Sys
      .fetchOne 'sta'
      .then (model) ->
        $scope.model = model
      .catch $log.error


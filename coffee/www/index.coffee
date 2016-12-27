require './templates'
require './model.coffee'
require 'angular-xeditable'

angular

  .module 'app', ['ionic', 'model', 'xeditable']

  .run (editableOptions) ->
    editableOptions.theme = 'bs3'

  .controller 'statusCtrl', ($scope, $log, resource) ->
    resource.Sys
      .fetchOne 'info'
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


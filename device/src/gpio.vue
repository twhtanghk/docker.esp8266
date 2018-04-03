<template>
</template>

<script lang='coffee'>
model = require './model'

url = (name = null) ->
  if name?
    "/gpio/#{name}"
  else
    '/gpio'

module.exports =
  components:
    card: require('./card').default
    formCol: require('./form').default
    field: require('./field').default
  props: [
    'name'
  ]
  data: ->
    value: 0
  methods:
    on: ->
      model
        .put "#{url(@name)}", {value: 1}
        .catch console.error
    off: ->
      model
        .put "#{url(@name)}", {value: 2}
        .catch console.error
    list: ->
      model
        .get "#{url(@name)}"
        .then (res) ->
          @value = res.value
        .catch console.error
</script>

<template>
  <div id='gpio'>
    <label class='checkbox' v-for='item in gpio' :key='item.name'>
      <toggle v-model='item.value' :options='{on: 1, off:0}' @change='set(item)' />
      {{ item.name }}
    </label>
  </div>
</template>

<script lang='coffee'>
model = require './model'

url = (name = null) ->
  root = '/gpio'
  if name?
    root = "#{root}/#{name}"
  return root

module.exports =
  components:
    toggle: require('vue-bootstrap-toggle').default
  data: ->
    gpio: []
  methods:
    set: (item) ->
      {name, value} = item
      model
        .put "#{url(name)}", {value: value}
        .catch console.error
    list: ->
      model
        .get "#{url()}"
        .then (res) ->
          res.json()
        .then (res) =>
          @gpio = res
        .catch console.error
  created: ->
    @list()
</script>

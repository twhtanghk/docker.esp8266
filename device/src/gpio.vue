<template>
  <div id='gpio'>
    <toggle-button class='toggle' v-for='item in gpio' :key='item.name' :value='item.value' :labels='labels(item)' :height='30' :width='100' @change='set($event, item)' :color='color' />
  </div>
</template>

<script lang='coffee'>
model = require './model'
Vue = require('vue').default
Vue.use require('vue-js-toggle-button').default

url = (name = null) ->
  root = '/gpio'
  if name?
    root = "#{root}/#{name}"
  return root

module.exports =
  data: ->
    gpio: []
    color: '#007bff'
  methods:
    labels: (item) ->
      checked: "#{item.name} On"
      unchecked: "#{item.name} Off"
    set: ({value, srcEvent}, item) ->
      model
        .put "#{url(item.name)}", {value: value}
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

<style lang='scss' scoped>
.toggle {
  font-size: 14px !important;
}
</style>

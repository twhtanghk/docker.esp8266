<template>
  <div id='gpio'>
    <model ref='gpio' baseUrl='/gpio' />
    <toggle-button class='toggle' v-for='item in gpio' :key='item.name' :value='item.value' :labels='labels(item)' :height='30' :width='100' @change='set($event, item)' :color='color' />
  </div>
</template>

<script lang='coffee'>
Vue = require('vue').default
Vue.use require('vue-js-toggle-button').default

url = (name = null) ->
  root = '/gpio'
  if name?
    root = "#{root}/#{name}"
  return root

module.exports =
  components:
    model: require('./model').default
  data: ->
    gpio: []
    color: '#007bff'
  methods:
    labels: (item) ->
      checked: "#{item.name} On"
      unchecked: "#{item.name} Off"
    set: ({value, srcEvent}, item) ->
      @$refs.gpio
        .update item.name,
          data:
            value: value
        .catch console.error
    list: ->
      @refs.gpio
        .list()
        .then (res) =>
          @gpio = res
        .catch console.error
  mounted: ->
    @list()
</script>

<style lang='scss' scoped>
.toggle {
  font-size: 14px !important;
}
</style>

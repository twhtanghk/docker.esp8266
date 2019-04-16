<template>
  <div id='gpio'>
    <v-switch v-for='item in gpio' :key='item.name' v-model='item.value' :label='labels(item)' @change='set(item)' />
  </div>
</template>

<script lang='coffee'>
{gpio} = require('./model').default

export default
  data: ->
    gpio: []
  methods:
    labels: (item) ->
      "#{item.name} #{if item.value then 'Off' else 'On'}"
    set: (item) ->
      gpio
        .update
          data:
            id: item.name
            value: if item.value then 1 else 0
        .catch console.error
    list: ->
      gpio
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

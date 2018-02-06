<template>
  <div class='panel-body'>
    <vue-form-generator :schema='schema' :model='model' :options='opts'>
    </vue-form-generator>
  </div>
</template>

<script lang='coffee'>
module.exports =
  data: ->
    essidList: []
    model:
      host: ''
      essid: ''
      password: ''
    schema:
      fields: [
        { type: 'input', inputType: 'text', label: 'host', model: 'host' }
        { type: 'select', label: 'essid', model: 'essid', values: [] }
        { type: 'input', inputType: 'password', label: 'password', model: 'password' }
      ]
    opts:
      validateAfterLoad: true
      validateAfterChanged: true
  beforeCreate: ->
    url =
      host: 'http://192.168.4.1/wlan/sta'
      essid: 'http://192.168.4.1/wlan/sta/scan'
    fetch url.host
      .then (res) =>
        @model.host = res.body
      .catch (err) =>
        @model.host = err
    fetch url.essid
      .then (res) =>
        @essidList = res.body
      .catch console.error
</script>

<style lang='scss' scoped>
  div.panel-body {
    margin-top: 1em;
    margin-bottom: 1em;
  }
</style>

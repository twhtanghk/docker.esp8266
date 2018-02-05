<template>
  <div class='panel-body'>
    <vue-form-generator :schema='schema' :model='model' :options='opts'>
    </vue-form-generator>
  </div>
</template>

<script lang='coffee'>
module.exports =
  data: ->
    model:
      host: 'host'
    schema:
      fields: [
        { type: 'input', inputType: 'text', label: 'host', model: 'host' }
      ]
    opts:
      validateAfterLoad: true
      validateAfterChanged: true
</script>

<style lang='scss'>
</style>

<template>
  <b-container fluid>
    <sta></sta>
    <hr/>
  </b-container>
</template>

<script lang='coffee'>
sta = require('./sta').default

module.exports =
  components:
    sta: sta
</script>

<style lang='scss'>
</style>

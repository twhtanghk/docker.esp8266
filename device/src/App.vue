<template>
  <b-tabs>
    <b-tab title='net' active>
      <net/>
    </b-tab>
    <b-tab title='pwm'>
      <pwm/>     
    </b-tab>
  </b-tabs>
</template>

<script lang='coffee'>
Vue = require('vue').default
console.error = (msg) ->
  Vue.toasted.error msg, duration: 5000
pwm = require('./pwm').default
net = require('./net').default

module.exports =
  components:
    net: net
    pwm: pwm
</script>

<style lang='scss'>
@import '~bootstrap/scss/bootstrap.scss';
@import 'vue-toasted/dist/vue-toasted.min.css';
</style>

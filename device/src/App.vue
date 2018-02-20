<template>
  <b-tabs>
    <b-tab title='AP' active>
      <ap/>
    </b-tab>
    <b-tab title='STA'>
      <sta/>
    </b-tab>
    <b-tab title='PWM'>
      <pwm/>     
    </b-tab>
  </b-tabs>
</template>

<script lang='coffee'>
Vue = require('vue').default
console.error = (msg) ->
  Vue.toasted.error msg, duration: 5000
console.info = (msg) ->
  Vue.toasted.info msg, duration: 5000
pwm = require('./pwm').default
ap = require('./ap').default
sta = require('./sta').default

module.exports =
  components:
    ap: ap
    sta: sta
    pwm: pwm
</script>

<style lang='scss'>
@import 'app.scss';
@import 'vue-toasted/dist/vue-toasted.min.css';
</style>

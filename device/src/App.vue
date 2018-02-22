<template>
  <b-tabs @input='select($event)'>
    <b-tab title='AP' active>
      <div id='ap' />
    </b-tab>
    <b-tab title='STA'>
      <div id='sta' />
    </b-tab>
    <b-tab title='PWM'>
      <div id='pwm' />
    </b-tab>
  </b-tabs>
</template>

<script lang='coffee'>
Vue = require('vue').default
error = console.error
console.error = (msg) ->
  error msg
  Vue.toasted.error msg, duration: 5000
info = console.info
console.info = (msg) ->
  info msg
  Vue.toasted.info msg, duration: 5000
AP = Vue.extend require('./ap').default
STA = Vue.extend require('./sta').default
PWM = Vue.extend require('./pwm').default

module.exports =
  methods:
    select: (tabIndex) ->
      component = @$children[0].$children[tabIndex]
      id = component.$el.id
      switch tabIndex
        when 0
          new AP el: "#ap"
        when 1
          new STA el: "#sta"
        when 2
          new PWM el: "#pwm"
</script>

<style lang='scss'>
@import 'app.scss';
@import 'vue-toasted/dist/vue-toasted.min.css';
</style>

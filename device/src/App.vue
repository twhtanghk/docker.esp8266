<template>
  <b-tabs @input='select($event)'>
    <b-tab title='AP' active>
      <div id='ap' />
    </b-tab>
    <b-tab title='STA'>
      <div id='sta' />
    </b-tab>
    <b-tab title='DDNS'>
      <div id='ddns' />
    </b-tab>
    <b-tab title='GPIO'>
      <div id='gpio' />
    </b-tab>
    <b-tab title='PWM'>
      <div id='pwm' />
    </b-tab>
  </b-tabs>
</template>

<script lang='coffee'>
require './app.scss'
require 'vue-toasted/dist/vue-toasted.min.css'

Vue = require('vue').default
Vue.use require('bootstrap-vue').default
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
DDNS = Vue.extend require('./ddns').default
GPIO = Vue.extend require('./gpio').default
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
          new DDNS el: "#ddns"
        when 3
          new GPIO el: "#gpio"
        when 4
          new PWM 
            el: "#pwm"
            propsData:
              name: 'fan'
</script>

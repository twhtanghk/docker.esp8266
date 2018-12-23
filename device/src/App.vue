<template>
  <v-app>
    <toolbar />
    <v-container fluid>
      <router-view />
    </v-container>
  </v-app>
</template>

<script lang='coffee'>
require './app.scss'
require 'vue-toasted/dist/vue-toasted.min.css'

Vue = require('vue').default
Vue.use require 'vuetify'
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

export default {}
</script>

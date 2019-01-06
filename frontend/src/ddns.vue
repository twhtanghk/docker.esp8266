<template>
  <v-layout row wrap>
    <card header='Settings'>
      <v-text-field v-model='url' label='URL' disabled />
      <v-text-field v-model='interval' label='Interval' disabled />
      <v-text-field v-model='host' label='Hostname' />
      <v-text-field v-model='user' label='Username' />
      <v-text-field v-model='pass' label='Password' />
      <v-switch v-model='enable' label='Enbale' />
      <v-btn color="primary" @click='save'>Save</v-btn>
    </card>
  </v-layout>
</template>

<script lang='coffee'>
{ddns} = require('./model').default

export default
  components:
    card: require('./card').default
  data: ->
    url: ''
    interval: 0
    host: ''
    user: ''
    pass: ''
    enable: false
  methods:
    get: ->
      ddns.get()
        .then (res) =>
          @url = res.url
          @interval = res.interval
          @host = res.host
          @user = res.user
          @enable = res.enable
        .catch console.error
    save: ->
      ddns
        .put data: _.pick @, 'url', 'interval', 'host', 'user', 'pass', 'enable'
        .catch console.error
  created: ->
    @get()
</script>

<template>
  <v-layout row wrap>
    <card header='Settings'>
      <v-text-field v-model='ip' label='IP' />
      <v-text-field v-model='port' label='Port' />
      <v-switch v-model='active' label='Enable' />
      <v-btn color="primary" @click='save'>Save</v-btn>
    </card>
  </v-layout>
</template>

<script lang='coffee'>
{pick} = require 'lodash'
{syslog} = require('./model').default
{required, ipAddress, integer} = require 'vuelidate/lib/validators'

export default
  components:
    card: require('./card').default
  data: ->
    ip: '192.168.0.105'
    port: 541
    active: false
  validations:
    ip: {required, ipAddress}
    port: {integer}
  methods:
    get: ->
      try
        {@ip, @port, @active} = await syslog.get()
      catch err
        console.error err
    save: ->
      try
        data = _.pick @, 'ip', 'port', 'active'
        {@ip, @port, @active} = await syslog.put {data}
      catch err
        console.error err
  created: ->
    @get()
</script>

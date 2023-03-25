<template>
  <v-layout row wrap>
    <card :header='"Syslog " + ip + ":" + port'>
      <v-text-field v-model='ip' label='IP' required
        :error-messages='v$.ip.$errors.map(e => e.$message)'
        @input='v$.ip.$touch'
        @blur='v$.ip.$touch'
      />
      <v-text-field v-model='port' label='Port'
        :error-messages='v$.port.$errors.map(e => e.$message)'
        @input='v$.port.$touch'
        @blur='v$.port.$touch'
      />
      <v-btn color="primary" @click='save'>Save</v-btn>
    </card>
  </v-layout>
</template>

<script lang='coffee'>
import card from './card'
import {syslog} from './plugins/api'
import {useVuelidate} from '@vuelidate/core'
import {required, ipAddress, integer} from 'vuelidate/validators'

export default
  setup: ->
    v$: useVuelidate()
  components: {card}
  data: ->
    ip: '192.168.4.2'
    port: 8888
  validations:
    ip: {required, ipAddress}
    port: {integer}
  methods:
    get: ->
      {@ip, @port} = await syslog.get url: '/log/'
    save: ->
      await syslog.put url: '/log/', data: {@ip, @port}
  created: ->
    @get()
</script>

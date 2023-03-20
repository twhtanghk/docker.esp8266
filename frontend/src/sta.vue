<template>
  <card :header='"Internet " + status'>
    <v-select v-model='ssid' label='ESSID' :items='list' filled />
    <v-text-field v-model='password' label='Password' type='password' required />
    <v-btn color="primary" @click='connect(essid, password)'>Connect</v-btn>
    <v-btn color="secondary" @click='getList()'>Scan</v-btn>
  </card>
</template>

<script lang='coffee'>
import {sta} from './plugins/api'
import card from './card'
import {useVuelidate} from '@vuelidate/core'
import {required, minLength} from '@vuelidate/validators'

export default
  setup: ->
    v$: useVuelidate()
  components: {card}
  data: ->
    config: {}
    ssid: ''
    list: []
    password: ''
  validations:
    essid:
      required: required
    password:
      required: required
      minLength: minLength(8) 
  computed:
    status: ->
      if @config.isconnected then JSON.stringify(@config.curr) else ''
  methods:
    getStatus: ->
      {@config, @essid} = await sta.get()
    connect: (essid, passwd) ->
      await sta.put data: {ssid, passwd}
      await @getStatus()
    getList: ->
      res = await sta.get url: "#{sta.baseUrl}/scan"
      @list = []
      for i in res.sort()
        @list.push
          value: i
          text: i
  mounted: ->
    @getStatus()
    @getList()
</script>

<template>
  <card :header='"Station " + status'>
    <v-select v-model='ssid' label='ESSID' :items='list' item-title='text' item-value='value' filled required
      :error-messages='v$.ssid.$errors.map(e => e.$message)'
      @input='v$.ssid.$touch'
      @blur='v$.ssid.$touch'
    />
    <v-text-field v-model='passwd' label='Password' type='password' required
      :error-messages='v$.passwd.$errors.map(e => e.$message)'
      @input='v$.passwd.$touch'
      @blur='v$.passwd.$touch'
    />
    <v-btn color="primary" @click='connect(ssid, passwd)'>Connect</v-btn>
    <v-btn @click='getList()'>Scan</v-btn>
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
    list: []
    ssid: ''
    passwd: ''
  validations: ->
    ssid:
      required: required
    passwd:
      required: required
      minLength: minLength(8) 
  computed:
    status: ->
      {curr} = @config
      if @config.isconnected then "(#{curr[0]}/#{curr[2]})" else ''
  methods:
    getStatus: ->
      @config = await sta.get url: '/sta/'
    connect: (ssid, passwd) ->
      await sta.put 
        url: '/sta/'
        body: JSON.stringify {ssid, passwd}
      await @getStatus()
    getList: ->
      res = await sta.get url: '/sta/scan'
      @list = []
      for i in res.sort()
        @list.push
          value: i
          text: i
  mounted: ->
    @getStatus()
    @getList()
</script>

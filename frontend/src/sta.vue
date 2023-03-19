<template>
  <card :header='"Internet " + status'>
    <v-select v-model='essid' label='ESSID' :items='list' filled />
    <v-text-field v-model='password' label='Password' type='password' required />
    <v-btn color="primary" @click='connect(essid, password)'>Connect</v-btn>
    <v-btn color="secondary" @click='getList()'>Scan</v-btn>
  </card>
</template>

<script lang='coffee'>
import sta from './plugins/api'
import card from './card'
import {useVuelidate} from '@vuelidate/core'
import {required, minLength} from '@vuelidate/validators'

export default
  setup: ->
    v$: useVuelidate()
  components: {card}
  data: ->
    config: {}
    essid: ''
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
      sta.get()
        .then (res) =>
          @config = res
          @essid = res.essid
        .catch console.error
    connect: (essid, passwd) ->
      sta
        .put 
          data:
            ssid: essid
            password: passwd
        .then =>
          @getStatus()
        .catch console.error
    getList: ->
      sta
        .get url: "#{sta.baseUrl}/scan"
        .then (res) =>
          @list = []
          for i in res.sort()
            @list.push
              value: i
              text: i
      .catch console.error
  mounted: ->
    @getStatus()
    @getList()
</script>

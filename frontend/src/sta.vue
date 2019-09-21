<template>
  <card :header='"Internet " + status'>
    <v-select v-model='essid' label='ESSID' :items='list' filled :rules='[required($v.essid)]'/>
    <v-text-field v-model='password' label='Password' type='password' :rules='[required($v.password), minLength($v.password)]' required />
    <v-btn color="primary" @click='connect(essid, password)'>Connect</v-btn>
    <v-btn color="secondary" @click='getList()'>Scan</v-btn>
  </card>
</template>

<script lang='coffee'>
{sta} = require('./model').default
{required, minLength} = require 'vuelidate/lib/validators'
rule = require('jsOAuth2/frontend/src/rule').default

export default
  components:
    card: require('./card').default
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
    required: rule.required
    minLength: rule.minLength
  mounted: ->
    @getStatus()
    @getList()
</script>

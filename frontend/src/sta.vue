<template>
  <v-layout row wrap>
    <card header='Status'>
      <v-text-field v-model='isconnected' label='Connected' disabled />
      <v-text-field v-model='JSON.stringify(config)' label='Config' disabled />
      <v-btn color="primary" @click='getStatus()'>Refresh</v-btn>
    </card>

    <card header='Host'>
      <v-text-field v-model='host' label='Hostname' required />
      <v-btn color='primary' @click='setHost(host)'>Save</v-btn>
    </card>

    <card header='Settings'>
      <v-select v-model='essid' label='ESSID' :items='list' filled />
      <v-text-field v-model='password' label='Password' type='password' />
      <v-btn color="primary" @click='connect(essid, password)'>Connect</v-btn>
      <v-btn color="secondary" @click='getList()'>Scan</v-btn>
    </card>
  </v-layout>
</template>

<script lang='coffee'>
{sta} = require('./model').default

export default
  components:
    card: require('./card').default
  data: ->
    isconnected: false
    config: {}
    host: ''
    essid: ''
    list: []
    password: ''
  methods:
    getStatus: ->
      sta.get()
        .then (res) =>
          @isconnected = res.isconnected
          @config = res.curr
          @host = res.dhcp_hostname
        .catch console.error
    setHost: (val) ->
      sta
        .put
          data:
            name: val
        .then (res) ->
          console.info 'updated successfully'
        .catch console.error
    connect: (essid, passwd) ->
      sta
        .put 
          data:
            ssid: essid
            password: passwd
        .then ->
          console.info 'connecting to specified essid'
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

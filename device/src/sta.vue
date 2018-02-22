<template>
  <b-container fluid id='sta'>
    <b-container fluid>
      <b-row>
        <div class='col-lg'>
          <label>isconnected: {{isconnected}}</label>
        </div>
        <div class='col-lg'>
          <label>config: {{config}}</label>
        </div>
      </b-row>
      <div class='action'>
        <b-button variant="primary" @click='getStatus()'>Refresh</b-button>
      </div>
    </b-container>

    <div>
      <b-form-group label='host'>
        <b-input-group>
          <b-form-input v-model='host' type='text' />
          <b-input-group-append>
            <b-btn variant='primary' @click='setHost(host)'>Update</b-btn>
          </b-input-group-append>
        </b-input-group>
      </b-form-group>
    </div>

    <div>
      <b-form-group label='essid'>
        <b-form-select v-model='essid' :options='list' />
      </b-form-group>
      <b-form-group label='password'>
        <b-form-input v-model='password' type='password' />
      </b-form-group>
      <div class='action'>
        <b-button variant="primary" @click='connect(essid, password)'>Connect</b-button>
        <b-button variant="secondary" @click='getList()'>Scan</b-button>
      </div>
    </div>
  </b-container>
</template>

<script lang='coffee'>
model = require './model'

url =
  host: '/wlan/sta'
  essid: '/wlan/sta/scan'

module.exports =
  data: ->
    host: ''
    essid: ''
    list: []
    password: ''
  methods:
    getStatus: ->
      model.get url.host
        .then (res) ->
          res.json()
        .then (res) =>
          @isconnected = res.isconnected
          @config = res.curr
          @host = res.dhcp_hostname
        .catch console.error
    setHost: (val) ->
      model.put url.host, name: val
        .then (res) ->
          console.info 'updated successfully'
        .catch console.error
    connect: (essid, passwd) ->
      model
        .put url.host, {ssid: essid, passwd: passwd}
        .then ->
          console.info 'connecting to specified essid'
        .catch console.error
    getList: ->
      fetch url.essid
        .then (res) ->
          res.json()
        .then (res) =>
          @list = []
          for i in res.sort()
            @list.push
              value: i
              text: i
      .catch console.error
  created: ->
    @getStatus()
      .then =>
        @getList()
</script>

<style lang='scss'>
</style>

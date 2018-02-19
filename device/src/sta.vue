<template>
  <div id='sta'>
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
      <b-form-group>
        <label :for='password'>password</label>
        <b-form-input id='password' v-model='password' type='password' />
      </b-form-group>
      <div class='action'>
        <b-button variant="primary" @click='connect(essid, password)'>Connect</b-button>
        <b-button variant="secondary" @click='getList()'>Scan</b-button>
      </div>
    </div>
  </div>
</template>

<script lang='coffee'>
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
    opts: (method, params) ->
      data = new URLSearchParams()
      for k, v of params
        data.set k, v
      method: method
      body: data
      headers:
        'Content-Type': 'application/x-www-form-urlencoded'
    getStatus: ->
      fetch url.host
        .then (res) ->
          if res.status != 200
            throw new Error res.statusText
          res.json()
        .then (res) =>
          @isconnected = res.isconnected
          @config = res.curr
          @host = res.dhcp_hostname
        .catch console.error
    setHost: (val) ->
      fetch url.host, @opts('PUT', name: val)
        .then (res) ->
          if res.status != 200
            throw new Error res.statusText
        .catch console.error
    connect: (essid, passwd) ->
      fetch url.host, @opts('PUT', {ssid: essid, passwd: passwd})
        .then (res) ->
          if res.status != 200
            throw new Error res.statusText
        .catch console.error
    getList: ->
      fetch url.essid
        .then (res) ->
          if res.status != 200
            throw new Error res.statusText
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
    @getList()
</script>

<style lang='scss'>
@import '~bootstrap/scss/bootstrap.scss';

#sta {
  > div {
    @extend .border;
    @extend .border-dark;
    @extend .rounded;
    margin-top: 10px;
    padding: 5px;
  }
}
div.action {
  text-align: right;
}
</style>

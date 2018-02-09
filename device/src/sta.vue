<template>
  <div id='sta'>
    <b-form-group label='host'>
      <b-input-group>
        <b-form-input v-model='host' type='text' />
        <b-input-group-append>
          <b-btn variant='primary' @click='setHost(host)'>Update</b-btn>
        </b-input-group-append>
      </b-input-group>
    </b-form-group>
    <hr>
    <b-form>
      <b-form-group label='essid'>
        <b-form-select v-model='essid' :options='list' />
      </b-form-group>
      <b-form-group>
      <label :for='password'>password</label>
      <b-form-input id='password' v-model='password' type='password' />
      </b-form-group>
      <div class='action'>
        <b-button type="submit" variant="primary">Connect</b-button>
        <b-button @click='getList()' variant="secnodary">Scan</b-button>
      </div>
    </b-form>
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
    getHost: ->
      fetch url.host
        .then (res) ->
          if res.status != 200
            throw new Error res.statusText
          res.json()
        .then (res) =>
          @host = res.dhcp_hostname
        .catch console.error
    setHost: (val) ->
      data = new URLSearchParams()
      data.set 'name', val
      opts =
        method: 'PUT'
        body: data
        headers:
          'Content-Type': 'application/x-www-form-urlencoded'
      fetch url.host, opts
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
    @getHost()
    @getList()
</script>

<style lang='scss' scoped>
#sta {
  margin: 10px 10px 0 0;
}
div.action {
  text-align: right;
}
</style>

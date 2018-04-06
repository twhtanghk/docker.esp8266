<template>
  <div id='sta'>
    <model ref='sta' baseUrl='/sta' />
    <card header='Status'>
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
    </card>

    <card header='Host'>
      <form-col>
        <div slot='fields'>
          <field name='name'>
            <b-form-input v-model='host' type='text' />
          </field>
        </div>
        <div slot='buttons' class='action'>
          <b-button variant='primary' @click='setHost(host)'>Save</b-button>
        </div>
      </form-col>
    </card>

    <card header='Settings'>
      <form-col>
        <div slot='fields'>
          <field name='essid'>
            <b-form-select v-model='essid' :options='list' />
          </field>
          <field name='password'>
            <b-form-input v-model='password' type='password' />
          </field>
        </div>
        <div slot='buttons' class='action'>
          <b-button variant="primary" @click='connect(essid, password)'>Connect</b-button>
          <b-button variant="secondary" @click='getList()'>Scan</b-button>
        </div>
      </form-col>
    </card>
  </div>
</template>

<script lang='coffee'>
module.exports =
  components:
    model: require('./model').default
    card: require('./card').default
    formCol: require('./form').default
    field: require('./field').default
  data: ->
    isconnected: false
    config: {}
    host: ''
    essid: ''
    list: []
    password: ''
  methods:
    getStatus: ->
      @$refs.sta.get()
        .then (res) =>
          @isconnected = res.isconnected
          @config = res.curr
          @host = res.dhcp_hostname
        .catch console.error
    setHost: (val) ->
      @$refs.sta
        .put
          data:
            name: val
        .then (res) ->
          console.info 'updated successfully'
        .catch console.error
    connect: (essid, passwd) ->
      @$refs.sta
        .put 
          data:
            ssid: essid
            passwd: passwd
        .then ->
          console.info 'connecting to specified essid'
        .catch console.error
    getList: ->
      @$refs.sta
        .read 'scan'
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

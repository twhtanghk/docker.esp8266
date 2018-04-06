<template>
  <div id='ap'>
    <model ref='ap' baseUrl='/ap' />
    <model ref='cfg' baseUrl='/cfg' />
    <card header='Settings'>
      <form-col>
        <div slot='fields'>
          <field name='essid'>
            <b-form-input v-model='essid' type='text' required />
          </field>
          <field name='password'>
            <b-form-input v-model='password' type='password' data-minlength='8' required />
          </field>
          <field name='authmode'>
            <b-form-input v-model='authmode' type='text' disabled />
          </field>
        </div>
        <div slot='buttons' class='action'>
          <b-button variant="primary" @click='save(essid, password)'>Save</b-button>
        </div>
      </form-col>
    </card>
    <card header='System'>
      <div class='action'>
        <b-button variant="primary" @click='reset()'>Restart</b-button>
        <b-button variant="primary" @click='factory()'>Factory Config</b-button>
      </div>
    </card>
  </div>
</template>

<script lang='coffee'>
model = require './model'
url = 
  ap: '/ap'
  reset: '/cfg/reset'
  factory: '/cfg/factory'

module.exports =
  components:
    model: require('./model').default
    card: require('./card').default
    formCol: require('./form').default
    field: require('./field').default
  data: ->
    essid: ''
    password: ''
    authmode: ''
  methods:
    getStatus: ->
      @$refs.ap.list()
        .then (res) =>
          @essid = res.essid
          @authmode = res.authmode
        .catch console.error
    save: (essid, password) ->
      @$refs.ap
        .put
          data:
            essid: essid
            password: password
        .then ->
          console.info 'saved successfully'
        .catch console.error
    reset: ->
      @$refs.cfg
        .read 'reset'
        .then ->
          console.info 'reset in progress'
        .catch console.error
    factory: ->
      @$refs.cfg
        .read 'factory'
        .then (res) =>
          @essid = res.essid
          @authmode = res.authmode
        .catch console.error
  mounted: ->
    @getStatus()
</script>

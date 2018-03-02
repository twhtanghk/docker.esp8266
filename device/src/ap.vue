<template>
  <div id='ap'>
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
    card: require('./card').default
    formCol: require('./form').default
    field: require('./field').default
  data: ->
    essid: ''
    password: ''
    authmode: ''
  methods:
    getStatus: ->
      model
        .get url.ap
        .then (res) ->
          res.json()
        .then (res) =>
          @essid = res.essid
          @authmode = res.authmode
        .catch console.error
    save: (essid, password) ->
      model
        .put url.ap, {essid: essid, password: password}
        .then ->
          console.info 'saved successfully'
        .catch console.error
    reset: ->
      model
        .get url.reset
        .then ->
          console.info 'reset in progress'
        .catch console.error
    factory: ->
      model
        .get url.factory
        .then (res) ->
          res.json()
        .then (res) =>
          @essid = res.essid
          @authmode = res.authmode
        .catch console.error
  created: ->
    @getStatus()
</script>

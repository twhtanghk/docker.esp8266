<template>
  <b-container fluid id='ap'>
    <b-container fluid>
      <b-form-group label='essid'>
        <b-form-input v-model='essid' type='text' required />
      </b-form-group>
      <b-form-group label='password'>
        <b-form-input v-model='password' type='password' data-minlength='8' required />
      </b-form-group>
      <b-form-group label='authmode'>
        <b-form-input v-model='authmode' type='text' disabled />
      </b-form-group>
      <div class='action'>
        <b-button variant="primary" @click='save(essid, password)'>Save</b-button>
      </div>
    </b-container>
    <b-container>
      <div class='action'>
        <b-button variant="primary" @click='reset()'>Restart</b-button>
        <b-button variant="primary" @click='factory()'>Factory Config</b-button>
      </div>
    </b-container>
  </b-container>
</template>

<script lang='coffee'>
model = require './model'
url = 
  ap: '/wlan/ap'
  reset: '/cfg/reset'
  factory: '/cfg/factory'

module.exports =
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
        .then ->
          console.info 'restored successfully'
        .catch console.error
  created: ->
    @getStatus()
</script>

<style lang='scss'>
</style>

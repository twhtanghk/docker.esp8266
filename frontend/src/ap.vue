<template>
  <v-layout row wrap>
    <card header='Settings'>
      <v-text-field v-model='essid' label='ESSID' required />
      <v-text-field v-model='password' label='Password' type='password' v-validate="'min:8'" required />
      <v-text-field v-model='authmode' label='Auth Mode' disabled />
      <v-btn color='primary' @click='save(essid, password)'>Save</v-btn>
    </card>

    <card header='System'>
      <v-btn color="primary" @click='reset()'>Restart</v-btn>
      <v-btn color="primary" @click='factory()'>Factory Config</v-btn>
    </card>
  </v-layout>
</template>

<script lang='coffee'>
{ap, cfg} = require('./model').default

export default
  components:
    card: require('./card').default
  data: ->
    essid: ''
    password: ''
    authmode: ''
  methods:
    getStatus: ->
      ap.get()
        .then (res) =>
          @essid = res.essid
          @authmode = res.authmode
        .catch console.error
    save: (essid, password) ->
      ap
        .put
          data:
            essid: essid
            password: password
        .then ->
          console.info 'saved successfully'
        .catch console.error
    reset: ->
      cfg
        .get url: "#{cfg.baseUrl}/reset"
        .then ->
          console.info 'reset in progress'
        .catch console.error
    factory: ->
      cfg
        .get url: "#{cfg.baseUrl}/factory"
        .then (res) =>
          @essid = res.essid
          @authmode = res.authmode
        .catch console.error
  mounted: ->
    @getStatus()
</script>

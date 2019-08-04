<template>
  <v-layout row wrap>
    <card header='Access Point'>
      <v-text-field v-model='essid' label='ESSID' :rules='[required($v.essid)]' required />
      <v-text-field v-model='password' label='Password' type='password' :rules='[required($v.password), minLength($v.password)]' required />
      <v-text-field v-model='passwordAgain' label='Confirm password' type='password' :rules='[required($v.passwordAgain), minLength($v.passwordAgain)]' required />
      <v-btn color='primary' @click='save(essid, password)' :disabled='$v.$invalid'>Save</v-btn>
    </card>

    <card header='System'>
      <v-btn color="primary" @click='reset()'>Restart</v-btn>
      <v-btn color="primary" @click='factory()'>Factory Config</v-btn>
    </card>
  </v-layout>
</template>

<script lang='coffee'>
{ap, cfg} = require('./model').default
{required, minLength} = require 'vuelidate/lib/validators'
rule = require('jsOAuth2/frontend/src/rule').default

export default
  components:
    card: require('./card').default
  data: ->
    essid: ''
    password: ''
    passwordAgain: ''
  validations:
    essid:
      required: required
    password:
      required: required
      minLength: minLength(8)
    passwordAgain:
      required: required
      minLength: minLength(8)
  methods:
    getStatus: ->
      ap.get()
        .then (res) =>
          @essid = res.essid
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
    required: rule.required
    minLength: rule.minLength
  mounted: ->
    @getStatus()
</script>

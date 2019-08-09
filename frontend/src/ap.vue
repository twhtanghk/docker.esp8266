<template>
  <card header='Access Point'>
    <v-text-field v-model='essid' label='ESSID' :rules='[required($v.essid)]' required />
    <v-text-field v-model='password' label='Password' type='password' :rules='[required($v.password), minLength($v.password)]' required />
    <v-text-field v-model='passwordAgain' label='Confirm password' type='password' :rules='[required($v.passwordAgain), minLength($v.passwordAgain), match($v.password, $v.passwordAgain)]' required />
    <v-btn color='primary' @click='save(essid, password)' :disabled='$v.$invalid'>Save</v-btn>
  </card>
</template>

<script lang='coffee'>
{ap} = require('./model').default
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
    required: rule.required
    minLength: rule.minLength
    match: rule.match
  mounted: ->
    @getStatus()
</script>

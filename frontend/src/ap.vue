<template>
  <card header='Wifi Config'>
    <v-text-field v-model='essid' label='ESSID' required />
    <v-text-field v-model='password' label='Password' type='password' required />
    <v-text-field v-model='passwordAgain' label='Confirm password' type='password' required />
    <v-btn color='primary' @click='save(essid, password)' :disabled='v$.$invalid'>Save</v-btn>
  </card>
</template>

<script lang='coffee'>
import {useVuelidate} from '@vuelidate/core'
import {required, sameAs, minLength} from '@vuelidate/validators' 
import ap from './plugins/api'
import card from './card'

export default
  setup: ->
    v$: useVuelidate()
  components: {card}
  data: ->
    essid: ''
    password: ''
    passwordAgain: ''
  validations: ->
    essid:
      required: required
    password:
      required: required
      minLength: minLength 8
    passwordAgain:
      sameAs: sameAs @password
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
  mounted: ->
    @getStatus()
</script>

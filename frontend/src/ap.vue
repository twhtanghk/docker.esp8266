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
import {ap} from './plugins/api'
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
      {@essid} = await ap.get()
    save: (essid, password) ->
      await ap.put data: {essid, password}
  mounted: ->
    await @getStatus()
</script>

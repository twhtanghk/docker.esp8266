<template>
  <card header='Access Point'>
    <v-text-field v-model='essid' label='ESSID' required
      :error-messages='v$.essid.$errors.map(e => e.$message)'
      @input='v$.essid.$touch'
      @blur='v$.essid.$touch'
    />
    <v-text-field v-model='password' label='Password' type='password' required 
      :error-messages='v$.password.$errors.map(e => e.$message)'
      @input='v$.password.$touch'
      @blur='v$.password.$touch'
    />
    <v-text-field v-model='passwordAgain' label='Confirm password' 
      type='password' required
      :error-messages='v$.passwordAgain.$errors.map(e => e.$message)'
      @input='v$.passwordAgain.$touch'
      @blur='v$.passwordAgain.$touch'
    />
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
      {@essid} = await ap.get url: '/ap/'
    save: (essid, password) ->
      await ap.put 
        url: '/ap/'
        body: JSON.stringify {essid, password}
  mounted: ->
    await @getStatus()
</script>

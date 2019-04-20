<template>
  <v-layout row wrap>
    <card header='Current Duty'>
      <v-slider
        :label="name"
        v-model="value"
        :max="1023"
        :min="0"
        @change='setDuty(value)'/>
    </card>

    <card header='Settings'>
      <v-text-field v-model='name' label='Name' required />
      <v-text-field v-model='pin' label='Pin' required />
      <v-text-field v-model='init' label='Default' required />
      <v-btn color="primary" @click='save(pin, init)'>Save</v-btn>
    </card>
  </v-layout>
</template>

<script lang='coffee'>
{pwm} = require('./model').default
{required, integer, minValue, maxValue} = require 'vuelidate/lib/validators'

export default
  components:
    card: require('./card').default
  data: ->
    name: 'fan'
    pin: 0
    init: 0
    value: 0
  validations:
    init: {required, minValue: minValue(0), maxValue: maxValue(1023)}
    value: {required, minValue: minValue(0), maxValue: maxValue(1023)}
  methods:
    save: (pin, init) ->
      try
        await pwm.update
          url: "#{pwm.baseUrl}/#{@name}"
          data:
            pin: pin
            default: @init
      catch err
        console.error err
    setDuty: (val) ->
      try
        await pwm.update
          url: "#{pwm.baseUrl}/#{@name}/duty"
          data:
            value: val
      catch err
        console.error err
    list: ->
      pwm
        .get()
        .then (res) =>
          @pin = res[@name].pin
          @init = res[@name].default
          @value = res[@name].value
        .catch console.error
  mounted: ->
    @list()
</script>

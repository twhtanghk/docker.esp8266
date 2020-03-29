<template>
  <v-layout row wrap>
    <card header='Current Duty'>
      <v-slider
        :label="label(pin, value)"
        v-model="value"
        :max="1024"
        :min="0"
        @change='duty(pin, value)'/>
    </card>
  </v-layout>
</template>

<script lang='coffee'>
{Pwm} = require('./plugins/model.coffee').default
import {required, integer, minValue, maxValue} from 'vuelidate/lib/validators'

export default
  components:
    card: require('./card').default
  data: ->
    pin: 2
    value: 0
  validations:
    value: {required, minValue: minValue(0), maxValue: maxValue(1024)}
  methods:
    label: (pin, value) ->
      "Pin #{pin} (#{value})"
    duty: (pin, value) ->
      try
        await Pwm.update
          data:
            id: @pin
            duty: @value
      catch err
        console.error err
    getDuty: (val) ->
      try
        @value = await Pwm.read
          data:
            id: @pin
      catch err
        console.error err
  mounted: ->
    await @getDuty()
</script>

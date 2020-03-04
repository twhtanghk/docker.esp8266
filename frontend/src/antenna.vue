<template>
  <v-layout row wrap>
    <card header='Heading'>
      <v-slider
        label="Boat"
        v-model="boat"
        thumb-label='always'
        thumb-color='red'
        :max="359"
        :min="0"
        @change='updateBoat()'/>
      <v-slider
        label="Antenna"
        v-model="antenna"
        thumb-label='always'
        thumb-color='red'
        :max="359"
        :min="0"
        @change='updateAntenna()'/>
      <v-btn color='primary' @click='stepback'>Stepback</v-btn>
    </card>
  </v-layout>
</template>

<script lang='coffee'>
{Model} = require('model').default
{required, integer, minValue, maxValue} = require 'vuelidate/lib/validators'

model = new Model baseUrl: "#{process.env.API_URL}"

export default
  components:
    card: require('./card').default
  data: ->
    boat: 0
    antenna: 0
  validations:
    boat: {required, minValue: minValue(0), maxValue: maxValue(359)}
  methods:
    updateBoat: ->
      try
        await model.put url: "#{process.env.API_URL}/heading/boat/#{@boat}"
      catch err
        console.error err
    updateAntenna: ->
      try
        await model.put url: "#{process.env.API_URL}/heading/antenna/#{@antenna}"
      catch err
        console.error err
    stepback: ->
      try
        await model.put url: "#{process.env.API_URL}/antenna/stepback"
      catch err
        console.error err
</script>

<template>
  <b-container fluid id='pwm'>
    <div>
      <b-row>
        <b-col>
          <b-form-group label='fan'>
            <b-form-input type='number' v-bind='attrs' v-model='value' @change='setValue($event)' />
          </b-form-group>
        </b-col>
        <b-col>
          <b-form-input type='range' v-bind='attrs' v-model='value' @change='setValue($event)'>
          </b-form-input>
        </b-col>
      </b-row>
    </div>
  </b-container>
</template>

<script lang='coffee'>
model = require './model'

url = '/pwm'

module.exports =
  name: 'pwm'
  data: ->
    attrs:
      required: true
      min: 0
      max: 1024
    value: 0
  methods:
    setValue: (val) ->
      @value = val
      if @value > @attrs.max
        @value = @attrs.max
      if @value < @attrs.min
        @value = @attrs.min
      model
        .put url, {device: 'fan', value: @value}
        .catch console.error
    getValue: ->
      model
        .get url
        .then (res) ->
          res.json()
        .then (res) ->
          @value = res.fan.value
        .catch console.error
  created: ->
    @getValue()
</script>

<style lang='scss'>
</style>

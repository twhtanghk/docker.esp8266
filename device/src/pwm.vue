<template>
  <b-container fluid id='pwm'>
    <div>
      <b-row>
        <b-col cols='3'>
          <b-form-input type='number' v-bind='attrs' v-model='value' @change='refresh($event)'>
          </b-form-input>
        </b-col>
        <b-col cols='9'>
          <b-form-input type='range' v-bind='attrs' v-model='value' @change='refresh($event)'>
          </b-form-input>
        </b-col>
      </b-row>
    </div>
  </b-container>
</template>

<script lang='coffee'>
module.exports =
  name: 'pwm'
  data: ->
    attrs:
      required: true
      min: 0
      max: 1024
    value: 500
  methods:
    refresh: (val) ->
      @value = val
      if @value > @attrs.max
        @value = @attrs.max
      if @value < @attrs.min
        @value = @attrs.min
</script>

<style lang='scss'>
</style>

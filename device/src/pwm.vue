<template>
  <div id='pwm' :name='name'>
    <card header='Current Duty'>
      <b-row>
        <b-col cols='4'>
          <b-form-input type='number' v-bind='attrs' v-model='value' @change='setValue($event)' />
        </b-col>
          <b-col cols='8'>
            <b-form-input type='range' v-bind='attrs' v-model='value' @change='setValue($event)' />
          </b-col>
      </b-row>
    </card>

    <card header='Settings'>
      <form-col>
        <div slot='fields'>
          <field name='pin'>
            <b-form-input type='number' v-model='pin' />
          </field>
          <field name='default'>
            <b-form-input type='number' v-bind='attrs' v-model='init' @change='init = valid($event)' />
          </field>
        </div>
        <div slot='buttons' class='action'>
          <b-button variant="primary" @click='save(pin, init)'>Save</b-button>
        </div>
      </form-col>
    </card>
  </div>
</template>

<script lang='coffee'>
model = require './model'

url = '/pwm'

module.exports =
  components:
    card: require('./card').default
    formCol: require('./form').default
    field: require('./field').default
  props: [
    'name'
  ]
  data: ->
    attrs:
      required: true
      min: 0
      max: 1024
    pin: 0
    init: 0
    value: 0
  methods:
    valid: (val) ->
      if val > @attrs.max
        val = @attrs.max
      if val < @attrs.min
        val = @attrs.min
      return val
    save: (pin, init) ->
      @init = @valid init
      model
        .put url, {device: @name, pin: pin, default: @init}
        .catch console.error
    setValue: (val) ->
      @value = @valid val
      model
        .put url, {device: @name, value: @value}
        .catch console.error
    getValue: ->
      model
        .get url
        .then (res) ->
          res.json()
        .then (res) =>
          @pin = res[@name].pin
          @init = res[@name].default
          @value = res[@name].value
        .catch console.error
  created: ->
    @getValue()
</script>

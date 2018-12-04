<template>
  <div id='pwm' :name='name'>
    <card header='Current Duty'>
      <b-row>
        <b-col cols='4'>
          <b-form-input type='number' v-bind='attrs' v-model='value' @change='setDuty($event)' />
        </b-col>
          <b-col cols='8'>
            <b-form-input type='range' v-bind='attrs' v-model='value' @change='setDuty($event)' />
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
{pwm} = require('./model').default

export default
  components:
    model: require('./model').default
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
      max: 1023
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
      pwm
        .update @name, 
          data:
            pin: pin
            default: @init
        .catch console.error
    setDuty: (val) ->
      @value = @valid val
      pwm
        .update "#{@name}/duty",
          data:
            value: @value
        .catch console.error
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

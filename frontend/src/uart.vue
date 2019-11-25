<template>
  <v-layout row wrap>
    <card header='UART'>
      <v-select label="Baudrate" v-model="baudrate" :items="opts.baudrate"/>
      <v-select label="Bits" v-model="bits" :items="opts.bits"/>
      <v-select label="Parity" v-model="parity" :items="opts.parity"/>
      <v-select label="Stop" v-model="stop" :items="opts.stop"/>
      <v-btn color='primary' @click.stop='set'>Update</v-btn>
    </card>
  </v-layout>
</template>

<script lang='coffee'>
{uart} = require('./model').default
{required, integer, minValue, maxValue} = require 'vuelidate/lib/validators'

export default
  components:
    card: require('./card').default
  data: ->
    baudrate: 4800
    bits: 8
    parity: null
    stop: 1
    opts:
      baudrate: [300, 600, 1200, 4800, 9600, 19200, 38400, 57600, 115200, 230400, 250000, 460800]
      bits: [7, 8]
      parity: [
        {text: 'None', value: null}
        {text: 'Even', value: 0}
        {text: 'Odd', value: 1}
      ]
      stop: [1, 2]
  methods:
    set: ->
      try
        await uart.put data: {@baudrate, @bits, @parity, @stop}
      catch err
        console.error err
    get: ->
      try
        {@baudrate, @bits, @parity, @stop} = await uart.get()
      catch err
        console.error err
  mounted: ->
    await @get()
</script>

<template>
  <v-layout row wrap>
    <card header='DHT'>
      <v-layout wrap>
        <v-flex xs6><div id='tempChart'/></v-flex>
        <v-flex xs6><div id='humidityChart'/></v-flex>
        <v-flex xs12>{{updatedAt}}</v-flex>
      </v-layout>
    </card>
  </v-layout>
</template>

<script lang='coffee'>
{dht} = require('./model').default
c3 = require 'c3'

export default
  components:
    card: require('./card').default
  data: ->
    updatedAt: new Date()
    temperature: 0
    humidity: 0
    task: null
    chart:
      temperature: null
      humidity: null
  methods:
    get: ->
      try
        {@temperature, @humidity} = await dht.get()
        @updatedAt = new Date()
        @chart.temperature.load
          columns: [
            ['temperature', @temperature]
          ]
        @chart.humidity.load
          columns: [
            ['humidity', @humidity]
          ]
      catch err
        console.error err
  created: ->
    await @get()
    @task = setInterval @get, 2000
  mounted: ->
    @chart.temperature = c3.generate
      bindto: '#tempChart'
      data:
        columns: [
        ]
        type: 'gauge'
      gauge:
        label:
          format: (value, ratio) ->
            "#{value}\u2103"
      color:
        pattern: ['red']
    @chart.humidity = c3.generate
      bindto: '#humidityChart'
      data:
        columns: [
        ]
        type: 'gauge'
      color:
        pattern: ['blue']
  destroyed: ->
    clearInterval @task
</script>

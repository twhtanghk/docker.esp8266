<template>
  <v-layout row wrap>
    <card header='Liquid Level'>
      <v-layout wrap>
        <v-flex xs12><div id='liquidChart'/></v-flex>
        <v-flex xs12>{{updatedAt}}</v-flex>
      </v-layout>
    </card>
  </v-layout>
</template>

<script lang='coffee'>
{liquid} = require('./model').default
c3 = require 'c3'

export default
  components:
    card: require('./card').default
  data: ->
    updatedAt: new Date()
    value: 0
    task: null
    chart: null
  methods:
    get: ->
      try
        @value = 100 * await liquid.read data: id: 2
        @updatedAt = new Date()
        @chart.load
          columns: [
            ['level', @value]
          ]
      catch err
        console.error err
  created: ->
    await @get()
    @task = setInterval @get, 2000
  mounted: ->
    @chart = c3.generate
      bindto: '#liquidChart'
      data:
        columns: [
        ]
        type: 'gauge'
  destroyed: ->
    clearInterval @task
</script>

<template>
  <v-layout row wrap>
    <card header='DHT'>
      <v-text-field v-model='updatedAt' label='Last updated at' disabled />
      <v-text-field v-model='temperature' label='Temperature' disabled />
      <v-text-field v-model='humidity' label='Humidity' disabled />
    </card>
  </v-layout>
</template>

<script lang='coffee'>
Promise = require 'bluebird'
{dht} = require('./model').default

export default
  components:
    card: require('./card').default
  data: ->
    updatedAt: new Date()
    temperature: 0
    humidity: 0
    task: null
  methods:
    get: ->
      try
        {@temperature, @humidity} = await dht.get()
        @updatedAt = new Date()
      catch err
        console.error err
  created: ->
    await @get()
    @task = setInterval @get, 2000
  destroyed: ->
    clearInterval @task
</script>

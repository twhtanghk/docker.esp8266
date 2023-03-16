<template>
  <v-row wrap justify='center'>
    <card :header="'Pin ' + id">
      <v-row justify='space-around'>
        <v-switch :label='val ? "on" : "off"' v-model="val" @change="set"/>
        <v-col cols="12">
          <v-text-field label="Interval" v-model="elapsed" @change="interval"/>
        </v-col>
      </v-row>
    </card>
  </v-row>
</template>

<script lang='coffee'>
{gpio} = require('./plugins/api').default
{required, integer, minValue, maxValue} = require '@vuelidate/validators'

export default
  components:
    card: require('./card').default
  data: ->
    id: 'switch'
    val: 0
    elapsed: 30 * 60 # default 30 min
    opts:
      val: [0, 1]
  methods:
    set: ->
      try
        await gpio.update data: {@id, @val}
      catch err
        console.error err
    get: ->
      try
        {@val, @elapsed} = await gpio.read data: {@id}
      catch err
        console.error err
    interval: ->
      try
        await gpio.put
          url: "#{gpio.baseUrl}/interval"
          data: {@elapsed}
      catch err
        console.error err
  mounted: ->
    await @get()
</script>

<style lang='scss'>
label {
  margin-bottom: 0;
}
</style>

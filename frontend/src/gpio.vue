<template>
  <v-row>
    <v-col>
      <card :header="id">
        <v-btn color='primary' variant='outlined' @mousedown='on' @touchstart='on' @mouseup='off' @touchend='off'>
          {{id}}
        </v-btn>
      </card>
    </v-col>
  </v-row>
</template>

<script lang='coffee'>
import {gpio} from './plugins/api'
import card from './card'

export default
  components: {card}
  data: ->
    id: 'switch'
  methods:
    on: ->
      await gpio.put url: "/gpio/#{@id}/on"
    off: ->
      await gpio.put url: "/gpio/#{@id}/off"
    get: ->
      val = await gpio.read data: {@id}
  mounted: ->
    await @get()
</script>

<style lang='scss'>
label {
  margin-bottom: 0;
}
</style>

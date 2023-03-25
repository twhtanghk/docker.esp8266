<template>
  <v-row>
    <v-col>
      <card :header="id + ': '  + (state == '1' ? 'high (off)' : 'low (on)')">
        <v-btn color='primary' variant='outlined' @mousedown='off' @touchstart='off' @mouseup='on' @touchend='on'>
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
    state: null
  methods:
    on: ->
      {@state} = await gpio.put url: "/gpio/#{@id}/on"
      @state = state
    off: ->
      {@state} = await gpio.put url: "/gpio/#{@id}/off"
  mounted: ->
    {@state} = await gpio.read data: {@id}
</script>

<style lang='scss'>
label {
  margin-bottom: 0;
}
</style>

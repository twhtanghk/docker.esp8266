<template>
  <v-layout row wrap>
    <ap/>
    <sta/>
    <card header='Settings'>
      <v-btn color='primary' @click='factory'>Factory Default</v-btn>
      <v-btn color='secondary' @click='reboot'>Reboot</v-btn>
    </card>
  </v-layout>
</template>

<script lang='coffee'>
{cfg} = require('./model').default

export default
  components:
    ap: require('./ap').default
    sta: require('./sta').default
    card: require('./card').default
  methods:
    factory: ->
      cfg
        .get url: "#{cfg.baseUrl}/factory"
        .catch console.error
    reboot: ->
      cfg
        .get url: "#{cfg.baseUrl}/reboot"
        .catch console.error
</script>

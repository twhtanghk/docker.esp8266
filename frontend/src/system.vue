<template>
  <v-row wrap justify='center'>
    <ap/>
    <sta/>
    <card header='Settings'>
      <v-btn color='primary' @click='factory'>Factory Default</v-btn>
      <v-btn color='secondary' @click='reboot'>Reboot</v-btn>
    </card>
  </v-row>
</template>

<script lang='coffee'>
{Cfg} = require('./plugins/model.coffee').default

export default
  components:
    ap: require('./ap').default
    sta: require('./sta').default
    card: require('./card').default
  methods:
    factory: ->
      Cfg
        .get url: "#{Cfg.baseUrl}/factory"
        .catch console.error
    reboot: ->
      Cfg
        .get url: "#{Cfg.baseUrl}/reboot"
        .catch console.error
</script>

<template>
  <v-row>
    <v-col>
      <ap/>
    </v-col>
    <v-col>
      <sta/>
    </v-col>
    <v-col>
      <card header='Settings'>
        <v-btn color='primary' @click='factory'>Factory Default</v-btn>
        <v-btn @click='reboot'>Reboot</v-btn>
      </card>
    </v-col>
  </v-row>
</template>

<script lang='coffee'>
import cfg from './plugins/api'
import ap from './ap'
import sta from './sta'
import card from './card'

export default
  components: {ap, sta, card}
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

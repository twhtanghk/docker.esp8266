<template>
  <v-toolbar color='primary' dark>
    <v-toolbar-title class='white--text'>
      ESP
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-menu bottom left>
      <template v-slot:activator="{ on }">
        <v-btn dark icon v-on="on">
          <v-icon>more_vert</v-icon>
        </v-btn>
      </template>
      <v-list>
        <v-list-item v-for='(desc, action) in actions' :key='action' @click='click(action)'>
          <v-list-item-title>{{desc}}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-toolbar>
</template>

<script lang='coffee'>
export default
  data: ->
    actions:
      ap: 'Access Point'
      sta: 'Station'
      syslog: 'Syslog'
      ddns: 'Dynamic DNS'
      gpio: 'General Purpose IO'
      pwm: 'Pulse Width Modulation'
  methods:
    click: (action) ->
      window.location.hash = "#/#{action}"
</script>

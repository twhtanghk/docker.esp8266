<template>
  <v-toolbar color='primary' dark>
    <v-toolbar-title class='white--text'>
      ESP
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-menu bottom left>
      <v-btn slot='activator' dark icon>
        <v-icon>more_vert</v-icon>
      </v-btn>
      <v-list>
        <v-list-tile v-for='(desc, action) in actions' :key='action' @click='click(action)'>
          <v-list-tile-title>{{desc}}</v-list-tile-title>
        </v-list-tile>
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

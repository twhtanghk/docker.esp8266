<template>
  <v-toolbar color='primary' dark>
    <v-toolbar-title class='white--text'>
      PWM Fan
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
      pwm: 'Pulse Width Modulation'
      system: 'System'
  methods:
    click: (action) ->
      window.location.hash = "#/#{action}"
</script>

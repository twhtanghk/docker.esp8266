<template>
  <v-app-bar> 
    <v-toolbar-title class='white--text'>
      GPIO
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn v-for='(desc, action) in actions' :key='action' @click='click(action)'>
      {{desc}}
    </v-btn>
  </v-app-bar>
</template>

<script lang='coffee'>
export default
  data: ->
    actions:
      gpio: 'GPIO'
      system: 'System'
  methods:
    click: (action) ->
      window.location.hash = "#/#{action}"
</script>

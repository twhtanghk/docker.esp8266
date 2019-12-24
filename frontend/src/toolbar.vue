<template>
  <v-app-bar app color='primary'>
    <v-toolbar-title class='white--text'>
      GPIO
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

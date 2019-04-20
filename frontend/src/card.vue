<template>
  <v-flex xs12>
    <v-card class='rounded-card' flat color='grey lighten-3'>
      <v-toolbar dense color='primary' class='white--text'>
        <v-toolbar-title>Switch</v-toolbar-title>
        <v-spacer/>
        <v-btn v-for='cmd in actions' :key='cmd' dark icon>
          <v-icon>{{cmd}}</v-icon>
        </v-btn>
      </v-toolbar>
      <v-card-text>
        <slot/>
      </v-card-text>
    </v-card>
  </v-flex>
</template>

<script lang='coffee'>
export default
  props: [
    'header'
    'actions'
  ]
</script>

<style scoped>
.rounded-card {
  border-radius: 1em;
}
</style>

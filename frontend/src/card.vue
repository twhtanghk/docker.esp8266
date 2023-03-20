<template>
  <v-row>
    <v-col>
      <v-card>
        <v-toolbar>
          <v-toolbar-title>{{header}}</v-toolbar-title>
          <v-btn v-for='cmd in actions' :key='cmd' dark icon>
            <v-icon>{{cmd}}</v-icon>
          </v-btn>
        </v-toolbar>
        <v-card-text>
          <slot/>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
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
  margin: .5em;
}
</style>

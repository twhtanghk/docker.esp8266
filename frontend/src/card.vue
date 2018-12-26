<template>
  <v-flex xs12>
    <v-card class='rounded-card'>
      <v-card-title class='primary white--text'>
        <div>
          <div class='headline'>{{header}}</div>
        </div>
      </v-card-title>
      <v-card-text>
        <slot></slot>
      </v-card-text>
    </v-card>
  </v-flex>
</template>

<script lang='coffee'>
export default
  props: [
    'header'
  ]
</script>

<style scoped>
.rounded-card {
  border-radius: 1em;
}

.v-card__title {
  padding: .5em;
}

.headline {
  font-size: 16px !important;
}
</style>

<template>
  <v-app>
    <toolbar />
    <v-content>
      <v-container grid-list-md>
        <router-view />
      </v-container>
    </v-content>
  </v-app>
</template>

<script lang='coffee'>
import toolbar from './toolbar'

export default
  components: {toolbar}
</script>

<style lang='scss'>
body {
  margin: 0;
}
</style>

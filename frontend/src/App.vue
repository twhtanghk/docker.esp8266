<template>
  <v-app>
    <v-layout>
      <toolbar />
      <v-main>
        <v-container>
          <router-view />
        </v-container>
      </v-main>
    </v-layout>
  </v-app>
</template>

<script lang='coffee'>
import toolbar from './toolbar'

export default
  components: {toolbar}
</script>

<style lang='scss'>
@use "vuetify/styles";

body {
  margin: 0;
}

button {
  @extend .mx-lg-2;
}
</style>

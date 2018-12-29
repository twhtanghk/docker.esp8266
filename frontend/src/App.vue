<template>
  <v-app>
    <toolbar />
    <v-card>
      <v-container fluid grid-list-lg>
        <router-view />
      </v-container>
    </v-card>
  </v-app>
</template>

<script lang='coffee'>
Vue = require('vue').default
Vue.use require 'vuetify'
Vue.use require 'vee-validate'

export default
  components:
    toolbar: require('./toolbar').default
</script>

<style lang='scss'>
$material-icons-font-path: '~material-icons/iconfont/';
@import '~material-icons/iconfont/material-icons.scss';
@import '~vuetify/dist/vuetify.min.css';

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

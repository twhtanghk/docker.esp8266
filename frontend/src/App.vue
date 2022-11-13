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
Vue = require('vue').default

export default
  components:
    toolbar: require('./toolbar').default
</script>

<style lang='scss'>
$material-icons-font-path: '~material-icons/iconfont/';
@import '~material-icons/iconfont/material-icons.scss';
@import '~vuetify/dist/vuetify.min.css';
@import '~c3/c3.min.css';

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

  button {
    margin: .4em;
  }
}

.v-content {
  height: 100%;
}

</style>

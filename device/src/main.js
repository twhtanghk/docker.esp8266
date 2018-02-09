// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import BootstrapVue from 'bootstrap-vue'
import Toasted from 'vue-toasted'

Vue.use(BootstrapVue)
Vue.use(Toasted)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>',
  http: {
    root: 'http://192.168.4.1',
  }
})

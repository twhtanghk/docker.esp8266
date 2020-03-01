import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import vuetify from './plugins/vuetify.coffee'
import './registerServiceWorker'

Vue.config.productionTip = false

Vue.use(VueRouter)
const router = new VueRouter({
  routes: [
    {path: '/antenna', component: require('./antenna').default},
    {path: '/system', component: require('./system').default},
    {path: '*', redirect: '/antenna'}
  ]
})

new Vue({
  router,
  render: h => h(App),
  vuetify
}).$mount('#app')

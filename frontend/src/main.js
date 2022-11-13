import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Vuetify from 'vuetify'
import './registerServiceWorker'

Vue.config.productionTip = false

Vue.use(VueRouter)
const router = new VueRouter({
  routes: [
    {path: '/antenna', component: require('./antenna').default},
    {path: '/system', component: require('./system').default},
    {path: '/:pathMatch(.*)*', redirect: '/antenna'}
  ]
})

Vue.use(Vuetify)
const vuetify = new Vuetify()

new Vue({
  router,
  render: h => h(App),
  vuetify
}).$mount('#app')

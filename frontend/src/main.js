import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import vuetify from './plugins/vuetify.coffee'

Vue.config.productionTip = false

Vue.use(VueRouter)
const router = new VueRouter({
  routes: [
    {path: '/gpio', component: require('./gpio').default},
    {path: '/system', component: require('./system').default},
    {path: '*', redirect: '/gpio'}
  ]
})

new Vue({
  router,
  render: h => h(App),
  vuetify
}).$mount('#app')

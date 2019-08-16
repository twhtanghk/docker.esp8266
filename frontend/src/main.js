import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import vuetify from './plugins/vuetify.coffee'

Vue.config.productionTip = false

Vue.use(VueRouter)
const router = new VueRouter({
  routes: [
    {path: '/system', component: require('./system').default},
    {path: '/syslog', component: require('./syslog').default},
    {path: '/gpio', component: require('./gpio').default},
    {path: '/ddns', component: require('./ddns').default},
    {path: '/pwm', component: require('./pwm').default},
    {path: '/dht', component: require('./dht').default},
    {path: '/liquid', component: require('./liquid').default},
    {path: '*', redirect: '/system'}
  ]
})

new Vue({
  router,
  render: h => h(App),
  vuetify
}).$mount('#app')

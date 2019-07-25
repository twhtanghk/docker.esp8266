import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import vuetify from './plugins/vuetify.coffee'

Vue.config.productionTip = false

Vue.use(VueRouter)
const router = new VueRouter({
  routes: [
    {path: '/ap', component: require('./ap').default},
    {path: '/sta', component: require('./sta').default},
    {path: '/syslog', component: require('./syslog').default},
    {path: '/gpio', component: require('./gpio').default},
    {path: '/ddns', component: require('./ddns').default},
    {path: '/pwm', component: require('./pwm').default},
    {path: '*', redirect: '/ap'}
  ]
})

new Vue({
  router,
  render: h => h(App),
  vuetify
}).$mount('#app')

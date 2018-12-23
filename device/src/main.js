import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

Vue.use(VueRouter)
const router = new VueRouter({
  routes: [
    {path: '/AP', component: require('./ap').default},
    {path: '/STA', component: require('./sta').default},
    {path: '/DDNS', component: require('./ddns').default},
    {path: '/GPIO', component: require('./gpio').default},
    {path: '/pwm', component: require('./pwm').default},
    {path: '*', redirect: '/AP'}
  ]
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

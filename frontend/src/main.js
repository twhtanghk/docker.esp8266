import { createApp }from 'vue'
import App from './App.vue'
import {createVuetify} from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import {md2} from 'vuetify/blueprints'
import * as VueRouter from 'vue-router'

const vuetify = createVuetify({components, directives, blueprint: md2})
const routes = [
  {path: '/', redirect: '/switch'},
  {path: '/switch', component: require('./gpio').default},
  {path: '/system', component: require('./system').default}
]
const router = VueRouter.createRouter({
  history: VueRouter.createWebHashHistory(),
  routes
})

const app = createApp(App)
app
  .use(vuetify)
  .use(router)
  .mount('#app')

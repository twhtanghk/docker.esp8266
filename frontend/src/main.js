import {createApp}from 'vue'
import App from './App.vue'
import {createVuetify} from 'vuetify'
import {md2} from 'vuetify/blueprints'
import {createRouter, createWebHashHistory} from 'vue-router'
import gpio from './gpio'
import system from './system'

const vuetify = createVuetify()
const routes = [
  {path: '/', redirect: '/gpio'},
  {path: '/gpio', component: gpio},
  {path: '/system', component: system}
]
const router = createRouter({
  history: createWebHashHistory(),
  routes
})

const app = createApp(App)
app
  .use(vuetify)
  .use(router)
  .mount('#app')

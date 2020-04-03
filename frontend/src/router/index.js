import Vue from 'vue'
import VueRouter from 'vue-router'
import main from './main'
import '../assets/_scss/app.scss'
Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    ...main
  ]
})

export default router

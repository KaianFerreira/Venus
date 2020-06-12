import Vue from 'vue'
import VueRouter from 'vue-router'
import main from './main'
import user from './user'
import '../assets/_scss/app.scss'
Vue.use(VueRouter)

Vue.config.errorHandler = (err, vm, info) => {
  if (err.name === 'NavigationDuplicated') return false
}

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    ...main,
    ...user
  ]
})

export default router

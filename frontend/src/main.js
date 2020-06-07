import Vue from 'vue'
import App from './components/App.vue'
import router from './router'
import store from './store'
import { getData } from './libs/token'

Vue.config.productionTip = false

Vue.component('Logo', () => import('./components/Logo.vue'))
Vue.component('Input', () => import('./components/Input.vue'))
Vue.component('IconClose', () => import('./icons/IconClose.vue'))
Vue.component('IconArrow', () => import('./icons/IconArrow.vue'))

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

const start = async () => {
  try {
    if (getData()) {
      store.dispatch('signIn', getData())
    } else {
      store.dispatch('signOut')
    }
  } catch (error) {
    store.dispatch('signOut')
  }
}

start()

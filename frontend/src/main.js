import Vue from 'vue'
import App from './components/App.vue'
import router from './router'
import store from './store'
// import { getToken } from './libs/token'
Vue.config.productionTip = false

Vue.component('Input', () => import('./components/Input.vue'))
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

// const start = async () => {
//   try {
//     if (getToken()) {

//     }
//   } catch (error) {
//     store.dispatch('signOut')
//   }
// }

// start()

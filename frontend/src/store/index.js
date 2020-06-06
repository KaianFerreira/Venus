import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router'
import { setData, removeData } from '../libs/token'
Vue.use(Vuex)

const startTime = new Date()

export default new Vuex.Store({
  state: {
    loaded: null,
    user: null
  },
  mutations: {
    loaded (state, data) { state.loaded = data },
    user (state, data) { state.user = data }
  },
  actions: {
    loaded (store) {
      const diff = (new Date()) - startTime
      const wait = 2000 - diff < 0 ? 0 : 2000 - diff
      setTimeout(() => {
        store.commit('loaded', true)
      }, wait)
    },
    async signIn (store, data) {
      store.commit('user', data.user)
      setData({ token: data.token, user: data.user })
      router.push('/')
      // should set the signIn token here
      store.dispatch('loaded')
    },
    signOut (store) {
      store.commit('user', null)
      removeData()
      router.push('/signin')
      store.dispatch('loaded')
    }
  }
})

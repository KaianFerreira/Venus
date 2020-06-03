import Vue from 'vue'
import Vuex from 'vuex'
import { setToken, removeToken } from '../libs/token'
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
      setToken(data.token)
      // should set the signIn token here
      store.dispatch('loaded')
    },
    signOut (store) {
      store.commit('user', null)
      removeToken()
      store.dispatch('loaded')
    }
  }
})

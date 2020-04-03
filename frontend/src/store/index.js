import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const startTime = new Date()

export default new Vuex.Store({
  state: {
    loaded: null,
    user: null
  },
  mutations: {
    loaded (state, data) { state.loaded = data }
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
      // should set the signIn token here
      store.dispatch('loaded')
    },
    signOut (store) {
      store.commit('user', null)
      store.dispatch('loaded')
    }
  }
})

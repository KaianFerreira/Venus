export default [
  {
    path: '/',
    name: 'Home',
    component: () => import(/* webpackChunkName: "user" */ '../components/user/Router.vue')
  }
]

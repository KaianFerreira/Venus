export default [
  {
    path: '*',
    redirect: '/signin'
  },
  {
    path: '/signin',
    name: 'signin',
    component: () => import(/* webpackChunkName: "main" */ '../components/SignIn.vue')
  }
]

export default [
  {
    path: '*',
    redirect: '/'
  },
  {
    path: '/signin',
    name: 'signin',
    component: () => import(/* webpackChunkName: "main" */ '../components/SignIn.vue')
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import(/* webpackChunkName: "main" */ '../components/SignUp.vue')
  },
  {
    path: '/',
    name: 'teste',
    component: () => import(/* webpackChunkName: "user" */ '../components/Chat.vue')
  }
]

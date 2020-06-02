export default [
  {
    path: '*',
    redirect: '/signin'
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
  }
  {
    path: '/teste',
    name: 'teste',
    component: () => import(/* webpackChunkName: "main" */ '../components/postList.vue')
  }
]

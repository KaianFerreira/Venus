export default [
  {
    path: '/',
    name: 'Posts',
    component: () => import(/* webpackChunkName: "user" */ '../components/user/Posts.vue')
  }
]
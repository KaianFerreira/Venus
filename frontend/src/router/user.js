export default [
  {
    path: '/',
    component: () => import(/* webpackChunkName: "user" */ '../components/user/Router.vue'),
    children: [
      {
        path: '',
        name: 'posts',
        component: () => import(/* webpackChunkName: "user" */ '../components/user/Posts.vue')
      },
      {
        props: true,
        path: '/profile/:username',
        name: 'profile',
        component: () => import(/* webpackChunkName: "user" */ '../components/user/Profile.vue')
      }
    ]
  }
]

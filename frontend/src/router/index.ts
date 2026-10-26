import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'homepage',
      component: () => import('../views/homepage/HomepageView.vue'),
    },
    {
      path: '/friends',
      name: 'friendslist',
      component: () => import('../views/friends/FriendsView.vue'),
    },
    {
      path: '/createfriends',
      name: 'createfriends',
      component: () => import('../views/create/CreateView.vue'),
    },
    {
      path: '/error',
      name: 'notfound',
      component: () => import('../views/error/NotFoundView.vue'),
    },
    {
      path: '/user/account/login',
      name: 'user-account-login',
      component: () => import('../views/user/account/LoginView.vue'),
    },
    {
      path: '/user/account/register',
      name: 'user-account-register',
      component: () => import('../views/user/account/RegisterView.vue'),
    },
    {
      path: '/user/space/:user_id',
      name: 'user-space',
      component: () => import('../views/user/space/SpaceView.vue'),
    },
    {
      path: '/user/profile',
      name: 'user-profile',
      component: () => import('../views/profile/ProfileView.vue'),
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'erro-page',
      component: () => import('../views/error/NotFoundView.vue'),
    }
  ],
})

export default router

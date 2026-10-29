import { createRouter, createWebHistory } from 'vue-router'
import {useUserStore} from "@/stores/user.ts";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'homepage',
      component: () => import('../views/homepage/HomepageView.vue'),
      meta: {
        needLogin: false,
      },
    },
    {
      path: '/friends',
      name: 'friendslist',
      component: () => import('../views/friends/FriendsView.vue'),
      meta: {
        needLogin: true,
      },
    },
    {
      path: '/createfriends',
      name: 'createfriends',
      component: () => import('../views/create/CreateView.vue'),
      meta: {
        needLogin: true,
      },
    },
    {
      path: '/error',
      name: 'notfound',
      component: () => import('../views/error/NotFoundView.vue'),
      meta: {
        needLogin: false,
      },
    },
    {
      path: '/user/account/login',
      name: 'user-account-login',
      component: () => import('../views/user/account/LoginView.vue'),
      meta: {
        needLogin: false,
      },
    },
    {
      path: '/user/account/register',
      name: 'user-account-register',
      component: () => import('../views/user/account/RegisterView.vue'),
      meta: {
        needLogin: false,
      },
    },
    {
      path: '/user/space/:user_id',
      name: 'user-space',
      component: () => import('../views/user/space/SpaceView.vue'),
      meta: {
        needLogin: true,
      },
    },
    {
      path: '/user/profile',
      name: 'user-profile',
      component: () => import('../views/profile/ProfileView.vue'),
      meta: {
        needLogin: true,
      },
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'erro-page',
      component: () => import('../views/error/NotFoundView.vue'),
      meta: {
        needLogin: false,
      },
    }
  ],
})

router.beforeEach((to, from, next) => {
  const userStore = useUserStore()
  if (to.meta.needLogin && !userStore.isLogin()) {
    return next('/user/account/login')
  }
  return next()
})

export default router

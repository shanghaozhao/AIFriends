import { createRouter, createWebHistory } from 'vue-router'
import {useUserStore} from "@/stores/user.ts";
import HomepageView from "@/views/homepage/HomepageView.vue";
import FriendView from "@/views/friends/FriendsView.vue";
import CreateView from "@/views/create/CreateView.vue";
import NotFoundView from "@/views/error/NotFoundView.vue";
import LoginView from "@/views/user/account/LoginView.vue";
import RegisterView from "@/views/user/account/RegisterView.vue";
import SpaceView from "@/views/user/space/SpaceView.vue";
import ProfileView from "@/views/profile/ProfileView.vue";
import UpdateCharacter from "@/views/create/character/UpdateCharacter.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'homepage',
      component: HomepageView,
      meta: {
        needLogin: false,
      },
    },
    {
      path: '/friends/',
      name: 'friendslist',
      component:FriendView,
      meta: {
        needLogin: true,
      },
    },
    {
      path: '/create/character/',
      name: 'create-character',
      component: CreateView,
      meta: {
        needLogin: true,
      },
    },
    {
      path: '/update/character/:character_id/', //这里的角色id在url中
      name: 'update-character',
      component: UpdateCharacter,
      meta: {
        needLogin: true,
      },
    },
    {
      path: '/error/',
      name: 'notfound',
      component: NotFoundView,
      meta: {
        needLogin: false,
      },
    },
    {
      path: '/user/account/login/',
      name: 'user-account-login',
      component: LoginView,
      meta: {
        needLogin: false,
      },
    },
    {
      path: '/user/account/register/',
      name: 'user-account-register',
      component: RegisterView,
      meta: {
        needLogin: false,
      },
    },
    {
      path: '/user/space/:user_id/',
      name: 'user-space',
      component: SpaceView,
      meta: {
        needLogin: true,
      },
    },
    {
      path: '/user/profile/',
      name: 'user-profile',
      component: ProfileView,
      meta: {
        needLogin: true,
      },
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'error-page',
      component: NotFoundView,
      meta: {
        needLogin: false,
      },
    }
  ],
})

router.beforeEach((to, from) => {
  const userStore = useUserStore()
  if (to.meta.needLogin && userStore.hasPulledUserInfo && !userStore.isLogin()) {
    return {
      name: 'user-account-login',
    }
  }
})

export default router

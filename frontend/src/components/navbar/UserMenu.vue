<script setup lang="ts">
import { useUserStore } from '@/stores/user.ts'
import UserSpaceIcon from "@/components/navbar/icons/UserSpaceIcon.vue";
import UserProfileIcon from "@/components/navbar/icons/UserProfileIcon.vue";
import UserLogOutIcon from "@/components/navbar/icons/UserLogOutIcon.vue";
import api from "@/js/http/api.ts";
import {useRouter} from "vue-router";


const userStore = useUserStore()
const router = useRouter()

function closeMenu() {
  const element = document.activeElement
  if (element && element instanceof HTMLElement) element.blur()
}

async function handleLogout() {
  try{
    const response = await api.post('/api/user/account/logout/')
    if (response.data.result === 'success') {
      userStore.logout()
      await router.push({ name: 'homepage' })
    }
  }catch (error){
    console.log(error)
  }

}
</script>

<template>
  <div class="dropdown dropdown-end mr-3">
    <div tabindex="0" role="button" class="avatar btn btn-circle m-2">
      <div class="w-8 rounded-full">
        <img :src="userStore.photo" />
      </div>
    </div>
    <ul tabindex="-1" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
      <li>
        <div @click="closeMenu">
          <div class="avatar">
            <div class="w-10 rounded-full">
              <img :src="userStore.photo" alt="" />
            </div>
          </div>
          <span class="text-base font-bold line-clamp-1 break-all">{{ userStore.username }}</span>
        </div>
      </li>
      <li>
        <router-link @click="closeMenu" :to="{ name: 'user-space' ,params: { user_id: userStore.id }}" class="text-sm font-bold py-2" >
          <user-space-icon />
          my space
        </router-link>
      </li>
      <li>
        <router-link @click="closeMenu" :to="{ name: 'user-profile'}" class="text-sm font-bold py-2" >
          <user-profile-icon />
          editor profile
        </router-link>
      </li>
      <li></li>
      <li>
        <a @click="handleLogout" class="text-sm font-bold py-2" >
          <user-log-out-icon />
          log out
        </a>
      </li>
    </ul>
  </div>
</template>

<style scoped>

</style>
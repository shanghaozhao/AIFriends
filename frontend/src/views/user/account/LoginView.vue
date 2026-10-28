<script setup lang="ts">

import {ref} from "vue";

const username = ref('');
const password = ref('');
const errorMessage = ref('');

import { useUserStore } from '@/stores/user.ts';
import { useRouter } from 'vue-router';
const userStore = useUserStore();
const router = useRouter();

import api from '@/js/http/api.ts'; //如果是选择ts项目，必须创建ts文件

async function handleLogin() {
   errorMessage.value  = '';
   if (!username.value.trim() || !password.value.trim()) {
     errorMessage.value = 'Username and password are required';
   } else {
     try {
      // TODO: Login logic here
      const response = await api.post('/api/user/account/login/',{
        username: username.value,
        password: password.value
      })
      const data = response.data
      if (data.result === 'success'){
        userStore.setAccessToken(data.access)
        // console.log(data.user_id)
        userStore.setUserInfo(data)
        await router.push({ name: 'homepage' });
      }
      else {
        errorMessage.value = data.result;
      }
     } catch (error) {
        errorMessage.value = 'Login failed. Please try again.';
        console.log(error)
     }
   }

}

</script>
<template>
  <div class="flex flex-col items-center h-screen pt-[18vh]">
     <form @submit.prevent="handleLogin" class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
        <legend class="fieldset-legend">
          <router-link :to="{ name: 'user-account-register' }" class="btn btn-xs btn-ghost">Register</router-link>
        </legend>

        <label class="label">Username</label>
        <input v-model="username" type="text" class="input" placeholder="Username" />

        <label class="label">Password</label>
        <input v-model="password" type="password" class="input" placeholder="Password" />

       <p v-if="errorMessage" class="text-error">{{ errorMessage }}</p>

        <button class="btn btn-neutral mt-4">Login</button>
      </form>
  </div>
</template>
<style scoped>

</style>
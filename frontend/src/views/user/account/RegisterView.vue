<script setup lang="ts">

import {ref} from "vue";

const username = ref('');
const password = ref('');
const confirmPassword = ref('');
const errorMessage = ref('');

import {useUserStore} from "@/stores/user.ts";
import {useRouter} from "vue-router";
import api from "@/js/http/api.ts";
const userStore = useUserStore();
const router = useRouter();

async function handleRegister() {
  errorMessage.value = '';
  if (!username.value.trim() || !password.value.trim() || !confirmPassword.value.trim()) {
    errorMessage.value = 'Please fill in all fields';
  }
  else if (password.value.trim() !== confirmPassword.value.trim()) {
    errorMessage.value = 'Passwords do not match';
  }
  else if (password.value.trim() === confirmPassword.value.trim()){
    try {
      const response = await api.post('/api/user/account/register/', {
        username: username.value,
        password: password.value
      });
      const data = response.data;
      if (data.result === 'success') {
        userStore.setAccessToken(data.access);
        userStore.setUserInfo(data);
        await router.push({name: 'homepage'});
      } else {
        errorMessage.value = data.result;
      }
    } catch (error) {
      console.error('Registration failed:', error);
      errorMessage.value = 'Registration failed. Please try again later.';
    }
  }
}
</script>

<template>
  <div class="flex flex-col items-center h-screen pt-[18vh]">
     <form @submit.prevent="handleRegister" class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
        <legend class="fieldset-legend">
          <router-link :to="{ name: 'user-account-login' }" class="btn btn-xs btn-ghost">Login</router-link>
        </legend>

        <label class="label">Username</label>
        <input v-model="username" type="text" class="input" placeholder="Username" />

        <label class="label">Password</label>
        <input v-model="password" type="password" class="input" placeholder="Password" />

        <label class="label">Confirm Password</label>
        <input v-model="confirmPassword" type="password" class="input" placeholder="Confirm Password" />
        <p v-if="errorMessage" class="text-error">{{ errorMessage }}</p>
       <button class="btn btn-neutral mt-4">Register</button>
      </form>
  </div>
</template>
<style scoped>

</style>
<script setup lang="ts">

</script>

<template>
  <div class="flex flex-col items-center h-screen pt-[18vh]">
     <fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
        <legend class="fieldset-legend">
          <router-link :to="{ name: 'user-account-login' }" class="btn btn-xs btn-ghost">Login</router-link>
        </legend>

        <label class="label">Username</label>
        <input type="text" class="input" placeholder="Username" />

        <label class="label">Password</label>
        <input type="password" class="input" placeholder="Password" />

        <label class="label">Confirm Password</label>
        <input type="password" class="input" placeholder="Confirm Password" />
        <button class="btn btn-neutral mt-4">Register</button>
      </fieldset>
  </div>
</template>
<style scoped>

</style>
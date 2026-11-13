<script setup lang="ts">
defineProps(['userProfile'])

</script>

<template>
  <div v-if="userProfile" class="flex mt-12 gap-6">
    <div class="justify-center avatar h-36 w-38">
      <img :src="userProfile.photo" alt="User Avatar" class="rounded-full w-32 h-32">
    </div>
    <div class="justify-center h-36 w-38">
      <div class="text-xl font-semibold line-clamp-1 break-all">{{ userProfile.username }}</div>
      <div class="text-base">AIFriends账号：{{ userProfile.user_id }}</div>
      <div class="text-gray-500 h-20 mt-4 line-clamp-4 break-all">{{ userProfile.profile }}</div>
    </div>
  </div>
</template>

<style scoped>

</style>
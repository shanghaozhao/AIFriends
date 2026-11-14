<script setup lang="ts">
import {ref} from "vue";

defineProps(['character', 'canEdit'])
const isHover = ref(false)
</script>

<template>
  <div>
    <div class="avatar cursor-pointer" @mouseenter="isHover = true" @mouseleave="isHover = false">
      <div class="w-50 h-100 rounded-2xl">
        <img :src="character.background_image" :class="{ 'scale-120': isHover }" alt="Avatar" />
      </div>
    </div>
    <div>
      用户信息author
    </div>
  </div>
</template>

<style scoped>

</style>
<script setup lang="ts">

import {ref, watch} from 'vue';
const props = defineProps({
  username: String,
});
const myUsername = ref(props.username);
watch(() => props.username, (newVal) => {
    myUsername.value = newVal;
})

defineExpose({ myUsername })

</script>

<template>
  <fieldset class="fieldset ">
    <div class="label text-base">用户名</div>
    <input v-model="myUsername" type="text" class="input w-full" placeholder="Username" />
  </fieldset>
</template>

<style scoped>

</style>
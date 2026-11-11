<script setup lang="ts">

import {ref, watch} from 'vue';
const props = defineProps({
  username: String,
});
const myUsername = ref(props.username);
// 监听props.username变化并更新myUsername，是在后端更新后能更新
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
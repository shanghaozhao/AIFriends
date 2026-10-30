<script setup lang="ts">

import {ref, watch} from 'vue';
const props = defineProps({
  profile: String,
});
const myProfile = ref(props.profile);

watch(() => props.profile, (newVal) => {
    myProfile.value = newVal;
})

defineExpose({ myProfile })

</script>

<template>
<fieldset class="fieldset">
    <div class="label text-base">个人简介</div>
    <textarea v-model="myProfile"  rows="6" class="textarea w-full" placeholder="Enter your profile here" />
  </fieldset>
</template>

<style scoped>

</style>
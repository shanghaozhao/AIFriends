<script setup lang="ts">
import {ref, watch} from "vue";

const props = defineProps(['name'])
const myName = ref(props.name)

watch(() => props.name, (newVal) => {
  myName.value = newVal
})

defineExpose({ myName })
</script>

<template>
  <fieldset class="fieldset">
    <label class="label text-base">名称</label>
    <input v-model="myName" class="input w-full" type="text">
  </fieldset>
</template>

<style scoped>

</style>
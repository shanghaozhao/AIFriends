<script setup lang="ts">

import {onBeforeUnmount, ref, useTemplateRef, watch} from 'vue'
import CameraIcon from "@/components/userinfo/icons/CameraIcon.vue";
import Croppie from 'croppie'
import 'croppie/croppie.css'

const props = defineProps(['photo'])
const myPhoto = ref(props.photo)

watch(() => props.photo, (newVal) => {
  myPhoto.value = newVal
})

const fileInputRef = useTemplateRef("file-input-ref")
const modalRef = useTemplateRef("modal-ref")
const croppieRef = useTemplateRef('croppie-ref')
let croppie = null

async function openModal(photo: string) {
  modalRef.value.showModal()

  if (!croppie) {
    croppie = new Croppie(croppieRef.value, {  // 创建croppie对象
      viewport: {width: 200, height: 200, type: 'square'},
      boundary: {width: 300, height: 300},
      enableOrientation: true,
      enforceBoundary: true,
    })
  }
  // 将图片加载到这个模态框里面
  croppie.bind({
    url: photo
  })
}

async function crop() {
  if (!croppie) return

  croppie.result({
    type: 'base64',
    size: 'viewport'
  }).then(result => {
    myPhoto.value = result
    modalRef.value.close()
  })
}
const onFileChange = (e: any) => {
  const file = e.target.files[0]
  e.target.value = '' //因为这里一个change函数需要有变化
  if (!file) return

  const reader = new FileReader()
  reader.onload = (e) => {       // ① 先注册"读完后的回调"
    openModal(reader.result)     // ③ 异步触发,此时 reading 已经完成
  }
  reader.readAsDataURL(file)    // ② 再启动读取(异步)
}

onBeforeUnmount(() => {  // 释放croppie对象，防止内存泄漏
  croppie?.destroy()
})

defineExpose({ myPhoto})
</script>

<template>
  <div class="flex justify-center">
    <div class="avatar relative">
      <div v-if="myPhoto" class="w-28 rounded-full">
        <img :src="myPhoto" alt="Avatar">
      </div>

      <div v-else class="w-28 h-28 rounded-full bg-base-200"></div>

      <div @click="fileInputRef?.click()" class="w-28 h-28 bg-black/20 rounded-full absolute top-0 left-0 flex justify-center items-center cursor-pointer">
        <CameraIcon />
      </div>
    </div>
  </div>

  <input ref="file-input-ref" type="file"  accept="image/*" class="hidden" @change="onFileChange">

  <dialog ref="modal-ref" class="modal">
    <div class="modal-box transition-none">
      <button @click="modalRef.close()" class="btn btn-circle btn-sm btn-ghost absolute right-2 top-2">✕</button>

      <div ref="croppie-ref" class="flex flex-col justify-center my-4"></div>

      <div class="modal-action">
        <button @click="modalRef.close()" class="btn">取消</button>
        <button @click="crop" class="btn btn-neutral">确定</button>
      </div>
    </div>
  </dialog>
</template>

<style scoped>

</style>
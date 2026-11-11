<script setup lang="ts">
import {onBeforeUnmount, ref, useTemplateRef, watch} from "vue";
import CameraIcon from "@/components/userinfo/icons/CameraIcon.vue";
import Croppie from 'croppie'
import 'croppie/croppie.css'

const props = defineProps(['backgroundImage'])
const myBackgroundImage = ref(props.backgroundImage)

watch(() => props.backgroundImage, (newVal) => {
  myBackgroundImage.value = newVal
})

const fileInputRef = useTemplateRef("file-input-ref")
const modalRef = useTemplateRef("modal-ref")
const croppieRef = useTemplateRef('croppie-ref')
let croppie = null

async function openModal(photo: string) {
  modalRef.value.showModal()

  if (!croppie) {
    croppie = new Croppie(croppieRef.value, {  // 创建croppie对象
      viewport: {width: 300, height: 500},
      boundary: {width: 600, height: 600},
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
    myBackgroundImage.value = result
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

defineExpose({ myBackgroundImage })
</script>

<template>
  <fieldset class="fieldset">
    <label class="label text-base">背景图片</label>
    <div class="avatar relative">
      <div v-if="myBackgroundImage" class="w-15 h-25 rounded-box">
        <img :src="myBackgroundImage" alt="背景图片">
      </div>

      <div v-else class="w-15 h-25 rounded-box bg-base-100"></div>

      <div @click="fileInputRef.click()" class="w-15 h-25 rounded-box bg-black/20 absolute left-0 top-0 flex justify-center items-center cursor-pointer">
        <CameraIcon/>
      </div>
    </div>
  </fieldset>

  <input ref="file-input-ref" type="file"  accept="image/*" class="hidden" @change="onFileChange">

  <dialog ref="modal-ref" class="modal">
    <div class="modal-box transition-none max-w-2xl">
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
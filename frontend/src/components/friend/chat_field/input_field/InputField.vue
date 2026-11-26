<script setup lang="ts">
import SendIcon from "@/components/friend/icons/SendIcon.vue";
import MicIcon from "@/components/friend/icons/MicIcon.vue";
import {ref, useTemplateRef} from "vue";
import api from "@/js/http/api.ts";
import streamApi from "@/js/http/streamApi.ts";

const props = defineProps(['friendId'])
const inputRef = useTemplateRef('input-ref')
const message = ref('')
let isRecording = false

function focus() {
  inputRef.value.focus()
}

async function handleSend(){
  if (isRecording) return
  isRecording = true

  const content = message.value.trim()
  if (!content) return
  message.value = ''

  try{
    await streamApi('/api/friend/message/chat/',{
      //以下这些实在api中定义好的
      body:{
        friend_id: props.friendId,
        message: content
      },
      onmessage(data,isDone){
        if(isDone){
          isRecording = false
        }else if (data.content){
          console.log(data.content)
        }
      },
      onerror(error){
        isRecording = false
      }
    })
  }catch(error){
    console.log(error)
  }
}

defineExpose({ focus })
</script>

<template>
  <form @submit.prevent="handleSend" class="absolute bottom-4 left-2 h-12 w-86 flex items-center">
    <input
        ref="input-ref"
        v-model="message"
        class="input bg-black/30 backdrop-blur-sm text-white text-base w-full h-full rounded-2xl pr-20"
        type="text"
        placeholder="文本输入..."
    >
    <div @click="handleSend" class="absolute right-2 w-8 h-8 flex justify-center items-center cursor-pointer">
      <SendIcon />
    </div>
    <div class="absolute right-10 w-8 h-8 flex justify-center items-center cursor-pointer">
      <MicIcon />
    </div>
  </form>
</template>


<style scoped>

</style>
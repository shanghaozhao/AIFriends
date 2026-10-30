<script setup lang="ts">

import { useUserStore } from '@/stores/user';
import UserNameCom from "@/components/userinfo/UserNameCom.vue";
import UserProfileCom from "@/components/userinfo/UserProfileCom.vue";
import UserPhotoCom from "@/components/userinfo/UserPhotoCom.vue";
import {ref, useTemplateRef} from "vue";
import api from "@/js/http/api.ts";
import {base64ToFile} from "@/js/utils/base64_to_file.ts";
const userStore = useUserStore();

const userphotoRef = useTemplateRef('userphoto-ref');
const usernameRef = useTemplateRef('username-ref');
const userprofileRef = useTemplateRef('userprofile-ref');
const errorMessage = ref('');

async function handleUpdate() {
  const userphoto = userphotoRef.value?.myPhoto?.trim(); //调用子组件返回的参数，相当于这个的属性
  const username = usernameRef.value?.myUsername?.trim();
  const profile = userprofileRef.value?.myProfile?.trim();
  errorMessage.value = ''
  if (!userphoto) {
    errorMessage.value = '头像不能为空'
  } else if (!username) {
    errorMessage.value = '用户名不能为空'
  } else if (!profile) {
    errorMessage.value = '简介不能为空'
  } else {
    const formData = new FormData()
    formData.append('username', username)
    formData.append('profile', profile)
    if (userphoto !== userStore.photo) {
      formData.append('photo', base64ToFile(userphoto, 'photo.png'))
    }
    try {
      const res = await api.post('/api/user/profile/update/', formData)
      const data = res.data
      if (data.result === 'success') {
        userStore.setUserInfo(data)
      } else {
        errorMessage.value = data.result
      }
    } catch (err) {
      console.log(err)
    }
  }
}

</script>

<template>
<div class="flex justify-center">
  <div class="card w-120  bg-base-100 shadow-sm mt-20">
    <div class="card-body">
      <h2 class="card-title">编辑个人资料</h2>
      <user-photo-com ref="userphoto-ref" :photo="userStore.photo"/>
      <user-name-com ref="username-ref" :username="userStore.username"/>
      <user-profile-com ref="userprofile-ref" :profile="userStore.profile"/>

      <p class="text-red-500">{{ errorMessage }}</p>
      <btn @click="handleUpdate" class="btn btn-neutral w-3/4 self-center">更新</btn>
    </div>
  </div>
</div>
</template>

<style scoped>

</style>
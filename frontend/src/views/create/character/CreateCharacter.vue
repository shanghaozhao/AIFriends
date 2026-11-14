<script setup lang="ts">

import CharacterPhoto from "@/components/character/CharacterPhoto.vue";
import CharacterName from "@/components/character/CharacterName.vue";
import BackgroundImage from "@/components/character/BackgroundImage.vue";
import CharacterProfile from "@/components/character/CharacterProfile.vue";
import {ref, useTemplateRef} from "vue";
import {base64ToFile} from "@/js/utils/base64_to_file.ts";
import api from "@/js/http/api.ts";
import {useUserStore} from "@/stores/user.ts";
import {useRouter} from "vue-router";

const userStore = useUserStore();
const router = useRouter();

const photoRef = useTemplateRef("photo-ref")
const nameRef = useTemplateRef("name-ref")
const profileRef = useTemplateRef("profile-ref")
const backgroundImageRef = useTemplateRef("backgroundImage-ref")
const errorMessage = ref("");
async function handleCreate() {
  const photo = photoRef.value?.myPhoto;
  const name = nameRef.value?.myName?.trim();
  const profile = profileRef.value?.myProfile?.trim();
  const backgroundImage = backgroundImageRef.value?.myBackgroundImage;
  errorMessage.value = "";

  if (!photo || !name || !profile || !backgroundImage) {
    errorMessage.value = "所有字段都是必填的";
  } else {
    const formData = new FormData();
    formData.append("character_photo", base64ToFile(photo, "photo.png"));
    formData.append("character_name", name);
    formData.append("character_profile", profile);
    formData.append("character_background_image", base64ToFile(backgroundImage, "background_image.png"));
    try {
      const res = await api.post('/api/character/create/', formData);
      const data = res.data;
      if (data.result === 'success') {
        // console.log("角色创建成功");
        await router.push({
          name: "user-space",
          params: {user_id: userStore.id}
        });
      } else {
        errorMessage.value = data.result;
      }
    } catch (err) {
      console.log(err);
    }
  }
}
</script>

<template>
  <div class="flex justify-center items-center flex-col">
    <div class="card w-120 bg-base-100 shadow-sm mt-6">
      <div class="title text-xl font-bold m-3">
        创建角色
      </div>
      <div class="card-body">
        <character-photo ref="photo-ref"/>
        <character-name ref="name-ref"/>
        <character-profile ref="profile-ref"/>
        <background-image ref="backgroundImage-ref"/>
      </div>

      <div v-if="errorMessage" class="text-red-300 text-center">{{ errorMessage }}</div>

      <div class="card-actions justify-center">
        <button @click="handleCreate" class="btn btn-accent w-60 my-3">创建角色</button>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
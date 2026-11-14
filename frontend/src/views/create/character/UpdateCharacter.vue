<script setup lang="ts">

import CharacterPhoto from "@/components/character/CharacterPhoto.vue";
import CharacterName from "@/components/character/CharacterName.vue";
import BackgroundImage from "@/components/character/BackgroundImage.vue";
import CharacterProfile from "@/components/character/CharacterProfile.vue";
import {onMounted, ref, useTemplateRef} from "vue";
import {base64ToFile} from "@/js/utils/base64_to_file.ts";
import api from "@/js/http/api.ts";
import {useUserStore} from "@/stores/user.ts";
import {useRoute, useRouter} from "vue-router";

const userStore = useUserStore();
const router = useRouter();
const route = useRoute();
const characterId = route.params.character_id;
const character = ref(null);

onMounted(async () => {
  try {
    const res = await api.get('/api/character/get_single/', {
      params: {character_id: characterId}
    });
    const data = res.data;
    if (data.result === 'success') {
      character.value = data.character;
    }
  } catch (err) {
    console.log(err);
  }
})

const photoRef = useTemplateRef("photo-ref")
const nameRef = useTemplateRef("name-ref")
const profileRef = useTemplateRef("profile-ref")
const backgroundImageRef = useTemplateRef("backgroundImage-ref")
const errorMessage = ref("");
async function handleUpdate() {
  const photo = photoRef.value?.myPhoto;
  const name = nameRef.value?.myName?.trim();
  const profile = profileRef.value?.myProfile?.trim();
  const backgroundImage = backgroundImageRef.value?.myBackgroundImage;
  errorMessage.value = "";

  if (!photo || !name || !profile || !backgroundImage) {
    errorMessage.value = "所有字段都是必填的";
  } else {
    const formData = new FormData();
    formData.append("character_id", characterId);
    formData.append("name", name);
    formData.append("profile", profile);

    if(photo !== character.value.photo){
      formData.append("photo", base64ToFile(photo, "photo.png"));
    }
    if(backgroundImage !== character.value.background_image) {
      formData.append("background_image", base64ToFile(backgroundImage, "background_image.png"));
    }
    try {
      const res = await api.post('/api/character/update/', formData);
      const data = res.data;
      if (data.result === 'success') {
        // console.log("角色信息更新成功");
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
  <div v-if="character" class="flex justify-center items-center flex-col">
    <div class="card w-120 bg-base-100 shadow-sm mt-6">
      <div class="title text-xl font-bold m-3">
        更新角色信息
      </div>
      <div class="card-body">
        <character-photo ref="photo-ref" :photo="character.photo"/>
        <character-name ref="name-ref" :name="character.name"/>
        <character-profile ref="profile-ref" :profile="character.profile"/>
        <background-image ref="backgroundImage-ref" :backgroundImage="character.background_image"/>
      </div>

      <div v-if="errorMessage" class="text-red-300 text-center">{{ errorMessage }}</div>

      <div class="card-actions justify-center">
        <button @click="handleUpdate" class="btn btn-accent w-60 my-3">更新</button>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
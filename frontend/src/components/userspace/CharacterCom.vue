<script setup lang="ts">
import {ref} from "vue";
import {useUserStore} from "@/stores/user.ts";
import RemoveCharacterIcon from "@/components/userspace/icons/RemoveCharacterIcon.vue";
import UpdateCharacterIcon from "@/components/userspace/icons/UpdateCharacterIcon.vue";
import api from "@/js/http/api.ts";

const props = defineProps(['character', 'canEdit']) //html中可以自动解包使用
const emit = defineEmits(['remove'])
const isHover = ref(false)
const userStore = useUserStore()

async function handleRemoveCharacter() {
  try {
    const res = await api.post('/api/character/remove/', {
      character_id: props.character.id
    })
    const data = res.data
    if (data.result === 'success') {
      emit('remove', props.character.id)
    }
  } catch (error) {
    console.log(error)
  }
}
</script>

<template>
  <div>
    <div class="avatar cursor-pointer" @mouseenter="isHover = true" @mouseleave="isHover = false">
      <div class="w-50 h-80 rounded-2xl relative">
        <img :src="character.background_image" class="transition-transform duration-300"  :class="{ 'scale-120': isHover }" alt="Avatar" />
        <div class="absolute left-0 top-50 w-50 h-full bg-linear-to-t from-black/60 to-transparent"> </div>

        <!-- 添加一个编辑和删除按钮 -->
        <div v-if="canEdit && character.author.id === userStore.id" class="absolute right-2 top-36">
          <router-link :to="{name:'update-character',params:{character_id:character.id}}" class="btn btn-circle btn-ghost bg-transparent">
            <UpdateCharacterIcon />
          </router-link>
          <button @click="handleRemoveCharacter"  v-if="canEdit" class="btn btn-circle btn-ghost bg-transparent">
            <RemoveCharacterIcon />
          </button>
        </div>

        <div class="avatar absolute left-4 top-50">
          <div class="w-10 rounded-full ring-3 ring-white">
            <img :src="character.photo" alt="Avatar" />
          </div>
        </div>

        <div class="absolute left-18 top-52">
          <div class="text-white font-semibold text-sm line-clamp-1 break-all">
            {{ character.name }}
          </div>
        </div>

        <div class="absolute left-4 top-63">
          <div class="text-white text-sm line-clamp-3 break-all">
            {{ character.profile }}
          </div>
        </div>
      </div>
    </div>
    <router-link :to="{name:'user-space', params:{user_id:character.author.id}}" class="flex items-center gap-2 pt-1 w-50">
      <div class="avatar">
        <div class="w-6 rounded-full ring-3 ring-white">
          <img :src="character.author.photo" alt="Avatar" />
        </div>
      </div>
      <div class=" font-semibold text-sm line-clamp-1 break-all">
        {{ character.author.username }}
      </div>
    </router-link>
  </div>
</template>

<style scoped>

</style>
<script setup lang="ts">

import MenuIcon from "@/components/navbar/icons/MenuIcon.vue";
import HomepageIcon from "@/components/navbar/icons/HomepageIcon.vue";
import CreateIcon from "@/components/navbar/icons/CreateIcon.vue";
import FriendIcon from "@/components/navbar/icons/FriendIcon.vue";
import SearcheIcon from "@/components/navbar/icons/SearcheIcon.vue";
</script>

<template>
<div class="drawer lg:drawer-open">
  <input id="my-drawer-4" type="checkbox" class="drawer-toggle inline" />
  <div class="drawer-content">
    <!-- Navbar -->
    <nav class="navbar w-full bg-base-200 shadow-base-sm">
      <div class="navbar-start">
        <label for="my-drawer-4" aria-label="open sidebar" class="btn btn-square btn-ghost drawer-button">
          <MenuIcon />
        </label>
        <div class="px-1.5 text-xl font-bold">AIFriends</div>
      </div>

      <div class="navbar-center">
        <div class="join">
          <input class="input join-item w-96 max-w-full rounded-l-full" placeholder="搜索你感兴趣的内容" />
          <button class="btn join-item rounded-r-full gap-0">
            <SearcheIcon />
            Search
          </button>
        </div>
      </div>

      <div class="navbar-end">
        <div class="aura">
          <button class="btn text-base">Sign in</button>
        </div>
      </div>

    </nav>
    <slot>  </slot>
  </div>

  <div class="drawer-side is-drawer-close:overflow-visible">
    <label for="my-drawer-4" aria-label="close sidebar" class="drawer-overlay"></label>
    <div class="flex min-h-full flex-col items-start bg-base-200 is-drawer-close:w-16 is-drawer-open:w-54">
      <!-- Sidebar content here -->
      <ul class="menu w-full grow">
        <!-- List item -->
        <li class="mt-10 my-2.5">
          <button class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-1.5" data-tip="首页">
            <!-- Home icon -->
            <HomepageIcon />
            <span class="is-drawer-close:hidden text-lg ml-2 whitespace-nowrap">Home</span>
          </button>
        </li>
        <!-- List item -->
        <li class="my-2.5">
          <button class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-1.5" data-tip="AI创作">
            <!-- Home icon -->
            <CreateIcon />
            <span class="is-drawer-close:hidden text-lg ml-2 whitespace-nowrap">Create AI</span>
          </button>
        </li>
        <!-- List item -->
        <li class="my-2.5">
          <button class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-1.5" data-tip="Friends">
            <!-- Home icon -->
            <FriendIcon />
            <span class="is-drawer-close:hidden text-lg ml-2 whitespace-nowrap">AI List</span>
          </button>
        </li>
        <!-- List item -->
        <li class="my-2.5">
          <button class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-1.5" data-tip="Settings">
            <!-- Settings icon -->
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor" class="my-1.5 inline-block size-6"><path d="M20 7h-9"></path><path d="M14 17H5"></path><circle cx="17" cy="17" r="3"></circle><circle cx="7" cy="7" r="3"></circle></svg>
            <span class="is-drawer-close:hidden text-lg ml-2 whitespace-nowrap">Settings</span>
          </button>
        </li>
      </ul>
    </div>
  </div>
</div>
</template>

<style scoped>

</style>
<script setup>
import DocumentationIcon from './icons/IconDocumentation.vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
</script>

<template>
  <div class="news-item flex flex-col sm:flex-row gap-2 pb-6 border-b-2 border-gray-100">

    <!-- Newsitem Date -->
    <div class="px-2 py-2 bg-teal-500 text-white flex flex-col items-left justify-center">
      <span class="text-sm flex gap-2">
        <span class="flex gap-1 items-center">

          <font-awesome-icon :icon="['fas', 'calendar-days']" />
        </span>
        <span class="flex gap-1 items-center">
          <slot name="date"></slot>
        </span>
      </span>


      <span class="text-2xl font-semibold flex gap-2">
        <span class="flex gap-1 items-center">
          <font-awesome-icon :icon="['far', 'clock']" />
        </span>
        <span class="flex gap-1 items-center">
                  <slot name="datetime"></slot>
        </span>
      </span>
    </div>
    <!--  -->
    <div class="flex flex-col justify-between">
      <!-- Author & Category -->
      <div class="flex md:gap-4 gap-2 text-sm text-gray-700 font-semibold">
        <span class="flex gap-1 items-center">
          <font-awesome-icon :icon="['far', 'user']" />
          <slot name="author"></slot>
        </span>
        <span class="flex gap-1 items-center">
          <font-awesome-icon :icon="['far', 'folder-closed']" />
          <slot name="category"></slot>
        </span>
      </div>
      <!-- Blog Titile -->
      <h3 class="text-2xl md:text-3xl font-semibold text-teal-900 capitalize chelsea-market-regular">
        <slot name="heading"></slot>
      </h3>
      <!-- Blog Description -->
      <p class="text-md text-gray-500">
        <slot></slot>
      </p>
    </div>

  </div>
</template>

<style scoped></style>

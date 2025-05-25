<script setup>
defineProps({
  imgsrc: String,
  text: String
})
</script>
<template>
                <a href="#"
            class="flex border items-center rounded-md cursor-pointer transition duration-500 shadow-sm hover:shadow-md hover:shadow-gray-400">
           
                    <div class="w-12 p-1 shrink-0">
                        <img :src="imgsrc" :alt="text" class="h-12 w-12">
                    </div>
                    <div class="p-0">
                        <p class="font-semibold text-pretty">{{ text }}</p>
                        <span class="text-gray-600"></span>
                    </div>
                </a>
</template>


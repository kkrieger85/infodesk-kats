<script setup>
import Newsfeed from './components/Newsfeed.vue'
import OSM from './components/OSM.vue'
import Organization from './components/Organization.vue'
import Legende from './components/Legende.vue'

import { ref } from 'vue'
let customMarkers = ref([])

function updateCustomMarkers(markers) {
  customMarkers.value = markers
}
</script>

<template>
  <main>
    <div class="einsatz w-full text-center">
                  <h2 class="text-3xl font-bold sm:text-4xl mb-4">
Saar Hackathon #7 PASCALSCHACHT, DUDWEILER</h2>
</div>
    <div class="map">
      <OSM :customMarkers="customMarkers" @customMarkers="updateCustomMarkers" />
    </div>
    <div class="legende" v-if="customMarkers.length > 0">
      <Legende :customMarkers="customMarkers" />
    </div>
  </main>
  <aside>
    <div class="org flex items-center justify-center m-4">
      <Organization></Organization>
    </div>
    <div class="newsfeed m-4">
      <Newsfeed />
    </div>
  </aside>
</template>

<style scoped>

</style>

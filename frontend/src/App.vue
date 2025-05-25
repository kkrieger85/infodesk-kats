<script setup>
import Newsfeed from './components/Newsfeed.vue'
import OSM from './components/OSM.vue'
import Organization from './components/Organization.vue'
import Legende from './components/Legende.vue'

import { ref } from 'vue'
import { stringify } from 'postcss'
import { onMounted } from 'vue'
let customMarkers = ref([])

function updateCustomMarkers(markers) {
  customMarkers.value = markers
  saveMarkers(customMarkers)

}

function saveMarkers(customMarkers) {
  var layerData;
  layerData = { type: "Zeichen", data: JSON.stringify(customMarkers.value) }
  // Hier könnten die Marker gespeichert werden, z.B. an einen API-Endpunkt
  console.log('Zeichen saved:', customMarkers.value)
  if (customMarkers._id) {
    fetch(`http://localhost:80/locations/${customMarkers._id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(layerData)
    })
      .then(response => response.json())
      .then(result => console.log("Updated:", result))
      .catch(error => console.error("Error:", error));
  } else {
    fetch('http://localhost:80/locations/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(layerData)
    })
      .then(response => response.json())
      .then(result => {
        customMarkers._id = result.id;
        console.log("Saved:", result);
      })
      .catch(error => console.error("Error:", error));
  }
}



function loadMarkers() {
  fetch('http://localhost:80/locations/Zeichen')
    .then(response => {
      if (!response.ok) throw new Error('Network response was not ok');
    })
    .then(data => {
      if (data && data.data) {
        customMarkers.value = JSON.parse(data.data);
        updateCustomMarkers(customMarkers.value);

        console.log('Zeichen loaded:', customMarkers.value);
      } else {
        console.warn('No zeichen found');
      }
    })
    .catch(error => console.error('Error loading markers:', error));
}

// Beim ersten Initialisieren laden
onMounted(() => {
  loadMarkers()
})


</script>

<template>
  <main>
    <div class="einsatz w-full text-center">
      <h2 class="text-3xl font-bold sm:text-4xl mb-4">
        What the Hack #7 PASCALSCHACHT, DUDWEILER</h2>
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

<style scoped></style>

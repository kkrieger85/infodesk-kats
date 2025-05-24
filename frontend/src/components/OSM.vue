<template>
    <l-map ref="mapRef" v-model:zoom="zoom" v-model:center="center" :useGlobalLeaflet="false">
        <l-tile-layer url="http://localhost:8080/tile/{z}/{x}/{y}.png" layer-type="base"
            name="Stadia Maps Basemap"></l-tile-layer>
        <l-marker :lat-lng="center">
            <l-icon :icon-url="iconExplosionUrl" :icon-size="iconSize" />
        </l-marker>
        <l-marker :lat-lng="centerSammel">
            <l-icon :icon-url="iconSammelpunktUrl" :icon-size="iconSize" />
        </l-marker>
        <l-marker
            v-for="(marker, idx) in customMarkers"
            :key="idx"
            :lat-lng="marker.latlng"
        >
            <l-icon :icon-url="marker.iconUrl" :icon-size="iconSize" />
        </l-marker>
        <l-control position="bottomleft" >
            <button @click="selectCustomIcon">
            Add custom marker</button>
        </l-control>
    </l-map>
    <MultiselectIconPicker
  v-if="showIconPicker"
  @close="showIconPicker = false"
  @select="addCustomMarker"
/>
</template>


<script setup>
import "leaflet/dist/leaflet.css"
import MultiselectIconPicker from "./MultiselectIconPicker.vue"
import { ref } from "vue"
import { LMap, LTileLayer, LMarker, LIcon, LControl } from "@vue-leaflet/vue-leaflet"

let showIconPicker = ref(false)
let selectedIcon = ref(null)

let zoom = ref(18)
let center = ref([49.2725, 7.0336])
let centerSammel = [49.272865, 7.034289]

let iconExplosionUrl = "/src/assets/taktische_zeichen/Gefahren/Akute_Gefahr_durch_Explosion.svg"
let iconSammelpunktUrl = "/src/assets/taktische_zeichen/Einrichtungen/Sammelstelle.svg"
let iconOtherUrl = "/src/assets/taktische_zeichen/Einrichtungen/Andere.svg" // Beispiel für weiteres Icon

let iconSize = [50, 50];;

let customMarkers = ref([])
let mapRef = ref(null)


function selectCustomIcon() {
    showIconPicker.value = true
}

function addCustomMarker(icon) {
    // Einfache Auswahl per prompt (besser: eigenes Modal)
    showIconPicker.value = false
    if (!icon) return
    selectedIcon.value = icon

    // Nutzer klickt auf die Karte, um Position zu wählen
    const mymap = mapRef.value.leafletObject
    const onClick = (e) => {
        customMarkers.value.push({
            latlng: [e.latlng.lat, e.latlng.lng],
            iconUrl: icon.url
        })
        mymap.off('click', onClick)
    }
    mymap.once('click', onClick)
    //alert("Klicke auf die Karte, um den Marker zu platzieren.")
}

</script>

<style lang="css">
#map {
    height: 600px;
}
</style>
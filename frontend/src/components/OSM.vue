<template>
    <l-map ref="mapRef" v-model:zoom="zoom" v-model:center="center" :useGlobalLeaflet="false">
        <l-tile-layer url="http://localhost:8080/tile/{z}/{x}/{y}.png" layer-type="base"
            name="Stadia Maps Basemap"></l-tile-layer>
        <l-marker v-for="(marker, idx) in customMarkers" :key="idx" :lat-lng="marker.latlng">
            <l-icon :icon-url="marker.iconUrl" :icon-size="iconSize" />
        </l-marker>
        <l-control position="bottomleft">
            <button @click="selectCustomIcon"
                class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded">
                Zeichen</button>
        </l-control>
    </l-map>
    <MultiselectIconPicker v-if="showIconPicker" @close="showIconPicker = false" @select="addCustomMarker" />
</template>


<script setup>
import "leaflet/dist/leaflet.css"
import MultiselectIconPicker from "./MultiselectIconPicker.vue"
import { ref, watch, defineProps, defineEmits } from "vue"
import { LMap, LTileLayer, LMarker, LIcon, LControl } from "@vue-leaflet/vue-leaflet"

const props = defineProps({ customMarkers: Array })
const emit = defineEmits(["customMarkers"])

let localMarkers = ref(props.customMarkers || [])


let showIconPicker = ref(false)

let zoom = ref(18)
let center = ref([49.2725, 7.0336])

let iconSize = [50, 50];;

let mapRef = ref(null)


function selectCustomIcon() {
    showIconPicker.value = true
}

function addCustomMarker(icon) {
    showIconPicker.value = false
    if (!icon) return

    // Nutzer klickt auf die Karte, um Position zu wählen
    const mymap = mapRef.value.leafletObject
    const onClick = (e) => {
        localMarkers.value.push({
            latlng: [e.latlng.lat, e.latlng.lng],
            iconUrl: icon.url,
            name: icon.name
        })
        emit("customMarkers", localMarkers.value)
        mymap.off('click', onClick)
    }
    mymap.once('click', onClick)

}

</script>

<style lang="css"></style>
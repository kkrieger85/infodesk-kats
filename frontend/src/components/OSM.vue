<template>
    <l-map ref="map" v-model:zoom="zoom" v-model:center="center" :useGlobalLeaflet="false">
        <l-tile-layer url="http://localhost:8080/tile/{z}/{x}/{y}.png" layer-type="base"
            name="Stadia Maps Basemap"></l-tile-layer>
    </l-map>
</template>


<script setup>
import "leaflet/dist/leaflet.css"
import { LMap, LTileLayer } from "@vue-leaflet/vue-leaflet"


let zoom = 19
let center = [49.2725, 7.0336]
</script>

<style lang="css">
#map {
    height: 600px;
}
</style>
<template>
    <l-map ref="map" v-model:zoom="zoom" v-model:center="center" :useGlobalLeaflet="false">
        <l-tile-layer url="http://localhost:8080/tile/{z}/{x}/{y}.png" layer-type="base"
            name="Stadia Maps Basemap"></l-tile-layer>
        <l-marker :lat-lng="center">
            <l-icon :icon-url="iconExplosionUrl" :icon-size="iconSize" />
        </l-marker>
        <l-marker :lat-lng="centerSammel">
            <l-icon :icon-url="iconSammelpunktUrl" :icon-size="iconSize" />
        </l-marker>
    </l-map>
</template>


<script setup>
import "leaflet/dist/leaflet.css"
import { LMap, LTileLayer, LMarker, LIcon } from "@vue-leaflet/vue-leaflet"


let zoom = 18
let center = [49.2725, 7.0336]
let centerSammel = [49.272865, 7.034289]

let iconExplosionUrl = "/src/assets/taktische_zeichen/Gefahren/Akute_Gefahr_durch_Explosion.svg"
let iconSammelpunktUrl = "/src/assets/taktische_zeichen/Einrichtungen/Sammelstelle.svg"
let iconSize = [50, 50];;

</script>

<style lang="css">
#map {
    height: 600px;
}
</style>
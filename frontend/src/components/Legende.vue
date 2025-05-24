<template>
    <h2>Legende</h2>

    <LegendeItem v-for="(marker, idx) in customMarkers" :key="idx" :imgsrc="marker.iconUrl" :text="marker.name">
        <template #icon="{ imgsrc, text }">
            <img :src="imgsrc" :alt="text" />
            <DocumentationIcon />
        </template>
        <template #explanation="{ text }">{{ text }}</template>
    </LegendeItem>

</template>
<script setup>
import DocumentationIcon from './icons/IconDocumentation.vue'
import LegendeItem from './LegendeItem.vue'

defineProps({ customMarkers: Array })




</script>
<style lang="css">
img {
    width: 60px;
}
</style>
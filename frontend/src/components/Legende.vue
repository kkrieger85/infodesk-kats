<template>
    <div class="mx-20 mt-20 w-Full p-4 shadow-md rounded-lg">
        <div class="flex justify-between pb-4">
            <p class="font-bold text-xl">Legende</p>
        </div>

        <div class="grid gap-1  grid-cols-3 md:grid-cols-4 lg:grid-cols-5" id="accordion-collapse-body-1">
            <LegendeItem v-for="(marker, idx) in uniqueMarkers" :key="idx" :imgsrc="marker.iconUrl" :text="marker.name">
            </LegendeItem>
        </div>

    </div>
</template>
<script setup>
import DocumentationIcon from './icons/IconDocumentation.vue'
import LegendeItem from './LegendeItem.vue'

import { computed } from 'vue'
const props = defineProps({ customMarkers: Array })

const uniqueMarkers = computed(() => {
    const seen = new Set()
    return (props.customMarkers || []).filter(marker => {
        const key = marker.iconUrl + '|' + marker.name
        if (seen.has(key)) return false
        seen.add(key)
        return true
    })
})
</script>
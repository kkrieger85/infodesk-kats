<template>
    <div>
        <input v-model="search" type="text" placeholder="Icon suchen..." class="icon-search" />
        <div class="icon-list">
            <div v-for="icon in filteredIcons" :key="icon.url" class="icon-item" :class="{ selected: isSelected(icon) }"
                @click="toggleSelect(icon)">
                <img :src="icon.url" :alt="icon.name" class="icon-img" />
                <span>{{ icon.name }}</span>
            </div>
        </div>
    </div>
</template>

<script setup>
const iconModules = import.meta.glob('/src/assets/taktische_zeichen/**/*.svg', { eager: true, as: 'url' })
const icons = ref(
    Object.entries(iconModules).map(([path, url]) => ({
        name: path.split('/').pop().replace('.svg', ''),
        url
    }))
)
import { ref, computed, defineEmits } from "vue"

const emit = defineEmits(["select", "close"])
const search = ref("")
const selectedIcons = ref([])

const filteredIcons = computed(() =>
    icons.value.filter(
        (icon) =>
            icon.name.toLowerCase().includes(search.value.toLowerCase()) ||
            icon.url.toLowerCase().includes(search.value.toLowerCase())
    )
)

function toggleSelect(icon) {
    const idx = selectedIcons.value.findIndex((i) => i.url === icon.url)
    if (idx === -1) {
        selectedIcons.value.push(icon)
    } else {
        selectedIcons.value.splice(idx, 1)
    }
    emit("select", icon)
    emit("close")
}

function isSelected(icon) {
    return selectedIcons.value.some((i) => i.url === icon.url)
}

// Exportiere die Auswahl für den Parent
defineExpose({ selectedIcons })
</script>

<style scoped>
.icon-search {
    width: 100%;
    margin-bottom: 8px;
    padding: 4px;
}

.icon-list {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    max-height: 200px;
    overflow-y: auto;
}

.icon-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 2px solid transparent;
    padding: 4px;
    cursor: pointer;
    width: 80px;
}

.icon-item.selected {
    border-color: #007bff;
    background: #e6f0ff;
}

.icon-img {
    width: 40px;
    height: 40px;
    object-fit: contain;
    margin-bottom: 4px;
}
</style>
<template>
    <div class="modal-backdrop" @click.self="emit('close')">
        <div class="modal-content" style="position:relative;">
            <button class="close-btn" @click="emit('close')" aria-label="Schließen">&times;</button>
            <input v-model="search" type="text" placeholder="Icon suchen..." class="icon-search" />
            <div class="icon-list">
                <div v-for="icon in filteredIcons" :key="icon.url" class="icon-item" :class="{ selected: isSelected(icon) }"
                    @click="toggleSelect(icon)">
                    <img :src="icon.url" :alt="icon.name" class="icon-img" />
                    <span class="item-name">{{ icon.name }}</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
const iconModules = import.meta.glob('/src/assets/taktische_zeichen/**/*.svg', { eager: true, query: '?url', import: 'default' })
const icons = ref(
    Object.entries(iconModules).map(([path, url]) => ({
        name: path.split('/').pop().replace('.svg', '').replaceAll('-', ' '),
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
.modal-backdrop {
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.4);
    z-index: 1000;
    display: flex;
    align-items: center;
    justify-content: center;
}

.modal-content {
    background: #fff;
    border-radius: 12px;
    padding: 24px 20px 16px 20px;
    min-width: 320px;
    max-width: 90vw;
    max-height: 80vh;
    box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    display: flex;
    flex-direction: column;
    align-items: stretch;
}

.icon-search {
    width: 100%;
    margin-bottom: 12px;
    padding: 6px 8px;
    border-radius: 6px;
    border: 1px solid #ccc;
    font-size: 1rem;
}

.icon-list {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    max-height: 50vh;
    overflow-y: auto;
    justify-content: flex-start;
}

.icon-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 2px solid transparent;
    padding: 6px;
    cursor: pointer;
    width: 80px;
    border-radius: 8px;
    transition: border-color 0.2s, background 0.2s;
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

.item-name {
    font-size: 0.675rem;
    text-align: center;
    color: #333;
    max-width: 80px;
    overflow: break-word;
    text-overflow: ellipsis;
}

.close-btn {
    position: absolute;
    top: 18px;
    right: 24px;
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: #888;
}
</style>
<template>
    <h2>Legende</h2>
    <LegendeItem>
        <template #icon>
            <img src="../assets/taktische_zeichen/Sonstiges/Ausgangspunkt.svg" alt="">
            <DocumentationIcon />
        </template>
        <template #explanation>Eigener Standort</template>
    </LegendeItem>
    <LegendeItem>
        <template #icon>
            <img src="../assets/taktische_zeichen/Gefahren/Akute_Gefahr_durch_Explosion.svg" alt="">
            <DocumentationIcon />
        </template>
        <template #explanation>Akute Gefahr durch Explosion</template>
    </LegendeItem>
    <LegendeItem>
        <template #icon>
            <img src="../assets/taktische_zeichen/Einrichtungen/Sammelstelle.svg" alt="">
            <DocumentationIcon />
        </template>
        <template #explanation>Sammelstelle Turnhalle Dudweiler</template>
    </LegendeItem>
</template>
<script setup>
import DocumentationIcon from './icons/IconDocumentation.vue'
import LegendeItem from './LegendeItem.vue'
</script>
<style lang="css">
img {
    width: 60px;
}
</style>
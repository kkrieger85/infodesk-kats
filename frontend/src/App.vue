<script setup>
import Newsfeed from './components/Newsfeed.vue'
import OSM from './components/OSM.vue'
import Organization from './components/Organization.vue'
import Legende from './components/Legende.vue'
</script>

<template>
  <main>
    <div class="map">
      <OSM />
    </div>
    <div class="legende">
      <Legende></Legende>
    </div>

  </main>
  <aside>
    <div class="org">
      <Organization></Organization>

    </div>
    <div class="newsfeed">
      <Newsfeed />

    </div>

  </aside>
  
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (max-width: 800px) {
  .org {
    display: none;
  }
}
@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>

<script setup>
import NewsItem from './NewsItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'

</script>


<template>
  <div class="w-full flex flex-col items-stretch justify-center">

    <h2 class="text-center text-4xl font-bold ">Liveticker</h2>
    <h3 class="text-center text-l pb-4">2025 <span class="font-bold">Mai</span></h3>
    <NewsItem>
      <template #date>25.05.</template>
      <template #datetime>16:00</template>
      <template #author>Kevin</template>
      <template #category>Hackathon</template>

      <span class="text-4xl">🎤</span>Presentation der Ergebnisse des Hackathon-Wochenendes!
    </NewsItem>

    <NewsItem>
      <template #date>25.05.</template>
      <template #datetime>13:37</template>
      <template #author>Kevin</template>
      <template #category>Hackathon</template>
      <span class="text-4xl">🎉</span>
      Projekt erreicht Version 0.1.0!
    </NewsItem>


    <NewsItem>
      <template #date>25.05.</template>
      <template #datetime>12:45</template>
      <template #author>Kevin</template>
      <template #category>Hackathon</template>
      <span class="text-4xl">🍕</span>
      Need more 🍕 for better <code>code</code>
    </NewsItem>

    <NewsItem>
      <template #date>25.05.</template>
      <template #datetime>10:00</template>
      <template #author>Kevin</template>
      <template #category>Hackathon</template>
      <span class="text-4xl">🚀</span>

      Round 2 of the Hackathon Weekend is starting! We are ready to go! 🚀
    </NewsItem>

    <NewsItem>
      <template #date>25.05.</template>
      <template #datetime>09:30</template>
      <template #author>Kevin</template>
      <template #category>Hackathon</template>
      <span class="text-4xl">☕️</span>
      coffee is ready, let's start the Hackathon Weekend!
      <br />
      I need more coffee! <br /><span class="text-4xl">☕️</span><span class="text-4xl">☕️</span><span
        class="text-4xl">☕️</span>
    </NewsItem>
  </div>
</template>
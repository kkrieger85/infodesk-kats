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
    <template #datetime>13:37</template>
    <template #author>Kevin</template>
    <template #category>Hackathon</template>

    Vue’s
    <a href="https://vuejs.org/" target="_blank" rel="noopener">official documentation</a>
    provides you with all information you need to get started.
  </NewsItem>


  <NewsItem>
    <template #date>25.05.</template>
    <template #datetime>12:45</template>
    <template #author>Kevin</template>
    <template #category>Hackathon</template>

    This project is served and bundled with
    <a href="https://vite.dev/guide/features.html" target="_blank" rel="noopener">Vite</a>. The
    recommended IDE setup is
    <a href="https://code.visualstudio.com/" target="_blank" rel="noopener">VSCode</a>
    +
    <a href="https://github.com/johnsoncodehk/volar" target="_blank" rel="noopener">Volar</a>. If
    you need to test your components and web pages, check out
    <a href="https://www.cypress.io/" target="_blank" rel="noopener">Cypress</a>
    and
    <a href="https://on.cypress.io/component" target="_blank" rel="noopener">Cypress Component Testing</a>.

    <br />

    More instructions are available in <code>README.md</code>.
  </NewsItem>

  <NewsItem>
    <template #date>25.05.</template>
    <template #datetime>10:00</template>
    <template #author>Kevin</template>
    <template #category>Hackathon</template>

    Get official tools and libraries for your project:
    <a href="https://pinia.vuejs.org/" target="_blank" rel="noopener">Pinia</a>,
    <a href="https://router.vuejs.org/" target="_blank" rel="noopener">Vue Router</a>,
    <a href="https://test-utils.vuejs.org/" target="_blank" rel="noopener">Vue Test Utils</a>, and
    <a href="https://github.com/vuejs/devtools" target="_blank" rel="noopener">Vue Dev Tools</a>. If
    you need more resources, we suggest paying
    <a href="https://github.com/vuejs/awesome-vue" target="_blank" rel="noopener">Awesome Vue</a>
    a visit.
  </NewsItem>

  <NewsItem>
    <template #date>25.05.</template>
    <template #datetime>09:30</template>
    <template #author>Kevin</template>
    <template #category>Hackathon</template>

    Got stuck? Ask your question on
    <a href="https://chat.vuejs.org" target="_blank" rel="noopener">Vue Land</a>, our official
    Discord server, or
    <a href="https://stackoverflow.com/questions/tagged/vue.js" target="_blank" rel="noopener">StackOverflow</a>.
    You
    should also subscribe to
    <a href="https://news.vuejs.org" target="_blank" rel="noopener">our mailing list</a>
    and follow the official
    <a href="https://twitter.com/vuejs" target="_blank" rel="noopener">@vuejs</a>
    twitter account for latest news in the Vue world.
  </NewsItem>
        </div>  
</template>
import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

import VueQrcode from '@chenfengyuan/vue-qrcode';

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
/* import specific icons */
import { fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import {fab } from '@fortawesome/free-brands-svg-icons'

/* add icons to the library */
library.add(fas, far, fab)
const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.component(VueQrcode.name, VueQrcode);
app.mount('#app')

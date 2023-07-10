import { createApp } from 'vue'
import App from './App.vue'
import CatalogSection from '../src/components/CatalogSection.vue'
import CarouselUniversal from './components/CarouselUniversal.vue'
import CardsItem from '../src/components/CardsItem.vue'
import CatalogDropdownDesktop from './components/CatalogDropdownDesktop.vue'
import router from './router'
import store from './vuex'
import './assets/tailwind.css'

const app = createApp(App).use(router).use(store)

app.component('CatalogSection', CatalogSection)

app.component('CarouselUniversal', CarouselUniversal)

app.component('CatalogDropdownDesktop', CatalogDropdownDesktop)

app.component('CardsItem', CardsItem)

app.mount('#app')
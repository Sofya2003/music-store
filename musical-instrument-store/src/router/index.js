import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '../components/MainPage.vue'
import CatalogSection from '../components/CatalogSection.vue'
import ProductPage from '../components/ProductPage'
import BlogPage from '../components/BlogPage'
import LoginPage from '../components/LoginPage'
import RegisterPage from '../components/RegisterPage'

const routes = [
  {
    path: '/',
    name: 'MainPage',
    component: MainPage
  },
  {
    path: '/catalogsection/:catalogcategory',
    name: 'CatalogSection',
    component: CatalogSection
  },
  {
    path: '/product/:id',
    name: 'ProductPage',
    component: ProductPage
  },
  {
    path: '/blog',
    name: 'BlogPage',
    component: BlogPage
  },
  {
    path: '/login',
    name: 'LoginPage',
    component: LoginPage
  },
  {
    path: '/register',
    name: 'RegisterPage',
    component: RegisterPage
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
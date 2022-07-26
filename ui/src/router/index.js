import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import UserPage from '../views/UserPage.vue'
import GalleryPage from '../views/GalleryPage.vue'
import GalleryAdmin from '../views/GalleryAdmin.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/userpage',
    name: 'UserPage',
    component: UserPage,    
  }, 
  {
    path: '/gallerypage',
    name: 'GalleryPage',
    component: GalleryPage,
  }, 
  {
    path: '/galleryadmin/:galleryId',
    name: 'GalleryAdmin',
    component: GalleryAdmin,    
  }, 
]
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
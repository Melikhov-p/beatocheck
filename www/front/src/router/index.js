import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      'path': '/beat/:id',
      'name': 'beat_detail',
      'component': () => import('../views/BeatView.vue')
    },
    {
      path: '/auth',
      name: 'auth',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AuthView.vue')
    },
    {
      path: '/studio',
      'name': 'studio',
      component: () => import('../views/StudioView.vue'),
      children: [
        {
          path: '/add_track',
          'name': 'add_track',
          component: () => import('../views/AddBeatView.vue')
        }
      ]
    },
    {
      path: '/@:username',
      name: 'profile',
      component: () => import('../views/ProfileView.vue')
    }
  ]
})

export default router

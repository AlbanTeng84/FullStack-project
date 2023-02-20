import { createRouter, createWebHistory } from 'vue-router';
import Jobs from '../components/Jobs.vue'
import PostData from '../components/PostData.vue'


const routes = [ 
  {
    path: '/jobs',
    name: 'Jobs',
    component: Jobs,
  },
  {
    path: '/postdata',
    name: 'PostData',
    component: PostData,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

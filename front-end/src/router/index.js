import { createRouter, createWebHistory } from 'vue-router';
// import Jobs from '../components/Jobs.vue';
// import PostData from '../components/PostData.vue';
import Get from '..components/Get.vue';


const routes = [ 
  // {
  //   path: '/jobs',
  //   name: 'Jobs',
  //   component: Jobs,
  // },
  // {
  //   path: '/postdata',
  //   name: 'PostData',
  //   component: PostData,
  // },
  {
    path: '/get',
    name: 'Get',
    component: Get,
  },

];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

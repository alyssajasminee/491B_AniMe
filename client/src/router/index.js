import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import GenresView from '../views/GenresView.vue';
import Lists from '../views/Lists.vue';
import { authGuard } from '../auth/authGuard'

Vue.use(VueRouter);

const routes = [{
        path: '/',
        name: 'Home',
        component: Home,
    },

    {
        path: '/user/lists',
        name: 'Lists',
        component: Lists,
    },
    {
        path: '/genres',
        name: 'GenresView',
        component: GenresView,
    },
    {
        path: '/profile',
        name: 'Profile',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ('../views/UserProfile.vue'),
        beforeEnter: authGuard
    },
    {
        path: '/profile/:id',
        name: 'userProfile',
        component: () =>
            import ('../views/UserProfile.vue')
    },
    {
        path: '/edit-profile',
        name: 'ProfileEdit',
        component: () =>
            import ('../views/EditProfile.vue')
  },
  {
    path: '/search-results',
    name: 'searchResults',
    component: () =>
      import('../components/SearchResultsPage.vue')
  }
];
const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

export default router;

import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import SignIn from '../components/SignIn.vue';
import Lists from '../views/Lists.vue';

Vue.use(VueRouter);

const routes = [{
  path: '/',
  name: 'Home',
  component: Home,
},
{
  path: '/signin',
  name: 'SignIn',
  component: SignIn,
},
{
  path: '/user/lists',
  name: 'Lists',
  component: Lists,
},
];
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;

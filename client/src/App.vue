<template>
  <div id="app" class="text-center">
    <Nav />
    <router-view />
  </div>
</template>
<script>
import Nav from './components/Nav.vue';
export default {
  name: 'app',
  components: {
    Nav
  }
  }
  </script>

<template>
  <div class="home">
    <HomeView msg="Welcome to Our App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HomeView from '@/components/HomeView.vue';

export default {
  name: 'HomeView',
  components: {
    HomeView,
  },
};
</script>

<template>
  <div class="home" id="pic-back">
    <div id="header">
      <h1 class="display-1 font-weight-bold"> AniMe
      </h1>
      <h2> Explore and find new animes. </h2>
    </div>
    <HomeView/>
  </div>
</template>

<style>
#header{
  margin-top: 15%;
  opacity: 1;
  background-size: auto;
}
#pic-back::before{
  top:0;
  top: 0;
  right: 0;
  left: 0;
  content: '';
  background-image:url('~@/assets/anime_home_background.jpg');
  height: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  opacity: 0.3;
  position: absolute;
  z-index: -1;
  width:100%;
}

</style>

<script>
// @ is an alias to /src
import HomeView from '@/components/HomeView.vue';

export default {
  name: 'Home',
  components: {
    HomeView,
  },
};
</script>

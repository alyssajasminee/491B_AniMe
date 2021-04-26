<template>
  <div class="main-background p-5 m-5" >
    
    <Genres />
   
  </div>
</template>

<style scoped>
body{
  background-color: hsl(224, 19%, 44%);
  height:auto;
  position: absolute;
  width:100%;
}
.btn.user-info{
  height:50px;
}
</style>

<script>
// @ is an alias to /src
import Genres from '@/components/Genres.vue';


export default {
  name: 'GenreView',
  components: {
    Genres,
  },
};
</script>

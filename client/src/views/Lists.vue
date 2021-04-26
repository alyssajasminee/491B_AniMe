<template>
  <div class="main-background p-5 m-5" >
    
    <MyList />
   
  </div>
</template>

<style>
html{
  background-color: hsl(218.24, 87.39%, 92.07%) !important;
  
}
.btn.user-info{
  height:50px;
}
</style>

<script>
// @ is an alias to /src
import MyList from '@/components/MyList.vue';


export default {
  name: 'Lists',
  components: {
    MyList,
  },
};
</script>

<template>
  <div class="main-background p-5" >
    
    <MyList />
   
  </div>
</template>

<style scoped>
html body{
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
import MyList from '@/components/MyList.vue';


export default {
  name: 'Lists',
  components: {
    MyList,
  },
};
</script>

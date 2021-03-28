<template>
  <div class="main-background p-5" >
    <div class="row justify-content-between">
      <h1 class="display-1 font-weight-bold"> AniMe</h1>
      <button class="user-info btn btn-secondary rounded-pill px-5">user </button>
    </div>
    <MyList />
    <GenreLists />
  </div>
</template>

<style>
.main-background{
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
import GenreLists from '../components/GenreLists.vue';

export default {
  name: 'Lists',
  components: {
    MyList,
    GenreLists,
  },
};
</script>

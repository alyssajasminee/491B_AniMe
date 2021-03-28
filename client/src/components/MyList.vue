<template>
  <div class="my_list">
    <h2  class="text-left pb-4 display-4 font-weight-bold"> My Picks</h2>
    <div  class="d-flex flex-wrap">
      <div  class="list-card" v-for="(show, index) in mylist" :key="index"
      :id="show.anime_id">
      <div class="justify-content-center">
        <h5 class="py-3">{{show.title}}</h5>
        <h6 class="pb-3">{{show.type}}</h6>
      </div>
      </div>
    </div>
 </div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'MyList',
  data() {
    return {
      mylist: [],
    };
  },
  methods: {
    getAnimes() {
      const path = 'http://localhost:5000/mypicks';
      axios.get(path)
        .then((response) => {
          this.mylist = response.data;
        });
    },
  },
  created() {
    this.getAnimes();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

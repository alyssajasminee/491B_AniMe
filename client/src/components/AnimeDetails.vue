<template>
<div>
<div class="my_list" v-for="(name,show,index) in glist" :key="index">
    <div  v-for="(id,index) in name" :key="index" :id="index">
        <h2  class="text-left pb-4 display-4 font-weight-bold">{{index}}</h2>
        <div class="d-flex flex-wrap">
            <a class="list-card margin-auto" v-for="item in id" :key="item"
            :href="'#'+item.anime_id">
              <div class="m-auto">
                <h5 class="py-3">{{item.title}}</h5>
                <h6 class="pb-3">{{item.type}}</h6>
              </div>
            </a>
        </div>
    </div>
</div>
</div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'GenreLists',
  data() {
    return {
      glist: [],

    };
  },
  methods: {
    getAnimes() {
      const path = 'http://localhost:5000/genres';
      axios.get(path)
        .then((response) => {
          this.glist = response.data;
        });
    },
  },
  created() {
    this.getAnimes();
  },
};
</script>

<template>
<div>
  <div class="my_list">
    <h2  class="text-left pb-4 display-4 font-weight-bold"> My Picks</h2>
    <div  class="d-flex flex-wrap">
      <div  class="list-card" v-for="(show, index) in mylist" :key="index"
      :id="show.anime_id" @click="animeModal(show.anime_id)">
      <div class="justify-content-center">
        <h5 class="py-3">{{show.title}}</h5>
        <h6 class="pb-3">{{show.type}}</h6>
      </div>
      </div>
    </div>
 </div>
 <div>
  <div class="my_list" v-for="(name,show,index) in glist" :key="index">
      <div  v-for="(id,index) in name" :key="index" :id="index">
          <h2  class="text-left pb-4 display-4 font-weight-bold">{{index}}</h2>
          <div class="d-flex flex-wrap">
              <div class="list-card margin-auto" v-for="item in id" :key="item.anime_id"
               @click="animeModal(item.anime_id)">
                <div class="m-auto">
                  <h5 class="py-3">{{item.title}}</h5>
                  <h6 class="pb-3">{{item.type}}</h6>
                </div>
              </div>
          </div>
      </div>
  </div>
  <div id="myModal" ref="myModal" class="modal">

    <!-- Modal content -->
    <div class="modal-content" v-for="(d,index) in details" :key="index">
      <button  @click="close()" class=" close btn text-right">x</button>
      <div class="d-flex">
        <div>
          <h3>{{d.title}}</h3>
          <p>{{d.type}}</p>
        </div>
        <span class=" px-4 font-weight-bold" @click="addAnime(d.anime_id)"> + </span>
        <span class="px-4 font-weight-bold" @click="removeAnime(d.anime_id)"> Remove</span>
      </div>
      <p>{{d.synopsis}}</p>
      <p>Producers: <span v-for="(p, index) in d.producer" :key="index">{{p}}, </span></p>
      <p>Aired: {{d.aired}}</p>
      <p>Studio: <span v-for="(s, index) in d.studio" :key="index">{{s}},</span></p>
      <p> Rate this: </p> 
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
      glist: [],
      details: [],
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
    getGenres() {
      const path = 'http://localhost:5000/genres';
      axios.get(path)
        .then((response) => {
          this.glist = response.data;
        });
    },
    animeModal(id) {
      console.log(id);
      const path = `http://localhost:5000/anime/${id}`;
      axios.get(path)
        .then((response) => {
          this.details = response.data;
        });
      this.$refs.myModal.style.display = 'block';
    },
    close() {
      this.$refs.myModal.style.display = 'none';
    },
    addAnime(id){
      const path = `http://localhost:5000/addAnime/${id}`
      axios.patch(path,{Username:"acervantes"},{ headers: { 'Content-Type': 'application/x-www-form-urlencoded' }})
      this.getAnimes
     
    },
    removeAnime(id){
      const path = `http://localhost:5000/RemoveAnime/${id}`
      axios.patch(path,{})
    }
  },
  created() {
    this.getAnimes();
    this.getGenres();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* The Modal (background) */
#myModal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  padding-top: 100px; /* Location of the box */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

/* Modal Content */
.modal-content {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 45%;
  text-align:left;
}

/* The Close Button */
.close {
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  }
</style>

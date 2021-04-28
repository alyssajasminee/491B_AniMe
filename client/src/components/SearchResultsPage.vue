<template>
  <div>
    <div id="mypicks" ref="mypicks" class="my_list">
      <h2 class="text-left pb-4 display-4 font-weight-bold">Results for '{{query}}'</h2>
      <div class="d-flex flex-wrap">
        <div class="list-card" v-for="(show, index) in searchlist" :key="index"
             :id="show.anime_id" @click="animeModal(show.anime_id)">
          <div class="m-auto">
            <h5 class="h6 py-3 font-weight-bold">{{show.title}}</h5>
            <h6 class="pb-3 font-weight-bold">{{show.type}}</h6>
          </div>
        </div>
      </div>
    </div>
    <div>
      <div id="myModal" ref="myModal" class="modal">

    <!-- Modal content -->
    <div class="modal-content" v-for="(d,index) in details" :key="index">
      <button  @click="close()" class=" close btn text-right">x</button>
      
      <div class="row my-5 mx-1 d-flex">
        <div>
          <h3 class="h3"><strong>{{d.title}}</strong></h3>
          <p><strong>{{d.type}}</strong></p>
          <p class="font-weight-bold ">Rated: {{d.rating}}/10</p>
        </div>
        
        <button v-if=" !inlist" class="ml-auto mr-4 btn btn-secondary rounded-pill edit-list px-4 font-weight-bold h-100 mt-4 py-3" @click="addAnime(d.anime_id)"> Add to my list </button>
        <button v-else class="ml-auto mr-4 btn btn-secondary rounded-pill edit-list px-4 font-weight-bold mt-4 h-100 py-3" @click="removeAnime(d.anime_id)"> Remove from my list </button>
      </div>
      
      <p class="mb-5">{{d.synopsis}}</p>
      <p><strong>Producers:</strong> <span v-for="(p, index) in d.producer" :key="index">{{p}}, </span></p>
      <p><strong>Aired:</strong> {{d.aired}}</p>
      <p><strong>Studio:</strong> <span v-for="(s, index) in d.studio" :key="index">{{s}},</span></p>
      <p v-if="rated" class=""> <strong>You rated this {{rating}} / 10 </strong> </p> 
      <div v-else-if="!rated && inlist">
        <p > <strong>Rate this: </strong> </p> 


        <form class="row" v-on:submit.prevent="onSubmit">
          
          <input class="ml-4" name="rating" id="rating" type="number" min="1" max="10" step="1">
          <p class="ml-1">out of 10</p>
           <button class="ml-4 btn btn-secondary rounded-pill submitRating" >Submit Rating</button>
        </form>
      </div>
      
    </div>
  </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  import searchResultService from '../services/SearchResultService';
  import { bus } from '../main'
  export default {
    name: 'SearchResults',
    data() {
      return {
        mylist: [],
        searchlist: [],
        email: "",
        details: [],
        inlist: false,
        rated: false,
        rating: 10,
        name: '',
        id: 0,
        currentPage: 1,
        query: '',
      };
    },
    methods: {
      userName() {
        const path = `http://localhost:5000/userName?email=${this.email}`;
        axios.get(path)
          .then((response) => {
            this.name = response.data;
          });

      },
      getAnimes() {
        const path = `http://localhost:5000/mypicks?email=${this.email}`;
        axios.get(path)
          .then((response) => {
            this.mylist = response.data;
          });
      },

      animeModal(id) {
        this.rated = false
        const path1 = `http://localhost:5000/anime/${id}`;
        axios.get(path1)
          .then((response) => {
            this.details = response.data;
            this.id = id
          });
        this.inlist = false
        for (let i in this.mylist) {
          if (this.mylist[i].anime_id == id) {
            this.inlist = true
          }
        }
        const path2 = `http://localhost:5000/FindReview?anime_id=${id}&email=${this.email}`
        axios.get(path2)
          .then((response) => {
            this.rating = response.data
            console.log(this.rating)
            if (this.rating > 0) {
              this.rated = true
            }
          });

        this.$refs.myModal.style.display = 'block';
      },
      close() {
        this.$refs.myModal.style.display = 'none';
      },
      addAnime(id) {
        const path = `http://localhost:5000/addAnime?anime_id=${id}&email=${this.email}`
        axios.patch(path, {}, { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }).then((response) => {
          this.mylist = response.data;
          this.inlist = true;
        });

      },
      removeAnime(id) {
        const path = `http://localhost:5000/RemoveAnime?anime_id=${id}&email=${this.email}`
        axios.patch(path, {}).then((response) => {
          this.mylist = response.data;
          this.inlist = false;
        });
      },
      onSubmit() {
        let r = document.getElementById("rating").value;
        let i = this.id
        const path1 = `http://localhost:5000/ReviewAnime?rating=${r}&anime_id=${i}&email=${this.email}`

        axios.get(path1, {}).then((response) => {
          this.rating = response.data
          this.rated = true
        });

      },
      async getEmail() {
        return await this.$auth.user.email;
      },
    },
    created() {
      this.query = this.$route.query.search
      this.getEmail()
        .then(email => {
          this.email = email
          this.getAnimes()
        }
      );
      searchResultService.findAnime(this.query)
        .then(res => {
          this.searchlist = res
        }
      )
      
      bus.$on('search', (input) => {
        searchResultService.findAnime(input)
          .then(res => {
            this.query = input;
            this.searchlist = res
          }
        )
      })
    },
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  /* The Modal (background) */

  body {
    background-color: hsl(224, 19%, 44%);
  }
</style>

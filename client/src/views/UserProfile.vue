<template>
    <div class="user-info">
        <h2 class="h2"><strong>Email:</strong> {{user[0].email}}</h2>
        <h2 class="h2"><strong>Name:</strong> {{user[0].nickname}}</h2>
        <button class="btn btn-secondary rounded-pill font-weight-bold px-5" @click="$router.push('edit-profile')">Edit</button>
    </div>
</template>

<script>
//import axios from 'axios';
  import editProfileService from '../services/EditProfileService.js';
    export default {
        name: "userprofile",
        
        data() {
            return {
                user: []
                //name:'',
            }
        },
        created() {
          this.getUserData()
        },
        methods: {
            //userName(){
            //var e = this.$auth.user.name
            //const path = `http://localhost:5000/userName?email=${e}`;
            //axios.get(path)
            //    .then((response) => {
            //    this.name = response.data;
            //    });

            //},
          async getUserData() {
            const email = await this.$auth.user.email;
            editProfileService.getUserByEmail(email)
           .then(
               (user => {
                  this.$set(this, "user", user);
               }).bind(this)
           );
          }
        }
    }
</script>

<style lang="scss" scoped>
    .event-single {
        margin-top: 30px;
    }

    .hero {
        margin-bottom: 70px;
    }

    .event-images {
        margin-top: 50px;
    }

    .description {
        margin-bottom: 30px;
    }

    .user-info {
        text-align: center;
    }
</style>

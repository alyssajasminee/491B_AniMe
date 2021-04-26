<template>
    <div class="editForm">
        <form id="editFormInput" v-on:submit.prevent="EditName">
            <label class="h2 font-weight-bold" c="nameLabel" for="name">Name: </label>
            <input type="text" name="name" id="name" :value="name" />
            
            <br />
            <button class="ml-4 mt-5 btn btn-secondary px-5 rounded-pill font-weight-bold" >Submit Edit</button>

            <br /><br /><br />
            
        </form>
        <button class="ml-4 btn btn-secondary rounded-pill px-5 font-weight-bold" @click="deleteAccount">Delete Account</button>
    </div>
</template>

<script>
import axios from 'axios';
    
export default {
    name: "userprofile",
    
    data() {
        return {
            user: {},
            name:'',
        }
    },
    created() {
    
        this.userName();
        
    },
    methods: {
        userName(){
            var e = this.$auth.user.email
            const path = `http://localhost:5000/userName?email=${e}`;
            axios.get(path)
                .then((response) => {
                this.name = response.data;
                });

        },
        EditName(){
            var e = this.$auth.user.email
            var u = document.getElementById('name').value
            const path = `http://localhost:5000/EditUser?email=${e}&username=${u}`;
            axios.patch(path,{})
                .then((response) => {
                this.name = response.data;
                window.location.href = '/profile'
                });
            
        },
        deleteAccount(){
            var e = this.$auth.user.email
            const path = `http://localhost:5000/DeleteUser?email=${e}`;
            axios.delete(path,{})
                .then(() => {
                    this.$auth.logout({
                    returnTo: window.location.origin
                    });
                });
            
        },
        }
        
    
}
</script>

<style>
    .editForm {
        text-align: center
    }
</style>
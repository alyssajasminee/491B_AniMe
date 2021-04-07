<template>
  <div class="buttons">
    <button id="create-account" @click="login" v-if="!$auth.isAuthenticated"
    class="btn btn-secondary border-secondary mt-5 btn-outline-light rounded-pill mx-auto">
    <a>Create Account</a>
    </button>
    <button id="sign up" @click="login" v-if="!$auth.isAuthenticated"
    class="btn btn-secondary border-secondary my-5 btn-outline-light rounded-pill mx-auto">
    <a href="/signin">Sign In</a>
    </button>
    <h1 v-if="$auth.isAuthenticated">Welcome, {{$auth.user.name}}!</h1>
 </div>
</template>

<script>
export default {
    name: 'HomeView',
    methods: {
      login() {
        console.log(this.$auth);
          this.$auth.loginWithRedirect();
      } 
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
button{
  width :200px;
}
.buttons{
  display:flex;
  flex-direction: column;
}
a:hover{
color:black
}
a{
color:white
}
</style>

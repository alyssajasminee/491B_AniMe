<template>
  <div class="buttons">
    
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

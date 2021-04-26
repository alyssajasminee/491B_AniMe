<template>
  <div>
    
    <h1 class="h2">Welcome, {{$auth.user.name}}!</h1>
 </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'HomeView',
    mounted() {
      this.$nextTick(() => {
        this.User();
      });
    },
    methods: {
      User(){
        var e = this.$auth.user.email
        const path = `http://localhost:5000/AddUser?email=${e}`
        axios.get(path,{})
      

      },
    },
    created(){
      this.User()
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

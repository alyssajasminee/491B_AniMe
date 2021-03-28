<template>
<div  id="pic-back">
<div id="signin-form">
  <label for="uname" class="text-uppercase font-weight-bold h4">username:</label>
  <input type="text" id="uname" name="uname"><br><br>
  <label for="uname" class="text-uppercase font-weight-bold h4">password:</label>
  <input type="text" id="password" name="password"><br><br>
  <button id="sign up"
    class="btn btn-secondary border-secondary my-5 btn-outline-light rounded-pill mx-auto">
    <a href="/user/lists">Sign In</a>
  </button>
</div>
</div>
</template>
<script>
export default {
  name: 'SignIn',

};
</script>
<style scoped>
button{
  width :200px;
}
#signin-form{
  margin-top: 20%
}
#pic-back::before{
  top:0;
  right: 0;
  left: 0;
  bottom:0;
  content: '';
  background-image:url('~@/assets/anime_home_background.jpg');
  height: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  opacity: 0.3;
  position: absolute;
  z-index: -1;
  width:100%;
}
</style>

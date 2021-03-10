<template>
  <div class="buttons">
    <button id="create-asccount"
    class="btn btn-secondary border-secondary mt-5 btn-outline-light rounded-pill mx-auto">
    <a>Create Account</a>
    </button>
    <button id="sign up"
    class="btn btn-secondary border-secondary my-5 btn-outline-light rounded-pill mx-auto">
    <a>Sign up</a>
    </button>
 </div>
</template>

<script>
export default {
  name: 'HomeView',
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
</style>

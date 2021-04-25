<template>
  <nav class="navbar container" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
    <div id="navbar" class="navbar-menu">
      <div class="navbar-start">
        <router-link v-if="$auth.isAuthenticated" to="/user/lists" class="navbar-item">My List</router-link>
        <router-link v-if="$auth.isAuthenticated" to="/genres" class="navbar-item">Genres</router-link>
        <router-link v-if="$auth.isAuthenticated" class="navbar-item" to="/profile">Profile</router-link>
      </div>
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <!-- Check that the SDK client is not currently loading before accessing is methods -->
            <div v-if="!$auth.loading">
              <!-- show login when not authenticated -->
              <a v-if="!$auth.isAuthenticated" @click="login" class="button is-dark"><strong>Sign in</strong></a>
              <!-- show logout when authenticated -->
              <a v-if="$auth.isAuthenticated" @click="logout" class="button is-dark"><strong>Log out</strong></a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>
<script>
    export default {
        name: 'Nav',
        methods: {
            // Log the user in
            login() {
                this.$auth.loginWithRedirect();
            },
            // Log the user out
            logout() {
                this.$auth.logout({
                    returnTo: window.location.origin
                });
            }
        }
    }
</script>
<style lang="scss" scoped>
  nav {
    margin-top: 25px;
    margin-bottom: 30px;
    background: inherit;
    a

  {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active

  {
    color: #d88d00;
  }

  }
  }
</style>

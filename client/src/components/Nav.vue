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
        <router-link to="/" class="navbar-item h2">Home</router-link>
        <router-link v-if="$auth.isAuthenticated" to="/user/lists" class="navbar-item h2">My List</router-link>
        <router-link v-if="$auth.isAuthenticated" to="/genres" class="navbar-item h2">Genres</router-link>
        <router-link v-if="$auth.isAuthenticated" class="navbar-item h2" to="/profile">Profile</router-link>
      </div>
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="search-container">
            <input type="text" placeholder="Search..." name="search" id="search">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            <button v-on:click="search()"><i class="fa fa-search"></i></button>
          </div>
          <div class="buttons">
            <!-- Check that the SDK client is not currently loading before accessing is methods -->
            <div v-if="!$auth.loading">
              <!-- show login when not authenticated -->
              <a v-if="!$auth.isAuthenticated" @click="login" class="button is-dark rounded-pill px-5 h2 h-auto "><strong class="h3 mb-1 font-weight-bold">Sign In</strong></a>
              <!-- show logout when authenticated -->
              <a v-if="$auth.isAuthenticated" @click="logout" class="button is-dark rounded-pill px-5 h2 h-auto "><strong class="h3 mb-1 font-weight-bold">Log Out</strong></a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <hr v-if="$auth.isAuthenticated" class="nav-bottom">
  </nav>
</template>
<script>
    import { bus } from '../main'
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
            },
            search() {
              const input = document.getElementById('search').value
              if (this.$route.name != 'searchResults') {
                this.$router.push(`/search-results?search=${input}`)
                this.$router.go(1)
              } else {
                bus.$emit('search', input)
              }
            }
        }
    }
</script>
<style lang="scss" scoped>
  * {box-sizing: border-box;}

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
  hr.nav-bottom{
  border-bottom: 5px solid black;
  width: 100%;
  margin: 0;
  }
  .navbar{
    flex-wrap:wrap;
  }

  .navbar-item {

      input[type=text] {
      padding: 6px;
      margin-top: 8px;
      font-size: 17px;
      border: none;
      }

  .search-container button {
    float: right;
    padding: 6px 10px;
    margin-top: 8px;
    margin-right: 16px;
    background: #ddd;
    font-size: 17px;
    border: none;
    cursor: pointer;
  }
      .search-container button:hover {
      background: #ccc;
    }
  }
</style>

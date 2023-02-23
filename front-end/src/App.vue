<template>
  <nav>
    <!-- <router-link :to="{ name:'Jobs'}">Jobs</router-link>
    <router-link :to="{name:'PostData'}">PostData</router-link> -->
    <router-link :to="{name:'Get'}">GetData</router-link>
  </nav>
  <router-view/>
  
</template>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    background: gray;
  }

  nav {
    padding: 30px;
  }

  nav a{
    font-weight: bold;
    color: blue;
    text-decoration: none;
    padding:10px;
    border-radius: 4px;
  }

  nav a.router-link-exact-active {
    color: #42b983;
  }
</style>


</script>

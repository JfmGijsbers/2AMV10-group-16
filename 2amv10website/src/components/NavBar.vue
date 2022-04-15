<template>
<div class="nav">
    <div>
        <v-row>
            <v-col cols="4" class="links">
                <h1>2AMV10 Group 16</h1>
            </v-col>
            <v-col cols="7" class="text-end" align-self="end">
                <div class="mt-3">
                    <router-link :to="{name: 'home'}" class="link" :class="{ active: $route.name==='home' }">Profiler</router-link>
                    <router-link :to="{name: 'analyst'}" class="ml-3 link" :class="{active: $route.name==='analyst'}">Data Analyst</router-link>
                </div>
            </v-col>
            <v-col cols="1"></v-col>
        </v-row>
    </div>
</div>
</template>

<script>
// :class="{active: $route.name==='analyst'}"
  export default {
      name: 'navigation-bar',
      data() {
          return {
          }
      }
  }
</script>

<style scoped>
.nav {
    width: 100%;
    background-color: white;
    height:60px;
    padding: 5px;
}
.links {
    height: 60px;
}
.link {
    cursor: pointer;
    text-decoration: none;
    color: grey;
}
.link:hover {
    color: black;
}
.active {
    color: black;
}
</style>
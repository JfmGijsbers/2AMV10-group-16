<template>
  <v-app style="background-color: #ede9f0">
    <NavBar/>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import NavBar from './components/NavBar.vue';

export default {
  name: 'App',

  components: {
    NavBar
  },

  data: () => ({
    //
  }),
}
</script>

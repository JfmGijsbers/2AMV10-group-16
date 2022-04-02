<template>
  <v-app>
      <NavBar/>
    <v-main>
      <v-container>
        <v-row>
            <v-col v-for="card in cards" :key="card.title" class="mt-4" cols="3">
                <card :icon="card.icon" :title="card.title" :value="card.value"/>
            </v-col>
        </v-row>
        <v-row class="mt-3"> 
            <v-col cols="9">
                <Scatter class="mt-4"/>
            </v-col>
            <v-col>
                <Table/>
            </v-col>
        </v-row>

      </v-container>
      </v-main>
  </v-app>
</template>

<script>
import Card from './components/Card.vue';
import Scatter from './components/Scatter.vue';
import Table from './components/Table.vue';
import NavBar from './components/NavBar.vue';

export default {
  name: 'App',
  components: {
      Card,
      Scatter,
      Table,
      NavBar
  },
  data() {
      return {
          cards: [
              {
                  icon: "mdi-alarm",
                  title: "Training time",
                  value: "152.3s",
              },
              {
                  icon: "mdi-integrated-circuit-chip",
                  title: "False positives",
                  value: "152 / 5000",
              },
              {
                  icon: "mdi-scoreboard",
                  title: "Validation score",
                  value: "89.8%",
              },
              {
                  icon: "mdi-scoreboard",
                  title: "Test accuracy",
                  value: "99.8%",
              },
          ],
          appTitle: 'Awesome App',
            sidebar: false,
            menuItems: [
                { title: 'Home',  icon: 'home' },
                { title: 'Sign Up',  icon: 'face' },
                { title: 'Sign In', icon: 'lock_open' }
            ]
      }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #ede9f0;
}
html {
    background-color: #ede9f0;
}
</style>

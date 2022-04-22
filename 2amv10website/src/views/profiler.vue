<template>
    <v-container>
        <v-row class="mt-3"> 
            <v-col cols="12">
                <Scatter class="mt-4"/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="6"><Network/></v-col>
            <v-col cols="6"><Chord/></v-col>
        </v-row>
        <v-row>
                <!-- <Chord/> -->
        </v-row>

    </v-container>
</template>

<script>
import Scatter from '../components/Scatter.vue';
import Chord from '../components/Chord.vue';
import Network from '../components/NetworkGraph.vue';

export default {
  name: 'App',
  components: {
      Scatter,
      Chord,
      Network,
  },
  data() {
      return {
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

<template>
    <v-container>
        <v-row>
            <v-col v-for="card in cards" :key="card.title" class="cards pl-2 pr-2" cols="3">
                <card :icon="card.icon" :title="card.title" :value="card.value"/>
            </v-col>
        </v-row>
        <v-row class="mt-4">
            <v-col cols="6">
                <Heatmap/>
            </v-col>
            <v-col cols="6">
                <img :src="imgSrc" alt="">
                <img :src="imgSrc" alt="">
            </v-col>
        </v-row>
        <!-- <v-row>
            <v-col cols="6">
            </v-col>
            <v-col cols="6">
                <img :src="imgSrc" alt="">
            </v-col>
        </v-row> -->
    </v-container>
</template>

<script>
import Card from '../components/Card.vue';
import Heatmap from '../components/Heatmap.vue';

export default {
  name: 'App',
  components: {
      Card,
      Heatmap,
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
          imgSrc: require('@/assets/preds.jpeg')
      }
  }
}
</script>

<style>
.cards {
    padding: 50px 0 50px 0;
}
</style>

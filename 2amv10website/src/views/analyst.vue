<template>
    <v-container>
        <v-row class="mt-4">
            <v-col cols="6">
                <Heatmap/>
            </v-col>
            <v-col cols="6">
                <img :src="imgSrc" alt="">
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <h4>Filter activations</h4>
            </v-col>
            <v-col cols="3">
                <img class="activation-image" :src="require('@/assets/activation1.jpeg')" alt="">
            </v-col>
            <v-col cols="3">
                <img class="activation-image" :src="require('@/assets/activation2.jpeg')" alt="">
            </v-col>
            <v-col cols="3">
                <img class="activation-image" :src="require('@/assets/activation3.jpeg')" alt="">
            </v-col>
            <v-col cols="3">
                <img class="activation-image" :src="require('@/assets/activation4.jpeg')" alt="">
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import Heatmap from '../components/Heatmap.vue';

export default {
  name: 'App',
  components: {
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
.activation-image {
    width: 100%;
}
</style>

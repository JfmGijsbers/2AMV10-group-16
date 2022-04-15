import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
// import * as VueRouter from 'vue-router';
import { createRouter, createWebHistory } from 'vue-router'
import VueApexCharts from "vue3-apexcharts";
import VNetworkGraph from "v-network-graph"
import "v-network-graph/lib/style.css"

import Analyst from './views/analyst.vue';
import Profiler from './views/profiler.vue';

loadFonts()

const routes = [
    {
        path: '/',
        name: 'home',
        component: Profiler,
    },
    {
        path: '/analyst',
        name: 'analyst',
        component: Analyst,
    }
]


const router = createRouter({
    // mode: 'history',
    history: createWebHistory(),
    props: true,
    routes: routes
})

createApp(App)
    .use(router)
    .use(vuetify)
    .use(VueApexCharts)
    .use(VNetworkGraph)
    .mount('#app');
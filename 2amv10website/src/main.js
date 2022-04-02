// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
Vue.config.productionTip = false;
import vuetify from '@/plugins/vuetify' // path to vuetify export

import VueApexCharts from 'vue-apexcharts'
Vue.use(VueApexCharts)

Vue.component('apexchart', VueApexCharts)
/* eslint-disable no-new */
new Vue({
    vuetify,
  el: '#app',
  components: { App },
  template: '<App/>'
})

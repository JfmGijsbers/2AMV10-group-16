<template>
<div class="example">
  <apexchart width="500" height="500" type="heatmap" :options="chartOptions" :series="series"></apexchart>
</div>
</template>

<script>
import heatmapData from '../json/cm.json';
export default {
  name: 'HeatmapExample',
  created() {
      this.convertData();
  },
  data: function() {
    return {
      data: heatmapData,
      chartOptions: {
        colors: ["#008FFB"],
        xaxis: {
          type: 'category',
          categories: [],
          title: {
              text: 'Predicted'
          },
          labels: {
              rotate: -70
          }
        },
        yaxis: {
            title: {
                text: 'Actual'
            }
        },
        title: {
          text: 'Prediction heatmap'
        },
        dataLabels: {
            enabled: true,
            style: {
                colors: ['#fff']
            }
        },
      },
      series: [],
      keys: []
    }
  },
  methods: {
    convertData() {
        let data = JSON.parse(JSON.stringify(this.data));
        let series = [];
        let keys = Object.keys(data);
        for (const item of Object.entries(data)) {            
            let cat_series = [];
            for (let i = 0; i < keys.length; i++) {
                cat_series.push({
                    x: keys[i],
                    y: item[1][i]
                })
            }
            series.unshift({
                name: item[0],
                data: cat_series
            });
        }
        this.series = series
    }
  }
}
</script>
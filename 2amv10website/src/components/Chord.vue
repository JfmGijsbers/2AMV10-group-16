<template>

	<div>
        <div id="chartdiv" class="chartdiv"></div>
    </div>

</template>

<script>
import * as am5 from "@amcharts/amcharts5";
import * as am5flow from "@amcharts/amcharts5/flow";
import am5themes_Animated from '@amcharts/amcharts5/themes/Animated';
export default {
    name: 'vue-chord-xx',
    data() {
        return {
        }
    },
    mounted() {
        
// Create root and chart
var root = am5.Root.new("chartdiv"); 

// Set themes
root.setThemes([
  am5themes_Animated.new(root)
]);

// Create series
var series = root.container.children.push(
  am5flow.Chord.new(root, {
    sourceIdField: "from",
    targetIdField: "to",
    valueField: "value"
  })
);

series.nodes.get("colors").set("step", 2);

// Set data
series.data.setAll([
  { from: "A", to: "B", value: 10 },
  { from: "B", to: "C", value: 8 },
  { from: "C", to: "D", value: 4 },
  { from: "C", to: "E", value: 3 },
  { from: "D", to: "G", value: 5 },
  { from: "D", to: "I", value: 2 },
  { from: "D", to: "H", value: 3 },
  { from: "E", to: "H", value: 6 },
  { from: "G", to: "J", value: 5 },
  { from: "I", to: "J", value: 1 },
  { from: "H", to: "J", value: 9 }
]);
    }
}

</script>

<style scoped>
#chartdiv {
  width: 100%;
  height: 550px;
}
</style>

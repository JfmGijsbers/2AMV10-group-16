<template>
	<div>
        <div id="chartdiv" class="chartdiv"></div>
    </div>
</template>

<script>
import * as am5 from "@amcharts/amcharts5";
import * as am5flow from "@amcharts/amcharts5/flow";
import am5themes_Animated from '@amcharts/amcharts5/themes/Animated';
import chord_nodes from "../json/chord_nodes.json";
export default {
    name: 'vue-chord-xx',
    data() {
        return {
            nodes: chord_nodes
        }
    },
    mounted() {
        this.convertData()
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
        series.data.setAll(this.convertData())
    },
    methods: {
        convertData() {
            let arr = JSON.parse(JSON.stringify(this.nodes))
            let data = []
            for (const item of Object.entries(arr)) {
                data.push(item[1])
            }
            return data;
        }
    }
}

</script>

<style scoped>
#chartdiv {
  width: 100%;
  height: 550px;
}
</style>

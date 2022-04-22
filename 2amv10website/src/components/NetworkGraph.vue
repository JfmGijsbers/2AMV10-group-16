<template>
  <v-network-graph
    class="network"
    :zoom-level="0.5"
    :nodes="nodes"
    :edges="edges"
    :configs="configs"
  >
    <template #edge-label="{ edge, ...slotProps }">
      <v-edge-label :text="edge.label" align="center" vertical-align="above" v-bind="slotProps" />
    </template>
    <template
      #override-node-label="{
        nodeId, scale
      }"
    >
      <text
        x="0"
        y="0"
        :font-size="9 * scale"
        text-anchor="middle"
        dominant-baseline="central"
        fill="#ffffff"
        >{{ nodeId }}</text
      >
    </template>
    <!-- Tooltip -->
    <!-- <div
      ref="tooltip"
      class="tooltip"
      :style="{ ...tooltipPos, opacity: tooltipOpacity }"
    >
      <div>
        {{ `${data.edges[targetEdgeId]?.name ?? ""}` }}
      </div>
    </div> -->
  </v-network-graph>
</template>

<script>
import edges from '../json/edges.json';
import nodes from '../json/nodes.json';
import { reactive, ref } from "vue";
import * as vNG from "v-network-graph";
import {
  ForceLayout,
} from "v-network-graph/lib/force-layout";

export default {
    name: 'navigation-bar',
    data() {
        return {
            nodeCount: ref(20),
            nodes: nodes,
            edges: edges,
            configs: reactive(
                vNG.defineConfigs({
                    view: {
                        layoutHandler: new ForceLayout({
                            positionFixedByDrag: false,
                            positionFixedByClickWithAltKey: true,
                        }),
                        scalingObjects: true,
                        minZoomLevel: 0.1,
                        maxZoomLevel: 64
                    },
                    node: {
                        label: {
                            visible: true,
                        },
                        normal: {
                            radius: node => node.size,
                            color: node => node.color
                        }
                    },
                    edge: {
                        label: {
                            fontSize: 7,
                        },
                        normal: {
                            width: edge => edge.width, // Use the value of each edge object
                        }
                    }
                })
                )
        }
    },
    methods: {
        watchEffect() {
            this.buildNetwork(20, this.nodes, this.edges)
        },
        buildNetwork(count, nodes, edges) {
            const idNums = [...Array(count)].map((_, i) => i)

            // nodes
            const newNodes = Object.fromEntries(idNums.map(id => [`person${id}`, {}]))
            Object.keys(nodes).forEach(id => delete nodes[id])
            Object.assign(nodes, newNodes)

            // edges
            const makeEdgeEntry = (id1, id2) => {
                return [`edge${id1}-${id2}`, { source: `person${id1}`, target: `person${id2}` }]
            }
            const newEdges = Object.fromEntries([
                ...idNums
                .map(n => [n, (Math.floor(n / 5) * 5) % count])
                .map(([n, m]) => (n === m ? [n, (n + 5) % count] : [n, m]))
                .map(([n, m]) => makeEdgeEntry(n, m)),
            ])
            Object.keys(edges).forEach(id => delete edges[id])
            Object.assign(edges, newEdges)
        },
        // getNodes(n) {
        //     let nodes = [];
        //     for (let i = 0; i < n; i++) {
        //         const name = 'node' + i;
        //         //nodes[name] = 'Person ' + i;
        //         nodes.push({
        //             key: name,
        //             value: {
        //                 name: 'Person ' + i
        //             }
        //         })
        //     }
        //     this.nodes = nodes;
        //     //console.log(this.nodes)
        // }

    },
    computed: {
        filteredEdges() {
            let filteredEdges = JSON.parse(this.edges).filter((edge) => {
                return parseInt(edge.label) > 8
            })
            console.log(filteredEdges)
            return filteredEdges;
        }
  }
}

</script>
<style>
.network {
    border: 3px grey;
    border-style: solid;
    width: 250px;
    height: 250px;
}

.tooltip-wrapper {
  position: relative;
}
.tooltip {
  top: 0;
  left: 0;
  opacity: 0;
  position: absolute;
  padding: 10px;
  text-align: center;
  font-size: 12px;
  background-color: #fff0bd;
  border: 1px solid #ffb950;
  box-shadow: 2px 2px 2px #aaa;
  transition: opacity 0.2s linear;
}

</style>


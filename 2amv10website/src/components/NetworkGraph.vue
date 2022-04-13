<template>
  <v-network-graph
    class="network"
    :zoom-level="0.5"
    :nodes="nodes"
    :edges="edges"
    :configs="configs"
  />
</template>

<script>
import { reactive, ref } from "vue"
import * as vNG from "v-network-graph"
import {
  ForceLayout,
} from "v-network-graph/lib/force-layout"

export default {
    name: 'navigation-bar',
    data() {
        return {
            nodeCount: ref(20),
            nodes: {
                node1: { name: "Node 1" },
                node2: { name: "Node 2" },
                node3: { name: "Node 3" },
                node4: { name: "Node 4" },
                node5: { name: "Node 5" },
                node6: { name: "Node 6" },
                node7: { name: "Node 7" },
                node8: { name: "Node 8" },
            },
            edges: {
                edge1: { source: "node1", target: "node2" },
                edge2: { source: "node2", target: "node3" },
                edge3: { source: "node3", target: "node4" },
                edge4: { source: "node8", target: "node7" },
                edge5: { source: "node4", target: "node8" },
                edge6: { source: "node3", target: "node8" }
            },
            configs: reactive(
                vNG.defineConfigs({
                    view: {
                        layoutHandler: new ForceLayout({
                            positionFixedByDrag: false,
                            positionFixedByClickWithAltKey: true,
                        }),
                        minZoomLevel: 0.1,
                        maxZoomLevel: 10
                    },
                    node: {
                        label: {
                            visible: true,
                        },
                    },
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
            const newNodes = Object.fromEntries(idNums.map(id => [`node${id}`, {}]))
            Object.keys(nodes).forEach(id => delete nodes[id])
            Object.assign(nodes, newNodes)

            // edges
            const makeEdgeEntry = (id1, id2) => {
                return [`edge${id1}-${id2}`, { source: `node${id1}`, target: `node${id2}` }]
            }
            const newEdges = Object.fromEntries([
                ...idNums
                .map(n => [n, (Math.floor(n / 5) * 5) % count])
                .map(([n, m]) => (n === m ? [n, (n + 5) % count] : [n, m]))
                .map(([n, m]) => makeEdgeEntry(n, m)),
            ])
            Object.keys(edges).forEach(id => delete edges[id])
            Object.assign(edges, newEdges)
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
</style>


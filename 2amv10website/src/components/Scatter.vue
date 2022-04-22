<template>
    <div id="chart" class="scatter">
        <apexchart type="scatter" height="700" :options="chartOptions" :series="preds"></apexchart>
    </div>
</template>

<script>
import preds from '../json/predsxttuples_translated_transposed.json';
export default {
    name: 'vue-scatter',
    data() {
        return {
            preds: [{
                name: "Predictions",
                data: preds
            }],
            label: 0,
            chartOptions: {
                chart: {
                height: 1000,
                type: 'scatter',
                zoom: {
                    enabled: false,
                    type: 'xy'
                }
                },
                title: {
                text: 'Item ownership scatter'
                },
                yaxis: {
                    tickAmount: 40,
                    labels: {
                        formatter: function(val) {
                            return 'Person' + Math.round(val)
                        }
                    },
                },
                xaxis: {
                    tickAmount: 43,
                    labels: {
                        rotate: -45,
                        style: {
                            fontSize: '10px'
                        },
                        formatter: function(val) {
                            const items = {
                                20: 'miniCards',
                                30: 'redDart',
                                24: 'pinkCandle',
                                14: 'gyroscope',
                                8: 'cupcakePaper',
                                9: 'eyeball',
                                35: 'spiderRing',
                                19: 'metalKey',
                                40: 'voiceRecorder',
                                33: 'sign',
                                17: 'lavenderDie',
                                16: 'hairRoller',
                                21: 'noisemaker',
                                42: 'yellowBalloon',
                                1: 'blueSunglasses',
                                31: 'redWhistle',
                                3: 'cactusPaper',
                                2: 'brownDie',
                                38: 'turtle',
                                36: 'stickerBox',
                                4: 'canadaPencil',
                                39: 'vancouverCards',
                                26: 'plaidPencil',
                                32: 'rubiksCube',
                                29: 'redBow',
                                12: 'giftBag',
                                34: 'silverStraw',
                                6: 'cloudSign',
                                25: 'pinkEraser',
                                15: 'hairClip',
                                28: 'rainbowPens',
                                27: 'pumpkinNotes',
                                41: 'yellowBag',
                                23: 'partyFavor',
                                22: 'paperPlate',
                                37: 'trophy',
                                11: 'gClamp',
                                5: 'carabiner',
                                0: 'birdCall',
                                7: 'cowbell',
                                10: 'foamDart',
                                13: 'glassBead',
                                18: 'legoBracelet'
                            }
                            return items[Math.round(val)]
                        },
                    },
                }
            },
        }
    },
}
</script>

<style>
</style>
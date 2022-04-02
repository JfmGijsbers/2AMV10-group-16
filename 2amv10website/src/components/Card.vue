<template>
    <div class="card">
        <v-row class="">
            <p class="card-title text-left mt-2">{{ title }}</p>
        </v-row>
        <v-row class="mt-0 ml-2 mr-2">
            <v-col cols="3" class="text-right">
                <v-icon large color="black" class="icon">{{ icon }}</v-icon>
            </v-col>
            <v-col cols="9" class="text-left">
                <p>{{ value }}</p>
            </v-col>
        </v-row>
    </div>
</template>

<script>
export default {
    props: {
        icon: String,
        title: String,
        value: String,
    },
    data() {
        return {
        }
    }
}
</script>

<style>
.card {
    background-color: white;
    border-radius: 10px;
}
.card-title {
    font-size: 12px;
    color: #4f4e4d;
    width: 100%;
    padding: 0 40px 0 40px;
    font-weight: bold;
    justify-content: center;
}
.icon {
    width: 100%;
    height: 25px;
}
</style>
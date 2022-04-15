<template>
    <div class="card options">
        <div class="content">
            <h4>Model</h4>
            <v-checkbox
                v-model="datagenerator"
                label="Use Datagenerator"
                hide-details
            ></v-checkbox>
            <v-divider class="mt-2"></v-divider>
            <v-autocomplete
                auto-select-first
                chips
                clearable
                v-model="value"
                :items="activationItems"
                label="Optimizer"
            ></v-autocomplete>
            <v-btn color="primary">Retrain</v-btn>

        </div>
    </div>
</template>

<script>
export default {
    name: 'vue-options',
    data() {
        return {
            value: "Adam",
            datagenerator: true,
            activationItems: [
                "Adam",
                "RMSProp"
            ]
        }
    }
}
</script>

<style>
.card {
    background-color: white;
    border-radius: 10px;
}
.content {
    margin: 20px;
    height: 100%;
}
.options {
    height: 100%;
}
.temp {
    height: 80%;
}
</style>
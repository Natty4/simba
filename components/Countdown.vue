<template>
    <div class="d-flex">

        <h1>On Development State !</h1>
        <v-card-text class="block">
            <p class="digit">{{ days }}</p>
            <h1 class="text">Days</h1>
        </v-card-text>
        <v-card-text class="block">
            <p class="digit">{{ hours }}</p>
            <h1 class="text">Hours</h1>
        </v-card-text>
        <v-card-text class="block">
            <p class="digit">{{ minutes }}</p>
            <h1 class="text">Minutes</h1>
        </v-card-text>
        <v-card-text class="block">
            <p class="digit">{{ seconds }}</p>
            <h1 class="text">Seconds</h1>
        </v-card-text>

    </div>
        
    
</template>
<script>
export default {
    ready() {
        window.setInterval(() => {
            this.now = Math.trunc((new Date()).getTime() / 1000);
        },1000);
    },
    props : {
        date : {
            type: String,
            coerce: str => Math.trunc(Date.parse(str) / 1000)
        }
    },
    data() {
        return {
            now: Math.trunc((new Date()).getTime() / 1000)
        }
    },
    computed: {
        seconds() {
            return (this.date - this.now) % 60;
        },
        minutes() {
            return Math.trunc((this.date - this.now) / 60) % 60;
        },
        hours() {
            return Math.trunc((this.date - this.now) / 60 / 60) % 24;
        },
        days() {
            return Math.trunc((this.date - this.now) / 60 / 60 / 24);
        }
    }
}
</script>


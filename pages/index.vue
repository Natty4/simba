<template>
  <div>
    <v-carousel
          cycle
          height="89vh"
          hide-delimiter-background
          show-arrows-on-hover
        >
          <v-carousel-item
            v-for="(item,i) in items"
              :key="i"
              :src="item.src"
          >
          
              <v-row
                class="fill-height"
                align="center"
                justify="center"
              >
                  <v-card
                      class="mx-auto"
                      max-width="80%"
                      color="transparent"
                      align="center"
                      justify="center"
                    >
                      

                  
                    <p class="text-h3" v-if="item.page==3">
                      {{ item.txt}}
                    </p>
                    <p class="text-h1 text-bold" v-if="item.page==3"> {{ dayCount }}d : {{ timeCount }}h : {{ minuteCount }}m : {{ secondCount }}s  </p>
                    
                    <v-card
                        class="mx-auto"
                        max-width="70%"
                        v-if="item.page==2"
                        color="white"
                        border="none"
                      >
                        <v-card-text  v-if="item.page==2">
                          <div class="text-h4 error--text">SIMBA</div>
                          <br>
                          <p class="text-h3 blue--text">
                            {{ item.txt }}
                          </p>
                          
                        </v-card-text>
                    </v-card>
                    
                    
                    <v-btn v-if="item.page==4"
                      
                      color="error "
                      @click="snackbar = true"
                    >
                      notify me
                    </v-btn>
                  
                    <v-btn v-else-if="item.page==3"
                      
                      color="error "
                      @click="snackbar = true"
                    >
                      notify me
                    </v-btn>

                    <v-snackbar
                      v-model="snackbar"
                      :timeout="timeout"
                      color="cyan"
                    >
                      {{ text }}

                      <template v-slot:action="{ attrs }">
                        <v-btn
                          color="error"
                          text
                          v-bind="attrs"
                          @click="snackbar = false"
                        >
                          Close
                        </v-btn>
                      </template>
                    </v-snackbar>
              
                </v-card>
              </v-row>

          </v-carousel-item>
        </v-carousel>  
  </div>
</template>

<script>
  import Countdown from '../components/Countdown.vue';

  export default {
      components: { Countdown },
    data() {
      return{
        title: 'SimbaKids',
        logo: {
          src: require('../static/simbakidslogo.png'),
          alt: 'Logo Not Found'

        },
        items: [
          {
            page: '1',
            src: require('../assets/img/simbakids-1.png'),
            title: 'Simba Kids',
            txt: '',
            countdown: '',
            button: '',
            
          },
          {
            page: '2',
            src: require('../assets/img/simbakids-2.png'),
            txt: 'FUN CLOTHING DESIGNED FOR YOUR LITTLES AND THEIR ADVENTURES',
            countdown: '',
            button: '',
          },
          {
            page: '3',
            src: require('../assets/img/blacklion|Natan304.png'),
            title: 'SimbaKids',
            txt: 'coming soon',
            countdown: 'True',
            button: 'True',
          },
          {
            page: '4',
            src: require('../assets/img/simbakids-4.png'),
            title: '',
            txt: '',
            countdown: '',
            button: 'True',
          },
          {
            page: '5',
            src: require('../assets/img/simbakids-5.png'),
            title: '',
            txt: '',
            countdown: '',
            button: '',
          },
        ],
          dayCount: 93,
          timeCount: 24,
          minuteCount: 60,
          secondCount: 60,
          picker: null,
          snackbar: false,
          text: 'Successfully added to the list.',
          timeout: 6000,
          dialog: false,
          
      }
      
    },
    watch: {

        dayCount: {
            handler(value) {

                if (value > 0) {
                    setTimeout(() => {
                        this.dayCount--;
                    }, 86400000);
                }

            },
            immediate: true 
        },
        timeCount: {
            handler(value) {

                if (value > 0) {
                    setTimeout(() => {
                        this.timeCount--;
                    }, 3600000);
                }

                else{
                  this.secondCount = 24
                }

            },
            immediate: true 
        },
        minuteCount: {
            handler(value) {

                if (value > 0) {
                    setTimeout(() => {
                        this.minuteCount--;
                    }, 60000);
                }

                else{
                  this.secondCount = 60
                }

            },
            immediate: true 
        },
        secondCount: {
            handler(value) {

                if (value > 0) {
                    setTimeout(() => {
                        this.secondCount--;
                    }, 1000);
                }
                else{
                  this.secondCount = 60
                }

            },
            immediate: true 
        },

    }
  }
</script>

<style scoped>
  .text-h3{
    font-weight: bold;
  }
</style>
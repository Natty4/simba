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
                        color="transparent"
                        border="none"
                      >
                        <v-card-text  v-if="item.page==2">
                          <div class="text-h4 deep-orange--text">SIMBA</div>
                          <br>
                          <p class="text-h3 grey--text">
                            {{ item.txt }}
                          </p>
                          
                        </v-card-text>
                    </v-card>
                    
                    
                    <v-btn v-if="item.page==4"
                      
                      color="deep-orange "
                      @click="snackbar = true"
                    >
                      notify me
                    </v-btn>
                  
                    <v-btn v-else-if="item.page==3"
                      
                      color="deep-orange "
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
                          color="deep-orange"
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

    },
     head() {
      return {
        title: 'SimbaKids',
        meta: [
          {
          hid: 'twitter:card',
          name: 'twitter:card',
          content: 'summary_large_image',
          },
          {
            hid: 'twitter:site',
            name: 'twitter:site',
            content: '@SimbaKids',
          },
          {
            hid: 'twitter:creator',
            name: 'twitter:creator',
            content: '@kiflu_natnael',
          },
          {
            hid: 'twitter:title',
            name: 'twitter:title',
            content: 'Simba Kids',
          },
          {
            hid: 'twitter:description',
            name: 'twitter:description',
            content:'SIMBA has grown into an online clothing and kids brand that feels more like a family than a business. operating @Addis Abeba, SIMBA is all about fostering a happy and healthy work-life balance.',
          },
          {
            hid: 'twitter:image',
            property: 'twitter:image',
            content: require('../static/simbakidslogo.png'),
          },
          {
            hid: 'og:image',
            property: 'og:image',
            content: require('../static/simbakidslogo.png'),
          },
          {
            hid: 'og:site_name',
            name: 'og:site_name',
            content: 'Simba Kids',
          },
          {
            hid: 'og:type',
            name: 'og:type',
            content: 'website',
          },
          {
            hid: 'og:url',
            name: 'og:url',
            content: 'https://simbakids.netlify.app/',
          },
          {
            hid: 'og:title',
            name: 'og:title',
            content: 'Simba Kids',
          },
          {
            hid: 'og:description',
            name: 'og:description',
            content: 'SIMBA has grown into an online clothing and kids brand that feels more like a family than a business. operating @Addis Abeba, SIMBA is all about fostering a happy and healthy work-life balance.',
          }, 
        ],
      }
    }
  }
</script>

<style scoped>
  .text-h3{
    font-weight: bold;
  }
</style>

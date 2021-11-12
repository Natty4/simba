<template>
  <v-app>
    <v-app-bar
      :clipped-left="clipped"
      fixed
      app
      color="light-blue accent-4"

    >
      <v-avatar>
          <img
            :src="logo.src"
            :alt="logo.alt"
            @click="dialog = false"
          >
      </v-avatar>  <v-toolbar-title v-text="title"/>
      <v-spacer />

      <v-btn
        icon
        @click.stop="rightDrawer = !rightDrawer"
      >
        <v-icon>mdi-menu</v-icon>
      </v-btn>
    </v-app-bar>
    <v-main >
        <Nuxt />    
    </v-main>
      
    <v-navigation-drawer
      v-model="rightDrawer"
      :right="right"
      temporary
      fixed
      color="deep-orange "
    >
      <v-list>
        <v-list-item @click.native="right = !right">
          <v-list-item-action>
            <v-btn
              icon
              color="green"
            >
              <v-icon>mdi-cached</v-icon>
            </v-btn>
          </v-list-item-action>
          <v-list-item-title> 
              

            <v-avatar>
                <img
                  :src="logo.src"
                  :alt="logo.alt"
                  @click="dialog = false"
                >
            </v-avatar>  SimbaKids
          </v-list-item-title>

        </v-list-item>
        <v-divider></v-divider>
       
         <p class="text-h6" align="center"   color="grey">
          About Us
        </p>
        <v-divider></v-divider>
        <v-list-item color="grey" class="p-3">
          SIMBA has grown into an online clothing and kids brand 
          that feels more like a family than a business. operating @Addis Abeba, 
          SIMBA is all about fostering a happy and healthy work-life balance.
        </v-list-item>
        <v-divider></v-divider>
        <br>
          <p class="text-h6 text--secondary" align="center"   color="grey">
            <v-icon>fa fa-map-marker</v-icon> Piazza Addis Ababa, ET 
          </p>
          <iframe 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d9615.72170895908!2d38.74785948089054!3d9.036302241764883!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x3b95017177ec7f0b!2zQXJhZGEgR2l5b3JnaXMo4Yuo4YiY4YqT4YyI4Yi7IOGMiOGKkOGJsCDhjL3hjIwg4YmF4Yux4Yi1IOGMiuGLruGIreGMiuGItSDhiaThibAg4Yqt4Yit4Yi14Ymy4Yur4YqVKQ!5e1!3m2!1sam!2set!4v1636467243722!5m2!1sam!2set" 
            width="100%" 
        
            style="border:0;" 
            allowfullscreen="" 
            loading="lazy">
          </iframe>
         
          <v-row
            justify="center"
          >
            <v-btn
              color="cyan"
              class="ma-2"
              
              @click="dialog = true"
            >
              Zoom
            </v-btn>
      
            <v-dialog
              v-model="dialog"
              fullscreen
              hide-overlay
              transition="dialog-bottom-transition"
              scrollable
            >
              <v-card tile>
                <v-toolbar
                  flat
                  
                  color="cyan"
                >  
                <v-avatar>
                    <img
                      :src="logo.src"
                      :alt="logo.alt"
                      @click="dialog = false"
                    >
                </v-avatar>  
                  <v-spacer />
                  <h3 color="error">SimbaKids</h3>
                  <v-spacer />
                  <v-btn
                    icon
                    
                    @click="dialog = false"
                  >
                    <v-icon>mdi-close</v-icon>
                  </v-btn>
              
              </v-toolbar>
                  <iframe 
                        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d9615.72170895908!2d38.74785948089054!3d9.036302241764883!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x3b95017177ec7f0b!2zQXJhZGEgR2l5b3JnaXMo4Yuo4YiY4YqT4YyI4Yi7IOGMiOGKkOGJsCDhjL3hjIwg4YmF4Yux4Yi1IOGMiuGLruGIreGMiuGItSDhiaThibAg4Yqt4Yit4Yi14Ymy4Yur4YqVKQ!5e1!3m2!1sam!2set!4v1636467243722!5m2!1sam!2set" 
                        width="100%"
                        height="100%" 
                        style="border:0;" 
                        allowfullscreen="" 
                        loading="lazy">
                      </iframe>

                <div style="flex: 1 1 auto;"></div>
              </v-card>
            </v-dialog>

          </v-row>

      </v-list>
      <v-footer
        :absolute="!fixed"
        app
        color="blue"
        align="center"
      >
        <v-btn text color="wighte">SimbaKids &copy;{{ new Date().getFullYear() }}</v-btn>
        <v-btn text color="blue-grey lighten-2">
          powered by:
          <a href="https://sevenoon.pythonanywhere.com/about/" target="_blank">seveNoon</a>
        </v-btn>
      </v-footer>
    </v-navigation-drawer>
    <v-footer
      :absolute="!fixed"
      app
      class="d-flex justify-center"
      justify="center"
      align="center"
    >
      <span align="center">SimbaKids &copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>

  export default {
    data() {
      return{
        clipped: false,
        drawer: false,
        fixed: false,
        miniVariant: false,
        right: true,
        rightDrawer: false,
        title: 'SimbaKids | coming soon',
        timeout: 6000,
        dialog: false,
        logo: {
          src: require('../static/simbakidslogo.png'),
          alt: 'Logo Not Found'

        },
      }

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
            content:'../static/simbakidslogo.png',
          },
          {
            hid: 'og:image',
            property: 'og:image',
            content:'../static/simbakidslogo.png',
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
<style>
  #app {
    background: orange;
    background-size: contain;
  }
</style>




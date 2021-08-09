export default {
  mode: 'universal',
	target: 'static',
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'Search Co. (さちこ)',
    htmlAttrs: {
      lang: 'ja'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: 'stylesheet', href: 'https://fonts.googleapis.com/icon?family=Material+Icons' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '~/assets/css/reset.css',
    '~/assets/css/bootstrap-grid.min.css',
    '~/assets/css/bootstrap-utilities.min.css',
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    // '~/plugins/adobe-fonts',
    '~/plugins/vueselect.js',
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    'nuxt-webfontloader'
  ],

  webfontloader: {
    google: {
      families: ['Noto+Sans:400', 'Noto+Sans+JP:400,700'] 
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {

  },

  generate: {
    async routes () {
      const { $content } = require('@nuxt/content')
      const files = await $content('news' || 'index').fetch()

      return files.map(file => file.path === '/index' ? '/' : file.path)
    }
  }


}

<template>
  <div>
    <HeaderNav />
    <Nuxt />
    <ReturnTop />
    <Footer />
  </div>
</template>

<script>
  import HeaderNav from "@/components/headerNav.vue";
  import Footer from "@/components/footer.vue";
  import ReturnTop from "@/components/ReturnTopButton.vue";
import ReturnTopButton from '../components/ReturnTopButton.vue';
  export default {
		components: {
			HeaderNav,
      Footer,
      ReturnTop
		}
	};
</script>



<style>
html {    
  font-family:
    'Noto Sans',
    'Noto Sans JP',
    'Source Sans Pro',
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    'Helvetica Neue',
    Arial,
    sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
}


.button--green {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #3b8070;
  color: #3b8070;
  text-decoration: none;
  padding: 10px 30px;
}

.button--green:hover {
  color: #fff;
  background-color: #3b8070;
}

.button--grey {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #35495e;
  color: #35495e;
  text-decoration: none;
  padding: 10px 30px;
  margin-left: 15px;
}

.button--grey:hover {
  color: #fff;
  background-color: #35495e;
}


@media screen and (max-width : 767px){
 html,
 body {
 overflow-x: hidden!important;
 overflow-y: scroll;
 -webkit-overflow-scrolling: touch;
 }
}



</style>

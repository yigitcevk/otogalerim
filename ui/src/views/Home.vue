<template>
  <div class='home-frame' style=''>
    <img
      src="@/assets/iconlarge.png"
    />
    <div>
      <a class="button-add" v-on:click="navigateGallery()">
          Galeri girişi
      </a>
      <a class="button-add" v-on:click="navigateUser()">
          Kullanıcı girişi
      </a>
      <div class="lower-page-div">
        <h1>Save time for buying cars!</h1>
        <p>We will search the autogaleries for your dream car.</p>
      </div>
      <img class="tobb-etu-png" src="@/assets/tobbetu.png"/>   

    
    </div>  

    <!-- <SearchCar/> -->
  </div>
</template>

<script>

import SearchCar from '@/components/SearchCar.vue'

export default {
  name: 'Home',
  components: {
    SearchCar,
  },
  methods: {
    navigateUser() {
      this.$router.push({
          name: 'UserPage',
          params: {
          }
      });     
    },
    navigateGallery() {
      this.$router.push({
          name: 'GalleryPage',
          params: {
          }
      });     
    }
  }
}

</script>

<style>

.lower-page-div {
  position: absolute;
  bottom: 0;
  text-align: center;
  padding-left: 38%;
}
.tobb-etu-png {
  position: absolute;
  bottom: 0;
  width: 5%;
  right: 0;
}

</style>

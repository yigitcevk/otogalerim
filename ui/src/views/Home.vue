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



</style>

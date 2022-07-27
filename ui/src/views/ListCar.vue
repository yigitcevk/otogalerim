<template>
  <div class="top-frame">

    <img class="otogalerimicon" src="@/assets/iconlarge.png"/>

  </div>

  <div class="lower-page-div">
    <h1>Save time for buying cars!</h1>
    <p>We will search the autogaleries for your dream car.</p>   
  </div>


</template>

<script>

export default {
  name: 'ListCar',
  components: {
    
  },
  data() {
    return {
      addedCars:[],
      brands:null,
      models:null    
    }
  },
  created() { 
    this.addedCars = this.$route.params.addedCars;
    console.log(this.addedCars)
  },
}

</script>



<style>

.otogalerimicon {
    width: 15%;
    position: absolute;
    left: 0;
    top: 0;
}
</style>


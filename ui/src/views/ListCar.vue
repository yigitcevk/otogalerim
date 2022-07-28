<template>
  <div class="top-frame">
    <img 
    class="otogalerimicon" src="@/assets/iconlarge.png"
    />

    <h1>
        Your cars on sale:
    </h1>    
    <div class ='container' >
        <div>
            <div class='car_card' v-for="item in firstSearchCars" :key="item[0]">
                {{item[1]}} {{item[2]}}
            </div>
        </div>
    </div>


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
      brandId:0,
      modelId:null,
      param:null,
      listCars:[],
      brands:null,
      models:null,
      firstSearchCars:[
      ],
    }
  },
  created() { 
    this.param = this.$route.params.addedCars;
    this.listCars = JSON.parse(this.param);

    fetch("http://127.0.0.1:5000/brands")
      .then(async response => {
        const data = await response.json();

        if (!response.ok) {
          const error = (data && data.message) || response.statusText;
          return Promise.reject(error);
        }
        this.brands = data;
      })
      .catch(error => {
        this.errorMessage = error;
        console.error("There was an error!", error);
      });

    fetch("http://127.0.0.1:5000/models")
      .then(async response => {
        const data = await response.json();

        if (!response.ok) {
          const error = (data && data.message) || response.statusText;
          return Promise.reject(error);
        }

        this.models = data;
      })
      .catch(error => {
        this.errorMessage = error;
        console.error("There was an error!", error);
      });

      const url = 'http://127.0.0.1:5000/listCar/';

      fetch(url, {
                method: 'post',
                headers: {
                    'Content-Type' : 'application/json'
                },
                body: data
            })
      .then(async response => {
        const data = await response.json();

        if (!response.ok) {
          const error = (data && data.message) || response.statusText;
          return Promise.reject(error);
        }

        this.firstSearchCars = data;
      })
      .catch(error => {
        this.errorMessage = error;
        console.error("There was an error!", error);
      });
  },
  methods: {
    tıkla(){
      console.log(this.listCars);
    }
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

.container {
  display:flex;
  text-align: center; 
  align-items: center
}
</style>


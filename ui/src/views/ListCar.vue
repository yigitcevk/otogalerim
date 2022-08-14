<template>
  <div>
    <div class="top-frame">
      <img 
      class="otogalerimicon" src="@/assets/iconlarge.png"
      />
      
      <div class ='container' >

          <div class="first-search-form">
            <div class="filter-form">

              <div class = 'brandCards'>
                <p style='margin:0'>
                  Filters
                </p>
                <div>
                  <label for="brand">
                    Select State
                  </label>
                
                  <select class = 'selectType' name="model" @change="stateClicked($event)">
                      <option v-for="item in state" :key="item.id" :value="item.name">
                          {{item.name}}
                      </option>
                  </select>
                </div>  


              <input class="email-input" style="border-style: solid; margin-top: 5px;" v-model="max_km" placeholder="Enter Maximum KM " />
              <input class="email-input" style="border-style: solid; margin-top: 5px;" v-model="max_price" placeholder="Enter Maximum price" />
              <a style='width:80px' class="button-login" v-on:click="enter()">
                  Enter 
              </a>
            </div>

          </div>
          <div class ='myCars' >
              <div>
                  <div class='car_card' v-for="item in forSaleCars" :key="item[0]">
                      <button class='rmv_sale_button'>
                        From : {{item[1]}} , Rating: {{item[2]}}
                      </button>
                      {{item[3]}} {{item[4]}} {{item[5]}} {{item[6]}} {{item[7]}} {{item[8]}} {{item[9]}} {{item[10]}} {{item[11]}} {{item[12]}} {{item[13]}}
                      <button class='rmv_sale_button' @click="buyCar(item[0])">
                          Buy This Car!
                      </button>
                  </div>
              </div>
          </div>          
          </div>

 
        <div class="filter-search">
          <h1>
            Cars for more detailed search:
          </h1>
          <div class ='myCars' >
              <div>
                  <div class='car_card' v-for="item in forSaleCarsFiltered" :key="item[0]">
                      <button class='rmv_sale_button'>
                        From : {{item[1]}} , Rating: {{item[2]}}
                      </button>
                      {{item[3]}} {{item[4]}} {{item[5]}} {{item[6]}} {{item[7]}} {{item[8]}} {{item[9]}} {{item[10]}} {{item[11]}} {{item[12]}} {{item[13]}}
                      <button class='rmv_sale_button' @click="buyCar(item[0])">
                          Buy This Car!
                      </button>
                  </div>
              </div>
          </div>           
        </div>
        
      </div>

    </div>
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
      forSaleCars:null,
      forSaleCarsFiltered:null,
      max_km:null,
      max_price:null,
      currentColor:'Siyah',
      currentState:'2.el',
      currentFue:'Benzin',
      currentVites:'Manuel',
      currentMotorHacmi:'1.3',
      color : [{'id':'1','name':'Siyah'}, {'id':'2','name':'Gri'},{'id':'3','name':'Kırmızı'}, {'id':'4','name':'Mavi'}, {'id':'5','name':'Lacivert'}, {'id':'6','name':'Beyaz'},{'id':'7','name':'Yeşil'},{'id':'8','name':'Sarı'}],
      state : [{'id':'1','name':'2.el'}, {'id':'2','name':'Sıfır'}],
      fue : [{'id':'1','name':'Benzin'}, {'id':'1','name':'Dizel'}, {'id':'1','name':'LPG'}, {'id':'1','name':'Elektrik'}, {'id':'1','name':'Benzin & LPG'}],
      vites : [{'id':'1','name':'Manuel'},{'id':'2','name':'Yarı Otomatik'}, {'id':'3','name':'Otomatik'}],
      motor_hacmi : [{'id':'1','name':'1.3'}, {'id':'2','name':'1.4'}, {'id':'3','name':'1.5'}, {'id':'4','name':'1.6'}]
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

      const url = 'http://127.0.0.1:5000/listCar'; 
      
      let carData = JSON.stringify(this.listCars);
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: carData
      };


    fetch(url,requestOptions)
      .then(async response => {
        const data = await response.json();

        if (!response.ok) {
          const error = (data && data.message) || response.statusText;
          return Promise.reject(error);
        }
        this.forSaleCars = data;
      })
      .catch(error => {
        this.errorMessage = error;
        console.error("There was an error!", error);
      });

  },
  methods: {
    buyCar(car_id){
      this.$router.push({
          name: 'BuyCar',
          params: {
            car_id:car_id
          }
      });  
    },
    colorClicked(e){
            this.currentColor = e.target.value;
    },
    stateClicked(e){
        this.currentState = e.target.value;
        this.max_km = 0;
    },    
    fueClicked(e){
        this.currentFue = e.target.value;
    },       
    vitesClicked(e){
        this.currentVites = e.target.value;
    },      
    hacimClicked(e){
        this.currentMotorHacmi = e.target.value;
    },
    enter(){
      if (this.max_km == null) {
        alert('Maximum km should be given');
      }
      if (this.max_price == null) {
        alert('Maximum price should be given');
      }
      let carData = JSON.stringify({'cars':this.listCars,'max_km':this.max_km,'max_price':this.max_price,'state':this.currentState});
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: carData
      };
    const url = 'http://127.0.0.1:5000/listCarFilter'; 
    fetch(url,requestOptions)
      .then(async response => {
        const data = await response.json();

        if (!response.ok) {
          const error = (data && data.message) || response.statusText;
          return Promise.reject(error);
        }
        this.forSaleCarsFiltered = data;
        console.log(this.forSaleCarsFiltered);
      })
      .catch(error => {
        this.errorMessage = error;
        console.error("There was an error!", error);
      });
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
  align-items: center;
}

.top-frame {
  display: flex;
}

.first-search-form{
  margin-top: 3%;
  width: 100%;
  display:flex;
  text-align: center; 
  align-items: center;
  flex-direction: row;
}

.filter-form{
  margin-top: 8px;
  width: 100%;
  text-align: center; 
  display:contents;
}

.filter-search{
  margin-top: 5px;
  width: 100%;
  display:flex;
  text-align: center; 
  align-items: center;
}

</style>


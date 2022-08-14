<template>
  <div>
    <div class="top-frame">
      <img 
      class="otogalerimicon" src="@/assets/iconlarge.png"
      />
      
      <div class ='container' >

          <div class="first-search-form">
              <h1>
              Cars for your search:
              </h1>
              <div class ='myCars' >
                  <div>
                      <div class='car_card' v-for="item in forSaleCars" :key="item[0]">
                          {{item[1]}} {{item[2]}} {{item[3]}} {{item[4]}} {{item[5]}} {{item[6]}} {{item[7]}} {{item[8]}} {{item[9]}} {{item[10]}} {{item[11]}}
                          <button class='rmv_sale_button' @click="buyCar(item[0])">
                              Buy This Car!
                          </button>
                      </div>
                  </div>
              </div>
          </div>


          <div class="filter-form">
            <h1>
              Filter for more detailed search:
            </h1>

            <div class = 'brandCards'>

              <div>
                <label for="brand">
                  Select Color
                </label>
              
                <select class = 'selectType' name="model" @change="colorClicked($event)">
                    <option v-for="item in color" :key="item.id" :value="item.name">
                        {{item.name}}
                    </option>
                </select>
              </div>

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

              <div>
                <label for="brand">
                  Select Fue
                </label>
              
                <select class = 'selectType' name="model" @change="fueClicked($event)">
                  <option v-for="item in fue" :key="item.id" :value="item.name">
                      {{item.name}}
                  </option>
                </select>
              </div> 

              <div>
                <label for="brand">
                  Select Vites
                </label>
              
                <select class = 'selectType' name="model" @change="vitesClicked($event)">
                    <option v-for="item in vites" :key="item.id" :value="item.name">
                        {{item.name}}
                    </option>
                </select>
              </div>       


            <div>
              <label for="brand">
                Select Volume
              </label>
            
              <select class = 'selectType' name="model" @change="hacimClicked($event)">
                  <option v-for="item in motor_hacmi" :key="item.id" :value="item.name">
                      {{item.name}}
                  </option>
              </select>
            </div>

            <input class="email-input" style="border-style: solid; margin-top: 5px;" v-model="hp" placeholder="Enter HP range" />
            <input class="email-input" style="border-style: solid; margin-top: 5px;" v-model="km" placeholder="Enter KM range" />
            <input class="email-input" style="border-style: solid; margin-top: 5px;" v-model="uretim_yili" placeholder="Enter Production Year range" />
            <a style='width:80px' class="button-login" v-on:click="enter()">
                Enter 
            </a>
          </div>

        </div>

        <div class="filter-search">
          <h1>
            Cars for more detailed search:
          </h1>
        </div>
        
      </div>

    </div>

    <div class="lower-page-div">
      <h1>Save time for buying cars!</h1>
      <p>We will search the autogaleries for your dream car.</p>   
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

      alert(carData);


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
      console.log(this.currentColor);
      console.log(this.currentMotorHacmi);
      console.log(this.currentFue);
      console.log(this.currentState);
      console.log(this.currentVites);
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


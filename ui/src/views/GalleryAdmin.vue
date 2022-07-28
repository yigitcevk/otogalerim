<template>
  <div style='heigth:100vh'>
    <h1>
        Your cars on sale:
    </h1>    
    <div class ='myCars' >
        <div>
            <div class='car_card' v-for="item in forSaleCars" :key="item[0]">
                {{item[1]}} {{item[2]}} {{item[3]}} {{item[4]}} {{item[5]}} {{item[6]}} {{item[7]}} {{item[8]}} {{item[9]}} {{item[10]}} {{item[11]}}
                <button class='rmv_sale_button' @click="removeCarFromSale(item[0])">
                    Remove From Sale
                </button>
            </div>
        </div>
    </div>

    <h1>
        Place your other cars for sale!!
    </h1>

    <select class='selectType' @change="carClicked($event)" >
        <option v-for="item in noSaleCars" :key="item[0]" :value="item[0]" >
            {{item[1]}} {{item[2]}} {{item[3]}} {{item[4]}} {{item[5]}} {{item[6]}} {{item[7]}} {{item[8]}} {{item[9]}} {{item[10]}}
        </option>
    </select>

    <div style="display:flex;flex-direction:column">
        <input class="email-input" style="border-style: solid; margin-top: 5px;" v-model="price" v-on:keyup.enter="login"  placeholder="Enter Price" />
        <a style='width:80px' class="button-login" v-on:click="place()">
            Place 
        </a>

    </div>

    <h1>
       Enter your new car to system!!
    </h1>    


  <div class = 'brandCards'>
      <div>
        <label for="brand">
          Select Brand
        </label>
        <select class='selectType' name="brand" @change="brandClicked($event)" >
          <option v-for="item in brands" :key="item.id" :value="item.id">
              {{item.name}}
          </option>
        </select>
      </div>

      <div>
        <label for="brand">
          Select Model
        </label>
      
        <select v-if="models!=null" class = 'selectType' name="model" @change="modelClicked($event)">
            <option v-for="item in models[brandId]" :key="item.id" :value="item.id">
                {{item.name}}
            </option>
        </select>
      </div>


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

    <input class="email-input" style="border-style: solid; margin-top: 5px;" v-model="hp" placeholder="Enter HP" />
    <input class="email-input" style="border-style: solid; margin-top: 5px;" v-model="km" placeholder="Enter KM" />
    <input class="email-input" style="border-style: solid; margin-top: 5px;" v-model="uretim_yili" placeholder="Enter Production Year" />
    <a style='width:80px' class="button-login" v-on:click="enter()">
        Enter 
    </a>
  </div>

  </div>
</template>

<script>


export default {
    name: 'GalleryAdmin',
    components: {
    },
    data(){
        return{
            brandId:0,
            modelId:null,            
            galleryId:'',
            forSaleCars:[],
            noSaleCars:[],
            price:null,
            km:null,
            hp:null,
            currentCar:null,
            brands:null,
            models:null,
            uretim_yili:null,
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

        this.galleryId = this.$route.params.galleryId;

        const url = 'http://127.0.0.1:5000/galleryForSale/' + this.galleryId;

        fetch(url)
        .then(async response => {
            const data = await response.json();

            if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
            }
            this.forSaleCars = data;
            console.log(this.forSaleCars);
        })
        .catch(error => {
            this.errorMessage = error;
            console.error("There was an error!", error);
        });

        const url2 = 'http://127.0.0.1:5000/galleryNoSaleCars/' + this.galleryId;        

        fetch(url2)
        .then(async response => {
            const data = await response.json();
            if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
            }
            this.noSaleCars = data;
            this.currentCar = data[0][0];
        })
        .catch(error => {
            this.errorMessage = error;
            console.error("There was an error!", error);
        });

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

    },
    methods: {
        removeCarFromSale(car_id) {
            let data =JSON.stringify({"car_id":car_id});    
            const url = 'http://127.0.0.1:5000/removeCarFromSale'; 

            fetch(url, {
                method: 'post',
                headers: {
                    'Content-Type' : 'application/json'
                },
                body: data
            }).then(function(response){
                return response.json(myvalue);
            }).then(function(text){
                console.log(text);
            }).catch(function (error){
                console.error(error);
            });
            location.reload();
        },
        brandClicked(e) {
            this.brandId = e.target.value;
            this.modelId = this.models[this.brandId][0].id;
        },
        modelClicked(e){
            this.modelId = e.target.value;
        },        
        carClicked(e){
            this.currentCar = e.target.value;
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
        place() {            
            let data =JSON.stringify({"car_id":this.currentCar,"gallery_id":this.galleryId,"price":this.price});    
            const url = 'http://127.0.0.1:5000/placeCar'; 

            fetch(url, {
                method: 'post',
                headers: {
                    'Content-Type' : 'application/json'
                },
                body: data
            }).then(function(response){
                return response.json(myvalue);
            }).then(function(text){
                console.log(text);
            }).catch(function (error){
                console.error(error);
            });
            location.reload();            
        },
        enter() {
            if (this.brandId == 0) {
                alert('brand and model should be selected!');
                return;
            }
            let data =JSON.stringify(
                {
                    "brand_id":this.brandId,
                    "model_id":this.modelId,
                    "color":this.currentColor,
                    "state":this.currentState,
                    "fue":this.currentFue,
                    "vites":this.currentVites,
                    "motor_hacmi":this.currentMotorHacmi,
                    "motor_gucu":this.hp,
                    "km":this.km,
                    "gallery_id":this.galleryId,
                    "uretim_yili":this.uretim_yili
                });

            const url = 'http://127.0.0.1:5000/enterCar'; 

            fetch(url, {
                method: 'post',
                headers: {
                    'Content-Type' : 'application/json'
                },
                body: data
            }).then(function(response){
                return response.json(myvalue);
            }).then(function(text){
                console.log(text);
            }).catch(function (error){
                console.error(error);
            });
            location.reload();  
        }        
    },

}

</script>

<style scoped>


.car_card {
  background: #fff;
  max-width: 1000px;
  border-radius: 10px;
  box-shadow: 1px 1px 2rem rgba(0, 0, 0, 0.3);
  display: flex;
  flex-direction:row;
}

.rmv_sale_button {
    margin-left: 30px;
    background-color: red;
    color: black;
    border: none;
    cursor: pointer;
}

.add_sale_button {
    margin-left:30px;
    background-color: green;
    color: black;
    border: none;
    cursor: pointer;
}

.myCars{

}


</style>
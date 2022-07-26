<template>
    <div class="top-frame">

        <img class="otogalerimicon"
            src="@/assets/iconlarge.png"
        />

        <div class="container" style="text-align: center; align-items: center">

            <div class = 'galleryEmailCards'>
                <div>
                    <label for="brand">
                    Enter email
                    </label>
                    <input class="email-input" v-model="message" placeholder="Enter email" />
                </div>

                <a class="button-add" v-on:click="newCar()">
                    Login 
                </a>

            </div>  

                <h1>
                Save time for buying cars!
                </h1>
                <p>
                We will search the autogaleries for your dream car.
                </p>
        </div>



    </div>
</template>

<script>

import { isProxy, toRaw } from 'vue';

export default {
  name: 'SearchCar',
  components: {
  },
  data() {
    return {
      key:"",
      query: "",
      brandId:0,
      modelId:null,
      addedCars:[],
      brands:null,
      models:null,      
    }
  },
  watch: {
    curQuery(newVal) {
      this.query = newVal;
    }
  },
  created() {

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
    brandClicked(e) {
      this.brandId = e.target.value;
      this.modelId = this.models[this.brandId][0].id;
    },
    modelClicked(e){
      this.modelId = e.target.value;
    },
    newCar() {
      let index = 0
      for (let i = 0; i < this.models[this.brandId].length ; i++) {
        if (this.models[this.brandId][i].id ===this.modelId)
          index = i;
      }
      let car = this.addedCars.find(car => car.brandId === this.brandId && car.index === index)
      if (car == null) {
        this.addedCars.push({"brandId":this.brandId,"index":index});
      }
      else {
        alert("this car is already added");
        return;
      }
      this.brandId = 0;
      this.modelId = null;
    },
    removeCar(item) {
      this.addedCars = this.addedCars.filter(data => (data.index != item.index || data.brandId != item.brandId));
    }
  }
}

</script>


<style>

.email-input {
    width:160px
}

.otogalerimicon {
    width: 15%;
    position: absolute;
    left: 0;
    top: 0;
}

.container{
    display: flex;
    position: absolute;
    margin-top: 80px;
}

.form {
  display: flex;
  flex-direction: row;
  background: #ffffff;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.05), 0px 25px 35px rgba(0, 0, 0, 0.03);
  border-radius: 8px;
  max-width: 664px;
  width: 100%;
  height: 56px;
  padding: 2px;
  margin:8px;

}

.form:hover{
  box-shadow: 0px 0px 20px gray;
  transition: box-shadow 0.2s ease-in-out;
}

.form:focus-within{
  box-shadow: 0px 0px 20px gray;
  transition: box-shadow 0.2s ease-in-out;
}

.button-added{
  cursor: pointer;
  float: right;
  padding: 14px 24px;
  margin:8px;
  background: #ffffff;
  color: #1b449c;
  text-decoration: none;
  font-weight: bold;
  border: 2px solid #1b449c;
  box-sizing: border-box;
  border-radius: 40px;  
}

.addedCars{
  display:flex;
  flex-direction:row;

}

.selectType{

  width:160px
}


.button-add:hover{
  box-shadow: 0px 0px 20px black;
  transition: box-shadow 0.2s ease-in-out;  
}

.button-add {
  cursor: pointer;
  float: right;
  padding: 8px 12px;
  margin-top:5px;
  margin-bottom:5px;
  background: #1b449c;
  color: #ffffff;
  width:50%;
  text-decoration: none;
  font-weight: bold;
  border: 2px solid #1b449c;
  box-sizing: border-box;
  border-radius: 40px;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
}


.button-add > .text {
  font-size: 8px;
  vertical-align: middle;
}

.galleryEmailCards{

  display: flex;
  flex-direction: column;
  text-align:center;
  align-items: center;
  /* This bit draws the box around it */
  background: #ffffff;
  /* Shadow / 1 */
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.05), 0px 25px 35px rgba(0, 0, 0, 0.03);
  border-radius: 8px;
  width:20%;
}


</style>

<template>
<div class="top-frame">


  <div class="container" style="text-align: center; align-items: center">
    <img
      src="@/assets/iconlarge.png"
      v-bind:style="[
        curQuery ? 'width:100px;height:100px;float:left;' : '',
      ]"
    />

  <div class = 'brandCards'>
      <div>
        <label for="brand">
          Select Brand
        </label>
        <select :placeholder="[[ asd ]]" class='selectType' name="brand" @change="brandClicked($event)" >
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

      <a class="button-add" v-on:click="newCar()">
          Add
      </a>

  </div>


  <div class="form">
    <div class='addedCars'>
      <div v-for="item in addedCars" :key="item.modelId">
          <a class='button-white' @click="removeCar(item)">
            {{brands[item.brandId].name}} {{models[item.brandId][item.modelId].name}} 
          </a>
      </div>
    </div>
  </div>

  <div style='width:200px'>
    <a class="button-add" v-on:click="search()">
        Search
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
  async created() {
    const response = await fetch("http://127.0.0.1:5000/brands");
    const data = await response.json();
    this.brands = data;
    const response2 = await fetch("http://127.0.0.1:5000/models");
    const data2 = await response2.json();
    this.models = data2;    
  },
  methods: {
    brandClicked(e) {
      this.brandId = e.target.value;
    },
    modelClicked(e){
      this.modelId = e.target.value;
    },
    newCar() {
      let car = this.addedCars.find(car => car.brandId === this.brandId && car.modelId === this.modelId)
      if (car == null)   
        this.addedCars.push({"brandId":this.brandId,"modelId":this.modelId})
      else
        alert("this car is already added");
    },
    removeCar(item) {
      this.addedCars = this.addedCars.filter(data => (data.modelId != item.modelId || data.brandId != item.brandId));
    }
  }
}

</script>


<style>

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
  color: #0d1821;
  text-decoration: none;
  font-weight: bold;
  border: 2px solid #0d1821;
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
  background: #0d1821;
  color: #ffffff;
  width:50%;
  text-decoration: none;
  font-weight: bold;
  border: 2px solid #0d1821;
  box-sizing: border-box;
  border-radius: 40px;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
}


.button-add > .text {
  font-size: 8px;
  vertical-align: middle;
}

.brandCards{

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

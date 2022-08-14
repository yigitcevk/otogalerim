<template>
    <div class="top-frame">

        <img class="otogalerimicon"
            src="@/assets/iconlarge.png"
        />

        <div class="container" style="text-align: center; align-items: center">
            
            <div class = 'brandCards'>
                <div>
                    <h4>
                        {{car[0][1]}} {{car[0][2]}} {{car[0][3]}} {{car[0][4]}} Renk 
                    </h4>
                </div>

                <h4>
                    Durum : {{car[0][5]}} Km : {{car[0][6]}} <br> Yakıt : {{car[0][7]}} Vites : {{car[0][8]}} <br> 
                    Motor Hacmi : {{car[0][9]}} Motor Gücü : {{car[0][10]}} <br> Fiyat : {{car[0][11]}}
                </h4>                
                <label for="brand">
                    Select Rating for this sale
                </label>
            
                <select class = 'selectType' name="model" @change="pointClicked($event)">
                    <option v-for="item in point" :key="item.id" :value="item.name">
                        {{item.name}}
                    </option>
                </select>  

                <a class="button-add" v-on:click="buy()">
                    Buy
                </a>

            </div>

            <h1>Save time for buying!</h1>
            <p>We will search the autogaleries for your dream car.</p>
        </div> 



    </div>
</template>

<script>

import { isProxy, toRaw } from 'vue';

export default {
  name: 'GalleryLogin',
  components: {
  },
  data() {
    return {
        car:null,
        car_id:null,
        currentPoint:'1',
        point : [{'id':'1','name':'1'}, {'id':'2','name':'2'}, {'id':'3','name':'3'}, {'id':'4','name':'4'},{'id':'5','name':'5'}]
    }
  },
  created() { 
    this.car_id = this.$route.params.car_id;
    const url = 'http://127.0.0.1:5000/viewCar/' + this.car_id; 
    fetch(url)
    .then(async response => {
        const data = await response.json();
        if (!response.ok) {
        const error = (data && data.message) || response.statusText;
        return Promise.reject(error);
        }
        this.car = data;
    })
    .catch(error => {
        this.errorMessage = error;
        console.error("There was an error!", error);
    });  
  },
  methods: {
    pointClicked(e){
        this.currentPoint = e.target.value;
    },
    buy() {
        let data =JSON.stringify({"car_id":this.car_id,"rating":this.currentPoint});    
        const url = 'http://127.0.0.1:5000/buy'; 
        fetch(url, {
            method: 'post',
            headers: {
                'Content-Type' : 'application/json'
            },
            body: data
        }).then(function(response){
            console.log(response)
        }).then(function(text){
            console.log(text);
        }).catch(function (error){
            console.error(error);
        });

        this.$router.push({
            name: 'UserPage',
            params: {
            }
        });

 
    }         
  }
}

</script>


<style>

.email-input {
    width:250px;
    border-radius: 8px;
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

.addedCars{
  display:flex;
  flex-direction:row;

}

.button-login:hover{
  box-shadow: 0px 0px 20px black;
  transition: box-shadow 0.2s ease-in-out;  
}

.button-login {
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


.button-login > .text {
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
  width:40%;
}


</style>

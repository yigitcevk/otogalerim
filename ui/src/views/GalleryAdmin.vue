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



  </div>
</template>

<script>


export default {
    name: 'GalleryAdmin',
    components: {
    },
    data(){
        return{
            galleryId:'',
            forSaleCars:[],
            noSaleCars:[],
            price:null,
            currentCar:null
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
        carClicked(e){
            this.currentCar = e.target.value;
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
        }
    }
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
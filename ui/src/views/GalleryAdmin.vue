<template>
  <div style='heigth:100vh'>
    <div v-for="item in myCars" :key="item[0]">
        {{item[1]}} {{item[2]}} {{item[3]}} {{item[4]}} {{item[5]}} {{item[6]}} {{item[7]}} {{item[8]}} {{item[9]}} {{item[10]}} {{item[11]}}
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
            myCars:[]
        }
    },
    created() {

        this.galleryId = this.$route.params.galleryId;

        const url = 'http://127.0.0.1:5000/galleryCars/' + this.galleryId;

        fetch(url)
        .then(async response => {
            const data = await response.json();

            if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
            }
            this.myCars = data;
            console.log(this.myCars);
        })
        .catch(error => {
            this.errorMessage = error;
            console.error("There was an error!", error);
        });

    },
    methods: {
        login() {
            alert(galleryId);
        }
    }
}

</script>

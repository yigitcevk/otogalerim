<template>
  <div style='heigth:100vh'>

  </div>
</template>

<script>


export default {
    name: 'GalleryAdmin',
    components: {
    },
    data(){
        return{
            galleryId:''
        }
    },
    created() {
        this.galleryId = this.$route.params.galleryId;
    },
    methods: {
        login() {
            alert(galleryId);
        }
    }
}

</script>

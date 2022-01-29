<template>
  <div v-if="isLoading" class="loading">LOADING.....</div>
  <div v-else-if="!isLoading && isError"><h2 class="error">Failed to Fetch Data....</h2></div>
  <div v-else>
    <gallery-container></gallery-container>
  </div>
</template>

<script>
import GalleryContainer from "./GalleryContainer.vue";
export default {
  inject: ['domain'],
  components: { GalleryContainer },
  provide() {
    return {
      data: this.imgUrls,
    };
  },
  data() {
    return {
      isLoading: false,
      imgUrls: [],
    };
  },
  created() {
    this.isLoading = true;
    console.log("Loading started!");
    this.axios
      .get("http://"+ this.domain +"/gallery", {auth:{username: 'hasanprakash', password: '@hasanprakash'}})
      .then((response) => {
        for (let i = 0; i < response.data.length; i++) {
          this.imgUrls.push(response.data[i]);
        }
        console.log("Loadingg completed");
        this.isLoading = false;
      })
      .catch((e) => {
        console.log(e);
        this.isError = true;
        this.isLoading = false;
      });
  },
};
</script>

<style scoped>
.loading {
  height: 400px;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgb(231, 231, 231);
}
</style>

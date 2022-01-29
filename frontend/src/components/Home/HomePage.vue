<template>
  <my-carousal></my-carousal>
  <!-- <image-carousal></image-carousal> -->
  <uevents-container v-if="!isError && !isLoading" :data="upcomingEvents"></uevents-container>
  <my-loader v-else-if="!isError" title="HANG ONN!!!" lheight="400px"></my-loader>
  <h2 class="error" v-else>Got Error While Retriving Data..</h2>
</template>

<script>
// import ImageCarousal from "./ImageCarousal.vue";
import MyCarousal from './MyCarousal.vue';
import UeventsContainer from './UeventsContainer.vue';
export default {
  inject: ['domain'],
  components: {
    // ImageCarousal,
    UeventsContainer,
    MyCarousal,
  },
  data() {
    return {
      isError: false,
      isLoading: false,
      upcomingEvents: [
        // {
        //   title: 'Title1',
        //   subtitle: 'subtitle1',
        //   url: 'https://c0.wallpaperflare.com/preview/483/210/436/car-green-4x4-jeep.jpg'
        // },
      ]
    }
  },
  created() {
    this.isLoading = true
    this.axios.get('https://'+ this.domain +'/upcomingevents', {auth:{username: 'hasanprakash', password: '@hasanprakash'}})
    .then((response) => {
      console.log(response.data);
      for(let i=0;i<response.data.length;i++) {
        this.upcomingEvents.push(response.data[i]);
      }
      this.isLoading = false;
    })
    .catch(e => {
      console.log(e);
      this.isError = true;
      this.isLoading = false;
    })
  }
};
</script>

<style scoped>
</style>

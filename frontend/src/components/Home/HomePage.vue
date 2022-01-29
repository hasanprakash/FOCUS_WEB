<template>
  <my-carousal></my-carousal>
  <!-- <image-carousal></image-carousal> -->
  <uevents-container v-if="!isError" :data="upcomingEvents"></uevents-container>
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
    MyCarousal
  },
  data() {
    return {
      isError: false,
      upcomingEvents: [
        // {
        //   title: 'Title1',
        //   subtitle: 'subtitle1',
        //   url: 'https://c0.wallpaperflare.com/preview/483/210/436/car-green-4x4-jeep.jpg'
        // },
        // {
        //   title: 'Title1',
        //   subtitle: 'subtitle2',
        //   url: 'https://c0.wallpaperflare.com/preview/483/210/436/car-green-4x4-jeep.jpg'
        // },
        // {
        //   title: 'Title3',
        //   subtitle: 'subtitle3',
        //   url: 'https://c0.wallpaperflare.com/preview/483/210/436/car-green-4x4-jeep.jpg'
        // },
        // {
        //   title: 'Title4',
        //   subtitle: 'subtitle4',
        //   url: 'https://c0.wallpaperflare.com/preview/483/210/436/car-green-4x4-jeep.jpg'
        // },
        // {
        //   title: 'Title5',
        //   subtitle: 'subtitle5',
        //   url: 'https://c0.wallpaperflare.com/preview/483/210/436/car-green-4x4-jeep.jpg'
        // },
        // {
        //   title: 'Title6',
        //   subtitle: 'subtitle6',
        //   url: 'https://c0.wallpaperflare.com/preview/483/210/436/car-green-4x4-jeep.jpg'
        // },
      ]
    }
  },
  created() {
    this.axios.get('http://'+ this.domain +'/upcomingevents', {auth:{username: 'hasanprakash', password: '@hasanprakash'}})
    .then((response) => {
      console.log(response.data);
      for(let i=0;i<response.data.length;i++) {
        this.upcomingEvents.push(response.data[i]);
      }
    })
    .catch(e => {
      console.log(e);
      this.isError = true;
    })
  }
};
</script>

<style scoped>
</style>

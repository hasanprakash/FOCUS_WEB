<template>
  <image-carousal></image-carousal>
  <uevents-container :data="upcomingEvents"></uevents-container>
</template>

<script>
import ImageCarousal from "./ImageCarousal.vue";
import UeventsContainer from './UeventsContainer.vue';
export default {
  components: {
    ImageCarousal,
    UeventsContainer,
  },
  data() {
    return {
      upcomingEvents: [
        {
          title: 'Title1',
          subtitle: 'subtitle1',
          url: 'https://c0.wallpaperflare.com/preview/483/210/436/car-green-4x4-jeep.jpg'
        },
        {
          title: 'Title1',
          subtitle: 'subtitle2',
          url: 'https://c0.wallpaperflare.com/preview/483/210/436/car-green-4x4-jeep.jpg'
        },
        {
          title: 'Title3',
          subtitle: 'subtitle3',
          url: 'https://c0.wallpaperflare.com/preview/483/210/436/car-green-4x4-jeep.jpg'
        },
        {
          title: 'Title4',
          subtitle: 'subtitle4',
          url: 'https://c0.wallpaperflare.com/preview/483/210/436/car-green-4x4-jeep.jpg'
        },
        {
          title: 'Title5',
          subtitle: 'subtitle5',
          url: 'https://c0.wallpaperflare.com/preview/483/210/436/car-green-4x4-jeep.jpg'
        },
        {
          title: 'Title6',
          subtitle: 'subtitle6',
          url: 'https://c0.wallpaperflare.com/preview/483/210/436/car-green-4x4-jeep.jpg'
        },
      ]
    }
  }
};
</script>

<style></style>

<template>
  <gallery-container></gallery-container>
</template>

<script>
import GalleryContainer from './GalleryContainer.vue';
export default {
  components: { GalleryContainer },
  provide() {
    return {
      data: this.imgUrls
    }
  },
  data() {
    return {
      imgUrls: [
        {
          id: '1',
          url: 'https://wallpaperaccess.com/full/82956.jpg'
        },
        {
          id: '2',
          url: 'https://media.istockphoto.com/photos/very-closeup-view-of-amazing-domestic-pet-in-mirror-round-fashion-is-picture-id1281804798?b=1&k=20&m=1281804798&s=170667a&w=0&h=HIWbeaP_cQSngCz7l9t3xwyE2eyzVgIy3K6xIqPhJQA=',
        },
        {
          id: '3',
          url: 'https://i.pinimg.com/originals/d0/bc/33/d0bc33dce3dc0a6f2fab4fd38ad8c131.jpg'
        },
        {
          id: '4',
          url: 'https://lh6.googleusercontent.com/-d3UBdVlclYE/T_s2pyG8J4I/AAAAAAAAGTo/5fiMHeKz24g/s1600/Cool-Cat-Picture-2.jpg',
        },
        {
          id: '5',
          url: 'https://www.desktopbackground.org/p/2010/05/15/17937_amazingly-cool-cats-wallpapers_2560x1920_h.jpg',
        },
        {
          id: '6',
          url: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrqBsZ15qFH1sICBMpPX-hy3mne8B37Dogdw&usqp=CAU',
        },
        {
          id: '7',
          url: 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=640:*',
        },
        {
          id: '8',
          url: 'https://i.pinimg.com/originals/e2/42/1e/e2421ea92c654c3e88aa220b69cbd9e3.jpg',
        },
        {
          id: '9',
          url: 'https://wallpaperaccess.com/full/390975.jpg', 
        },
        {
          id: '10',
          url: 'https://hgtvhome.sndimg.com/content/dam/images/hgtv/fullset/2018/3/22/0/shutterstock_national-puppy-day-224423782.jpg.rend.hgtvcom.966.725.suffix/1521744674350.jpeg',
        },
        {
          id: '11',
          url: 'https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/newscms/2018_20/1339472/puppy-cute-today-180515-tease.jpg', 
        },
        {
          id: '12',
          url: 'https://parade.com/wp-content/uploads/2021/02/cutest-dog-breeds-1024x683.jpg'
        },
        {
          id: '13',
          url: 'https://cdn.wallpapersafari.com/93/51/jDaydf.jpg', 
        }, 
        {
          id: '14',
          url: 'https://images.theconversation.com/files/224977/original/file-20180626-112611-1uf34g4.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1200&h=675.0&fit=crop',
        },
        {
          id: '15',
          url: 'https://nypost.com/wp-content/uploads/sites/2/2020/05/hamster-covid-spread-masks-01.jpg?quality=80&strip=all'
        }
      ]
    }
  }
};
</script>

<style scoped>

</style>

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
  components: { GalleryContainer },
  provide() {
    return {
      data: this.imgUrls,
    };
  },
  data() {
    return {
      isLoading: false,
      imgUrls: [
        // {
        //   id: '1',
        //   url: 'https://wallpaperaccess.com/full/82956.jpg'
        // },
        // {
        //   id: '3',
        //   url: 'https://i.pinimg.com/originals/d0/bc/33/d0bc33dce3dc0a6f2fab4fd38ad8c131.jpg'
        // },
        // {
        //   id: '4',
        //   url: 'https://lh6.googleusercontent.com/-d3UBdVlclYE/T_s2pyG8J4I/AAAAAAAAGTo/5fiMHeKz24g/s1600/Cool-Cat-Picture-2.jpg',
        // },
        // {
        //   id: '5',
        //   url: 'https://www.desktopbackground.org/p/2010/05/15/17937_amazingly-cool-cats-wallpapers_2560x1920_h.jpg',
        // },
        // {
        //   id: '7',
        //   url: 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=640:*',
        // },
        // {
        //   id: '9',
        //   url: 'https://wallpaperaccess.com/full/390975.jpg',
        // },
        // {
        //   id: '10',
        //   url: 'https://hgtvhome.sndimg.com/content/dam/images/hgtv/fullset/2018/3/22/0/shutterstock_national-puppy-day-224423782.jpg.rend.hgtvcom.966.725.suffix/1521744674350.jpeg',
        // },
        // {
        //   id: '11',
        //   url: 'https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/newscms/2018_20/1339472/puppy-cute-today-180515-tease.jpg',
        // },
        // {
        //   id: '12',
        //   url: 'https://parade.com/wp-content/uploads/2021/02/cutest-dog-breeds-1024x683.jpg'
        // },
        // {
        //   id: '13',
        //   url: 'https://cdn.wallpapersafari.com/93/51/jDaydf.jpg',
        // },
        // {
        //   id: '14',
        //   url: 'https://images.theconversation.com/files/224977/original/file-20180626-112611-1uf34g4.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1200&h=675.0&fit=crop',
        // },
        // {
        //   id: '15',
        //   url: 'https://nypost.com/wp-content/uploads/sites/2/2020/05/hamster-covid-spread-masks-01.jpg?quality=80&strip=all'
        // },
        // {
        //   id: '16',
        //   url: 'https://wallpaperaccess.com/full/82956.jpg'
        // },
        // {
        //   id: '17',
        //   url: 'https://i.pinimg.com/originals/d0/bc/33/d0bc33dce3dc0a6f2fab4fd38ad8c131.jpg'
        // },
        // {
        //   id: '18',
        //   url: 'https://lh6.googleusercontent.com/-d3UBdVlclYE/T_s2pyG8J4I/AAAAAAAAGTo/5fiMHeKz24g/s1600/Cool-Cat-Picture-2.jpg',
        // },
        // {
        //   id: '19',
        //   url: 'https://www.desktopbackground.org/p/2010/05/15/17937_amazingly-cool-cats-wallpapers_2560x1920_h.jpg',
        // },
        // {
        //   id: '20',
        //   url: 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=640:*',
        // },
        // {
        //   id: '21',
        //   url: 'https://wallpaperaccess.com/full/390975.jpg',
        // },
        // {
        //   id: '22',
        //   url: 'https://hgtvhome.sndimg.com/content/dam/images/hgtv/fullset/2018/3/22/0/shutterstock_national-puppy-day-224423782.jpg.rend.hgtvcom.966.725.suffix/1521744674350.jpeg',
        // },
        // {
        //   id: '23',
        //   url: 'https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/newscms/2018_20/1339472/puppy-cute-today-180515-tease.jpg',
        // },
        // {
        //   id: '24',
        //   url: 'https://parade.com/wp-content/uploads/2021/02/cutest-dog-breeds-1024x683.jpg'
        // },
        // {
        //   id: '25',
        //   url: 'https://cdn.wallpapersafari.com/93/51/jDaydf.jpg',
        // },
        // {
        //   id: '26',
        //   url: 'https://images.theconversation.com/files/224977/original/file-20180626-112611-1uf34g4.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1200&h=675.0&fit=crop',
        // },
        // {
        //   id: '27',
        //   url: 'https://nypost.com/wp-content/uploads/sites/2/2020/05/hamster-covid-spread-masks-01.jpg?quality=80&strip=all'
        // }
      ],
    };
  },
  created() {
    this.isLoading = true;
    console.log("Loading started!");
    this.axios
      .get("http://localhost:8000/gallery", {auth:{username: 'hasanprakash', password: '@hasanprakash'}})
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

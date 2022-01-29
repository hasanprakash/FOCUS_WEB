<template>
  <div v-if="!isError && !isLoading" class="container" style="text-align: center">
    <events-container v-if="!isLoading" :data="events"></events-container>
  </div>
  <my-loader v-else-if="!isError" title='PLEASE WAIT' lheight="400px"></my-loader>
  <h2 v-else class="error">Failed To Fetch Data....</h2>
</template>

<script>
import EventsContainer from "./EventsContainer.vue";
export default {
  inject: ['domain'],
  components: { EventsContainer },
  data() {
    return {
      isError: false,
      isLoading: false,
      events: [
        // {
        //   heading: 'Y19 48-Hr Skill Development Project-3',
        //   description: 'description',
        //   imgUrl: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimage.flaticon.com%2Ficons%2Fpng%2F512%2F25%2F25231.png&f=1&nofb=1'
        // }, 
      ],
    };
  },
  created() {
    this.isLoading = true;
    this.axios
      .get("https://"+ this.domain +"/events/", {
        auth: { username: "hasanprakash", password: "@hasanprakash" },
      })
      .then((response) => {
        console.log(response.data[0], response.data[1]);
        console.log(response.data[0].imageUrl);
        for (let i = 0; i < response.data.length; i++) {
          this.events.push(response.data[i]);
        }
        this.isLoading = false;
      })
      .catch((e) => {
        this.isError = true;
        this.isLoading = false;
        console.log(e);
      });
  },
};
</script>

<style scoped>
.container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 30px;
  grid-auto-rows: auto;
}
.card {
  box-shadow: 0 0 10px 1px rgb(150, 150, 150);
}
.card-grid {
  display: grid;
  grid-template-columns: 200px 10fr;
  grid-gap: 10px;
  align-items: center;
}
.card-grid div {
  padding: 20px;
}

.desc span,
.desc button {
  margin-bottom: 10px;
}
.heading {
  font-weight: bold;
  font-size: 20px;
}

@media only screen and (max-width: 600px) {
  .container {
    display: grid;
    grid-template-columns: 1fr;
    grid-gap: 30px;
    grid-auto-rows: auto;
  }
}
@media only screen and (max-width: 1000px) {
  .card-grid {
    display: grid;
    grid-template-columns: 1fr;
    grid-gap: 10px;
    align-items: center;
  }
}
</style>

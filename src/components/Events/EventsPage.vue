<template>
  <div class="container" style="text-align: center">
    <events-container :data="events"></events-container>
  </div>
</template>

<script>
import EventsContainer from './EventsContainer.vue';
export default {
  components: { EventsContainer },
  data() {
    return {
      events:[
        {
          heading: 'Y19 48-Hr Skill Development Project-3',
          description: 'description',
          imgUrl: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimage.flaticon.com%2Ficons%2Fpng%2F512%2F25%2F25231.png&f=1&nofb=1'
        }, {
          heading: '#Include',
          description: 'description', 
          imgUrl: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimage.flaticon.com%2Ficons%2Fpng%2F512%2F25%2F25231.png&f=1&nofb=1'
        }, {
          heading: 'Surabhi',
          description: 'description',
          imgUrl: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimage.flaticon.com%2Ficons%2Fpng%2F512%2F25%2F25231.png&f=1&nofb=1'
        }, {
          heading: 'Guruvedic 2020',
          description: 'description', 
          imgUrl: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimage.flaticon.com%2Ficons%2Fpng%2F512%2F25%2F25231.png&f=1&nofb=1'
        }, {
          heading: 'Pre-Conference Workshops',
          description: 'description', 
          imgUrl: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimage.flaticon.com%2Ficons%2Fpng%2F512%2F25%2F25231.png&f=1&nofb=1'
        }, {
          heading: '48-Hr Skill Development Project-1',
          description: 'description', 
          imgUrl: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimage.flaticon.com%2Ficons%2Fpng%2F512%2F25%2F25231.png&f=1&nofb=1'
        }
      ]
    }
  }
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

.desc span, .desc button {
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

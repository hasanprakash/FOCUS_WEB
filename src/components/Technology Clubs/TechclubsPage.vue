<template>
  <div class="main-container">
    <div class="container">
      <techclub-container :data="technologyClubs"></techclub-container>
    </div>
  </div>
</template>

<script>
import TechclubContainer from './TechclubContainer.vue';
export default {
  components: { TechclubContainer },
  data() {
    return {
      technologyClubs: [
        {
          technology: 'DS/ML',
          heading: 'KOGNITIV',
          description: 'Total description about this technology club',
          presidentName: 'Pavan Sai'
        }, 
        {
          technology: 'Unity',
          heading: 'MAYAVI',
          description: 'Total description about this technology club',
          presidentName: 'Some Person'
        }, 
        {
          technology: 'Cloud',
          heading: 'MEGA',
          description: 'Total description about this technology club',
          presidentName: 'Some Person'
        }, 
        {
          technology: 'AUTOMATION ANYWHERE',
          heading: 'RPA CLUB',
          description: 'Total description about this technology club',
          presidentName: 'Some Person'
        }
      ]
    }
  }
};
</script>

<style scoped>
.main-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0;
  background-color: #f7f8fc;
  font-family: "Roboto", sans-serif;
  color: #10182f;
}
.container {
  display: flex;
  width: 1040px;
  justify-content: space-evenly;
  flex-wrap: wrap;
}

</style>

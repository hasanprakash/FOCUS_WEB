<template>
  <div v-if="!isError" class="main-container">
    <div class="container">
      <techclub-container :data="technologyClubs"></techclub-container>
    </div>
  </div>
  <h2 v-else class="error">Failed To Fetch Data....</h2>
</template>

<script>
import TechclubContainer from './TechclubContainer.vue';
export default {
  inject: ['domain'],
  components: { TechclubContainer },
  data() {
    return {
      isError: false,
      technologyClubs: [
        // {
        //   technology: 'TOOL NAME',
        //   heading: 'KOGNITIV',
        //   description: 'Total description about this technology club',
        //   presidentName: 'Pavan Sai'
        // }, 
        // {
        //   technology: 'Unity/AR/VR',
        //   heading: 'MAYAVI',
        //   description: 'Total description about this technology club',
        //   presidentName: 'Some Person'
        // }, 
        // {
        //   technology: 'TOOL NAME',
        //   heading: 'MEGA',
        //   description: 'Total description about this technology club',
        //   presidentName: 'Some Person'
        // }, 
        // {
        //   technology: 'AUTOMATION ANYWHERE',
        //   heading: 'RPA CLUB',
        //   description: 'Total description about this technology club',
        //   presidentName: 'Some Person'
        // }
      ]
    }
  },
  created() {
    this.axios.get('https://'+ this.domain +'/techclubs', {auth:{username: 'hasanprakash', password: '@hasanprakash'}})
    .then((response) => {
      for(let i=0;i<response.data.length;i++) {
        this.technologyClubs.push(response.data[i]);
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

<template>
  <!-- Team Focus Start -->
  <div class="section-title">
    <h1>TEAM FOCUS</h1>
  </div>
  <div v-if="!isError">
  <team-container v-if="!isLoading" title="" :data="main"></team-container>
  <my-loader v-else title="" lheight="100px"></my-loader>

  <team-container v-if="!isLoading" title="DIRECTORS" :data="directors"></team-container>
  <my-loader v-else title="DIRECTORS"></my-loader>

  <team-container v-if="!isLoading" title="WEB MASTERS" :data="webmasters"></team-container>
  <my-loader v-else title="WEB MASTERS"></my-loader>

  <team-container v-if="!isLoading" title="LEADS" :data="leads"></team-container>
  <my-loader v-else title="LEADS"></my-loader>
  </div>
  <h2 v-else class="error">Failed To Fetch Data....</h2>
</template>

<script>
import TeamContainer from "./TeamContainer.vue";
export default {
  inject: ['domain'],
  data() {
    return {
      isLoading: false,
      isError: false,
      main: [
      ],
      directors: [
      ],
      webmasters: [
      ],
      leads: [
      ],
    };
  },
  components: {
    TeamContainer,
  },
  created() {
    this.isLoading = true;
    this.axios.get('https://'+ this.domain +'/focusteam', {auth:{username: 'hasanprakash', password: '@hasanprakash'}})
    .then((response) => {
      for(let i=0;i<response.data.length;i++) {
        if(response.data[i].groupName == "MAIN")
        this.main.push(response.data[i]);
        else if(response.data[i].groupName == "DIRECTORS")
        this.directors.push(response.data[i]);
        else if(response.data[i].groupName == "WEBMASTERS")
        this.webmasters.push(response.data[i]);
        else if(response.data[i].groupName == "LEADS")
        this.leads.push(response.data[i]);
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
/* MAIN HEADING */
.section-title {
  width: 100%;
  text-align: center;
  padding: 45px 0 30px 0;
}

/** MAIN TITLE */
.section-title::after {
  position: absolute;
  content: "";
  width: 50px;
  height: 5px;
  left: calc(50% - 25px);
  background: #353535;
}
.section-title h1 {
  color: #353535;
  font-size: 50px;
  letter-spacing: 5px;
  margin-bottom: 5px;
}


.dummy {
  width: 300px;
  height: 500px;
  background-color: #969696;
}
.center {
  display: flex;
  justify-content: space-evenly;
}
</style>

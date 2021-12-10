<template>
  <!-- Team Focus Start -->
  <div class="section-title">
    <h1>TEAM FOCUS</h1>
  </div>
  <div v-if="!isError">
  <team-container  title="" :data="main"></team-container>

  <team-container title="DIRECTORS" :data="directors"></team-container>

  <team-container title="WEB MASTERS" :data="webmasters"></team-container>

  <team-container title="LEADS" :data="leads"></team-container>
  </div>
  <h2 v-else class="error">Failed To Fetch Data....</h2>
</template>

<script>
import TeamContainer from "./TeamContainer.vue";
export default {
  data() {
    return {
      isError: false,
      main: [
        // {
        //   name: "Sai Kiran",
        //   role: "President",
        //   id: "180030000",
        // },
        // {
        //   name: "Prateek",
        //   role: "Treasurer",
        //   id: "180000000",
        // },
        // {
        //   name: "Jahnavi",
        //   role: "Secretary",
        //   id: "190000000",
        // },
      ],
      directors: [
        // {
        //   name: "Sai Kiran",
        //   role: "President",
        //   id: "180030000",
        // },
        // {
        //   name: "Prateek",
        //   role: "Treasurer",
        //   id: "180000000",
        // },
        // {
        //   name: "Jahnavi",
        //   role: "Secretary",
        //   id: "190000000",
        // },
        // {
        //   name: "Prateek",
        //   role: "Treasurer",
        //   id: "180000000",
        // },
      ],
      webmasters: [
        // {
        //   name: "Sai Kiran",
        //   role: "President",
        //   id: "180030000",
        // },
        // {
        //   name: "Prateek",
        //   role: "Treasurer",
        //   id: "180000000",
        // },
        // {
        //   name: "Jahnavi",
        //   role: "Secretary",
        //   id: "190000000",
        // },
        // {
        //   name: "Prateek",
        //   role: "Treasurer",
        //   id: "180000000",
        // },
        // {
        //   name: "Jahnavi",
        //   role: "Secretary",
        //   id: "190000000",
        // },
      ],
      leads: [
        // {
        //   name: "Sai Kiran",
        //   role: "President",
        //   id: "180030000",
        // },
        // {
        //   name: "Prateek",
        //   role: "Treasurer",
        //   id: "180000000",
        // },
        // {
        //   name: "Jahnavi",
        //   role: "Secretary",
        //   id: "190000000",
        // },
        // {
        //   name: "Sai Kiran",
        //   role: "President",
        //   id: "180030000",
        // },
        // {
        //   name: "Prateek",
        //   role: "Treasurer",
        //   id: "180000000",
        // },
        // {
        //   name: "Jahnavi",
        //   role: "Secretary",
        //   id: "190000000",
        // },
      ],
    };
  },
  components: {
    TeamContainer,
  },
  created() {
    this.axios.get('http://localhost:8000/focusteam', {auth:{username: 'hasanprakash', password: '@hasanprakash'}})
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
    })
    .catch(e => {
      console.log(e);
      this.isError = true;
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
</style>

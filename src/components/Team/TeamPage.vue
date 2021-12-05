<template>
  <!-- Team Focus Start -->
  <div class="section-title">
    <h1>TEAM FOCUS</h1>
  </div>

  <team-container title="" :data="main"></team-container>

  <team-container title="DIRECTORS" :data="directors"></team-container>

  <team-container title="WEB MASTERS" :data="webmasters"></team-container>

  <team-container title="LEADS" :data="leads"></team-container>
</template>

<script>
import TeamContainer from "./TeamContainer.vue";
export default {
  data() {
    return {
      main: [
        {
          name: "Sai Kiran",
          role: "President",
          id: "180030000",
        },
        {
          name: "Prateek",
          role: "Treasurer",
          id: "180000000",
        },
        {
          name: "Jahnavi",
          role: "Secretary",
          id: "190000000",
        },
      ],
      directors: [
        {
          name: "Sai Kiran",
          role: "President",
          id: "180030000",
        },
        {
          name: "Prateek",
          role: "Treasurer",
          id: "180000000",
        },
        {
          name: "Jahnavi",
          role: "Secretary",
          id: "190000000",
        },
        {
          name: "Prateek",
          role: "Treasurer",
          id: "180000000",
        },
      ],
      webmasters: [
        {
          name: "Sai Kiran",
          role: "President",
          id: "180030000",
        },
        {
          name: "Prateek",
          role: "Treasurer",
          id: "180000000",
        },
        {
          name: "Jahnavi",
          role: "Secretary",
          id: "190000000",
        },
        {
          name: "Prateek",
          role: "Treasurer",
          id: "180000000",
        },
        {
          name: "Jahnavi",
          role: "Secretary",
          id: "190000000",
        },
      ],
      leads: [
        {
          name: "Sai Kiran",
          role: "President",
          id: "180030000",
        },
        {
          name: "Prateek",
          role: "Treasurer",
          id: "180000000",
        },
        {
          name: "Jahnavi",
          role: "Secretary",
          id: "190000000",
        },
        {
          name: "Sai Kiran",
          role: "President",
          id: "180030000",
        },
        {
          name: "Prateek",
          role: "Treasurer",
          id: "180000000",
        },
        {
          name: "Jahnavi",
          role: "Secretary",
          id: "190000000",
        },
      ],
    };
  },
  components: {
    TeamContainer,
  },
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

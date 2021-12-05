<template>
  <div class="container">
    <div class="section-subtitle"><h3>{{ title }}</h3></div>
    <team-card v-for="i in data" :key="i.id">
      <template #name>{{ i.name }}</template>
      <template #role>{{ i.role }}</template>
      <template #id>{{ i.id }}</template>
    </team-card>
  </div>
</template>

<script>
import TeamCard from "../UI/TeamCard.vue";
export default {
  components: { TeamCard },
  props: ["data", "title"],
  data() {
    return {};
  },
};
</script>

<style scoped>
.container {
  display: flex;
  /* width: 1040px; */
  width: 100%;
  justify-content: space-evenly;
  flex-wrap: wrap;
}
.section-title,
.section-subtitle {
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

/** SUBTITLE */
.section-subtitle h3 {
  color: #353535;
  font-size: 35px;
  letter-spacing: 5px;
  margin-bottom: 5px;
}
.section-subtitle::after {
  position: absolute;
  content: "";
  width: 50px;
  height: 3px;
  left: calc(50% - 25px);
  background: #353535;
}

@media (max-width: 767.98px) {
  .section-title h1 {
    font-size: 40px;
    letter-spacing: 3px;
  }
}
@media (max-width: 767.98px) {
  .section-subtitle h3 {
    font-size: 40px;
    letter-spacing: 3px;
  }
}
</style>

<template>
<div class="section-subtitle"><h3>UPCOMING EVENTS</h3></div>
<div class="container">
  <uevents-card v-for="i of data" :key="i.title + (JSON.stringify(new Date()))"
    :url="i.url"
  >
    <template #title>{{ i.title }}</template>
    <template #subtitle>{{ i.subtitle }}</template>
  </uevents-card>
</div>
</template>

<script>
export default {
  props: ['data']
}
</script>

<style scoped>
.container {
  display: flex;
  width: 100%;
  justify-content: space-evenly;
  flex-wrap: wrap;
}

.section-subtitle {
  width: 100%;
  text-align: center;
  padding: 45px 0 30px 0;
}
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
  .section-subtitle h3 {
    font-size: 40px;
    letter-spacing: 3px;
  }
}
</style>
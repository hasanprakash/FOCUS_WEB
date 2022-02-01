<template>
  <div class="section-subtitle"><h3><slot></slot></h3></div>
</template>

<script>
export default {

}
</script>

<style scoped>
/* SUBTITLE */
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
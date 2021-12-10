<template>
  <my-header></my-header>
  <router-view></router-view><br>
  <my-footer></my-footer>
</template>

<script>
import MyFooter from './components/UI/MyFooter.vue'
export default {
  name: 'App',
  components: {
    MyFooter,
  }
}
</script>

<style>
.error {
  text-align: center;
  margin: 20px;
  color: red;
}
</style>

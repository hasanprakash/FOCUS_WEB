<template>
  <my-header></my-header>
  <router-view></router-view>
  <my-footer></my-footer>
</template>

<script>
import MyFooter from './components/UI/MyFooter.vue'
export default {
  name: 'App',
  components: {
    MyFooter
  }
}
</script>

<style>

</style>

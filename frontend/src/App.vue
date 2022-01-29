<template>
  <my-header></my-header>
  <router-view></router-view><br>
  <my-footer></my-footer>
</template>

<script>
export default {
  name: 'App',
  provide() {
    return {
      domain: 'focusfinalwebsite.azurewebsites.net'
    }
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

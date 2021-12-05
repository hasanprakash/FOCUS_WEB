<template>
  <techclub-card v-for="i in data" :key="i.heading">
      <template #technology>{{ i.technology }}</template>
      <template #heading>{{ i.heading }}</template>
      <template #description>{{ i.description }}</template>
      <template #presidentName>{{ i.presidentName }}</template>
  </techclub-card>
</template>

<script>
export default {
    props: ['data'],
    
}
</script>

<style>

</style>
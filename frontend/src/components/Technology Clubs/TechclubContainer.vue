<template>
  <techclub-card v-for="i in data" :key="i.name" :src="i.clubLogo">
      <template #technology>{{ i.technology }}</template>
      <template #heading>{{ i.name }}</template>
      <template #description>{{ i.description }}</template>
      <template #mainPerson>{{ i.mainPerson }}</template>
      <template #mainPersonRole>{{ i.theirRole }}</template>
  </techclub-card>
</template>

<script>
export default {
    props: ['data'],
    
}
</script>

<style>

</style>
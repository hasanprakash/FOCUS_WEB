<template>
  <event-card v-for="i in data" :key="i.name" :url="i.imgUrl">
      <template #heading>
          {{ i.heading }}
      </template>
      <template #description>
          {{ i.description }}
      </template>
  </event-card>
</template>

<script>
import EventCard from '../UI/EventCard.vue'
export default {
    props:['data'],
    components: {
        EventCard
    }
}
</script>
<style>

</style>
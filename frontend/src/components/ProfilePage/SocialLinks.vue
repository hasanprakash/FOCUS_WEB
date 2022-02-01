<template>
  <li
    class="list-group-item d-flex justify-content-between align-items-center p-3"
  >
    <a
      class="btn btn-primary btn-floating m-0"
      style="background-color: white; width: 25px; height: 25px"
      href="#!"
      role="button"
    >
      <img
        :src="imageUrl"
      />
    </a>
    <p class="mb-0"><slot></slot></p>
  </li>
</template>

<script>
export default {
  props: ['imageUrl'],
};
</script>

<style></style>

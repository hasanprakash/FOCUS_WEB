<template>
  <div class="form-group">
    <label for="example1"><slot name="fieldName"></slot></label>
    <input type="text" id="example1" class="form-control">
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
    input {
        width: 300px;
        margin-bottom: 20px;
    }
</style>
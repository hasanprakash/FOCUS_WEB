<template>
  <base-title>FOCUS LOGIN</base-title>
  <div class="center">
      <div>
        <my-input-field><template #fieldName>Enter ID</template></my-input-field>
        <my-input-field><template #fieldName>Enter Password</template></my-input-field>
        <div style="float: right;"><base-button>LOGIN</base-button></div>
      </div>
  </div>
</template>

<script>
import BaseButton from '../UI/BaseButton.vue'
export default {
  components: { BaseButton },

}
</script>

<style scoped>
    .center {
        display: flex;
        justify-content: center;
        width: 100%;
    }
</style>
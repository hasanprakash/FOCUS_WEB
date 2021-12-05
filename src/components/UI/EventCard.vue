<template>
  <div class="card">
    <div class="card-grid">
      <div>
        <img :src="url" />
      </div>
      <div class="desc">
        <span class="heading"><slot name="heading"></slot></span>
        <span class="description"><slot name="description"></slot></span>
        <div>
          <button type="button" class="btn btn-primary">
            Click here
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["url"],
};
</script>

<style scoped>
.card {
  box-shadow: 0 0 10px 1px rgb(150, 150, 150);
}
.card-grid {
  display: grid;
  grid-template-columns: 200px 10fr;
  grid-gap: 10px;
  align-items: center;
}
.card-grid div:nth-child(1) {
  padding: 20px;
}
/* 
.desc span,
.desc button {
  margin-bottom: 10px;
} */
.heading {
  font-weight: bold;
  font-size: 20px;
}
@media only screen and (max-width: 1000px) {
  .card-grid {
    display: grid;
    grid-template-columns: 1fr;
    grid-gap: 10px;
    align-items: center;
  }
}

.desc {
  height: 200px;
  display: grid;
  grid-template-rows: 22% 53% 25%;
  padding: 10px;
}
/* .desc span,
.desc button {
  border: 2px solid blue;
} */



.heading {
  white-space: nowrap;
  overflow-y: auto;
}
::-webkit-scrollbar {
  width: 1px;
  height: 2px;
  /* display: none; */
}
::-webkit-scrollbar-thumb {
  background: blue; 
  border-radius: 10px;
}

.description {
  overflow: auto;
}

.btn {
  padding: 10px;
  width: auto;
}
</style>

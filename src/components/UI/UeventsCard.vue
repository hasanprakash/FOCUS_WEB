<template>
  <div class="card-index" style="border-radius: 13px">
    <div class="card-body">
      <div>
        <img class="card-header" :src="url" alt="rover" />
      </div>

      <div class="body_post">
        <div><h1 class="title"><slot name="title"></slot></h1></div>
        <div><p class="subtitle">
          <slot name="subtitle"></slot>
        </p></div>
        <div class="r">
          <button type="button" class="button is-info">Read More</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["url"],
  data() {
    return {
      // url:'https://c0.wallpaperflare.com/preview/483/210/436/car-green-4x4-jeep.jpg',
      title: "#INCLUDE",
      subtitle:
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci animi assumenda cumque deserunt dolorum ex exercitationem.",
    };
  },
};
</script>

<style scoped>
.title {
  font-size: 25px;
}
.card-index {
  margin: 10px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  width: 300px;
}

.card-body {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  padding: 20px;
  min-height: 250px;
}

.card-body p {
  font-size: 13px;
  margin: 0 0 40px;
}

button {
  float: right;
}
.container {
  display: flex;
  width: 1040px;
  justify-content: space-evenly;
  flex-wrap: wrap;
}

.body_post {
  width: 100%;
  height: 200px;
  display: grid;
  grid-template-rows: 22% 55% 23%;
  padding: 15px;
}
/* .body_post div {
  border: 2px solid blue;
} */
.body_post div:nth-child(2) {
  overflow: auto;
}

::-webkit-scrollbar {
  width: 3px;
  height: 2px;
  /* display: none; */
}
::-webkit-scrollbar-thumb {
  background: blue; 
  border-radius: 10px;
}

button {
  transform: scale(0.80);
}
</style>

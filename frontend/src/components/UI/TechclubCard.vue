<template>
  <div class="card">
    <div class="card-header">
      <img
        :src="src"
        alt="rover"
      />
    </div>
    <div class="card-body">
      <span class="tag tag-teal"><slot name="technology"></slot></span>
      <h4 class="heading"><slot name="heading"></slot></h4>
      <span class="desc"><slot name="description"></slot></span>
      <div class="club-head">
        <img
          src="https://www.pngitem.com/pimgs/m/514-5149286_profile-logo-hd-png-download.png"
          alt="user"
        />
        <div class="user-info">
          <h5><slot name="mainPerson"></slot></h5>
          <span class="president-name"><slot name="mainPersonRole"></slot></span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['src']
};
</script>

<style scoped>
.card {
  margin: 10px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  width: 300px;
}
img {
  height: 300px;
}

.card-header {
  padding: 0;
}
.card-header img {
  width: 100%;
  /* height: 200px; */
  object-fit: cover;
}
.card-body {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  padding: 20px;
  min-height: 250px;
}

.tag {
  background: #cccccc;
  border-radius: 50px;
  font-size: 12px;
  margin: 0;
  color: #fff;
  padding: 2px 10px;
  text-transform: uppercase;
  cursor: pointer;
  margin-bottom: 10px;
}
.tag-teal {
  background-color: #47bcd4;
}
.tag-purple {
  background-color: #5e76bf;
}
.tag-pink {
  background-color: #cd5b9f;
}

.card-body p {
  font-size: 13px;
  margin: 0 0 40px;
}
.club-head {
  display: flex;
  margin-top: auto;
  align-items: center;
}

.club-head img {
  border-radius: 50%;
  width: 40px;
  height: 40px;
  margin-right: 10px;
}
.user-info h5 {
  margin: 0;
}
.heading {
  font-weight: bold;
  font-size: 20px;
}

.desc {
  font-size: 15px;
  height: 150px;
  overflow: auto;
}

.president-name {
  font-size: 13px;
}

.user-info {
  margin-top: 10px;
}
</style>

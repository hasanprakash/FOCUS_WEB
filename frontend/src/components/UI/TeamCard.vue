<template>
  <div class="team-6">
    <div class="team-img">
      <img
        :src="imageUrl"
        alt="Team Image"
      />
    </div>
    <div class="team-content">
      <h2><slot name="name"></slot></h2>
      <h3 style="font-size: xx-large"><slot name="role"></slot></h3>
      <h3 style="font-size: x-large"><slot name="id"></slot></h3>
      <div>
        <!-- Section: Social media -->
        <section>
          <!-- Facebook -->
          <a
            class="btn btn-primary btn-floating m-1"
            style="background-color: #3b5998"
            href="#!"
            role="button"
            >
            <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.freebiesupply.com%2Fimages%2Flarge%2F2x%2Ffacebook-logo-circle.png&f=1&nofb=1"/>
            </a>

          <!-- Twitter -->
          <a
            class="btn btn-primary btn-floating m-1"
            style="background-color: #55acee"
            href="#!"
            role="button"
            >
            <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.freeiconspng.com%2Fuploads%2Flogo-twitter-circle-png-transparent-image-1.png&f=1&nofb=1"/>
            </a>

          <!-- Instagram -->
          <a
            class="btn btn-primary btn-floating m-1"
            style="background-color: #dd2a7b"
            href="#!"
            role="button"
            >
            <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pinclipart.com%2Fpicdir%2Fbig%2F157-1577892_learn-more-instagram-logo-2018-transparent-background-clipart.png&f=1&nofb=1"/>
            </a>

          <!-- Linkedin -->
          <a
            class="btn btn-primary btn-floating m-1"
            style="background-color: white"
            href="#!"
            role="button"
            >
            <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.freebiesupply.com%2Flogos%2Flarge%2F2x%2Flinkedin-icon-logo-png-transparent.png&f=1&nofb=1"/>
            </a>
          <!-- Github -->
          <a
            class="btn btn-primary btn-floating m-1"
            style="background-color: white"
            href="#!"
            role="button"
            >
            <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimage.flaticon.com%2Ficons%2Fpng%2F512%2F25%2F25231.png&f=1&nofb=1"/>
            </a>
        </section>
        <!-- Section: Social media -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['imageUrl'],
  data() {
    return {

    }
  }
};
</script>

<style scoped>
.team-6 {
  margin-bottom: 30px;
  height: 500px;
  margin: 17px;
}

.team-6 .team-img {
  position: relative;
  font-size: 0;
  text-align: center;
  border-radius: 100%;
  margin-bottom: 30px;
  overflow: hidden;
}

.team-6 .team-img img {
  width: 250px;
  height: 240px;
  border-radius: 100%;
  border: 15px solid #f3f4fa;
  transition: all 0.3s;
}

.team-6:hover .team-img img {
  border: 0px solid #f3f4fa;
}

.team-6 .team-content {
  text-align: center;
}

.team-6 .team-content h2 {
  font-size: 25px;
  font-weight: 700;
  letter-spacing: 2px;
  margin-bottom: 15px;
}

.team-6 .team-content h3 {
  font-size: 16px;
  font-weight: 300;
  margin-bottom: 15px;
}

.team-6 .team-social {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0;
}

.team-6 .team-social a {
  display: inline-block;
  width: 40px;
  height: 40px;
  margin-right: 5px;
  padding: 12px 0 10px 0;
  font-size: 16px;
  line-height: 16px;
  text-align: center;
  color: #ffffff;
  border-radius: 100%;
  transition: all 0.3s;
}

.team-6 {
  border-radius: 15px;
  box-shadow: 0 0 10px 2px #ccc;
  padding: 20px;
  width: 300px;
}
</style>

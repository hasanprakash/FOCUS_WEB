<template>
  <!-- Navbar -->
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <!-- Container wrapper -->
    <div class="container">
      <div class="nav-items">
        <div>
          <!-- Toggle button -->
          <button
            class="navbar-toggler"
            type="button"
            data-mdb-toggle="collapse"
            data-mdb-target="#navbarButtonsExample"
            aria-controls="navbarButtonsExample"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <font-awesome-icon icon="bars" class="icons" />
          </button>
        </div>
        <div>
          <!-- Navbar brand -->
          <router-link class="navbar-brand me-2" to="/home">
            <img
              src="../../images/focus_black_png.png"
              height="16"
              width="70"
              alt=""
              loading="lazy"
              style="margin-top: -1px"
            />
          </router-link>
        </div>
      </div>

      <!-- Collapsible wrapper -->
      <div class="collapse navbar-collapse" id="navbarButtonsExample">
        <!-- Left links -->
        <ul class="navbar-nav me-auto mb-12 mb-lg-0"></ul>
        <!-- Left links -->
        <div class="d-flex align-items-center">
          <ul class="navbar-nav me-auto mb-12 mb-lg-0">
            <li class="nav-item">
              <router-link
                class="button is-info is-inverted px-3 me-2"
                to="/home"
                >HOME</router-link
              >
              <router-link
                class="button is-info is-inverted px-3 me-2"
                to="/events"
                >EVENTS</router-link
              >
              <router-link
                class="button is-info is-inverted px-3 me-2"
                to="/team"
                >TEAM</router-link
              >
              <router-link
                class="button is-info is-inverted px-3 me-2"
                to="/gallery"
                >GALLERY</router-link
              >
              <router-link
                class="button is-info is-inverted px-3 me-2"
                to="/techclubs"
                >TECHNOLOGY CLUBS</router-link
              >
              <!-- <router-link
                class="button is-info is-inverted px-3 me-2"
                to="/registration"
                >REGISTRATION</router-link
              > -->
            </li>
          </ul>
        </div>
      </div>
      <!-- Collapsible wrapper -->
    </div>
    <!-- Container wrapper -->
  </nav>
  <!-- Navbar -->
</template>

<script>
export default {};
</script>

<style>
.navbar {
  margin-bottom: 20px;
  /* padding: 0; */
  /**Removing this will increase the navbar height */
  height: auto;
}
.nav-items {
    display: flex;
}
.nav-items div {
    display: inline-block;
}
.nav-items div:nth-child(1) button {
    height: 100%;   
    font-size: 20px;
    margin-right: 10px;
}
.nav-items div:nth-child(2) {
    transform: scale(1.3);
}
li a {
  border-color: transparent;
}

@media only screen and (max-width: 1000px) {
  li a {
    display: block;
    width: 100%;
    white-space: normal;
    margin: 5px;
  }
  .align-items-center, ul  {
    width: 100%;
    align-items: center;
    justify-content: center;
  }
}

.nav-items div  {
  float: left;
}
</style>

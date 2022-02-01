<template>
  <section style="background-color: #eee">
    <div class="container py-5">
      <div class="row">
        <div class="col-lg-4">
          <div class="card mb-4">
            <div class="card-body text-center">
              <img
                src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3.webp"
                alt="avatar"
                class="rounded-circle img-fluid"
                style="width: 150px"
              />
              <h5 class="my-3">John Smith</h5>
              <p class="text-muted mb-1">Full Stack Developer</p>
              <p class="text-muted mb-4">Bay Area, San Francisco, CA</p>
              <div class="d-flex justify-content-center mb-2">
                <button type="button" class="btn btn-primary">Follow</button>
                <button type="button" class="btn btn-outline-primary ms-1">
                  Message
                </button>
              </div>
            </div>
          </div>
          <div class="card mb-4 mb-lg-0">
            <div class="card-body p-0">
              <ul class="list-group list-group-flush rounded-3">
                <social-links :imageUrl="socialMediaLogo.github">GITHUB USERNAME</social-links>
                <social-links :imageUrl="socialMediaLogo.instagram">INSTAGRAM USERNAME</social-links>
                <social-links :imageUrl="socialMediaLogo.facebook">FACEBOOK USERNAME</social-links>
                <social-links :imageUrl="socialMediaLogo.twitter">TWITTER USERNAME</social-links>
                <social-links :imageUrl="socialMediaLogo.linkedin">LINKEDIN USERNAME</social-links>
              </ul>
            </div>
          </div>
        </div>
        <div class="col-lg-8">
          <div class="card mb-4">
            <div class="card-body">
              <div class="row">
                <div class="col-sm-3">
                  <p class="mb-0">Full Name</p>
                </div>
                <div class="col-sm-9">
                  <p class="text-muted mb-0">Johnatan Smith</p>
                </div>
              </div>
              <hr />
              <div class="row">
                <div class="col-sm-3">
                  <p class="mb-0">Email</p>
                </div>
                <div class="col-sm-9">
                  <p class="text-muted mb-0">example@example.com</p>
                </div>
              </div>
              <hr />
              <div class="row">
                <div class="col-sm-3">
                  <p class="mb-0">Phone</p>
                </div>
                <div class="col-sm-9">
                  <p class="text-muted mb-0">(097) 234-5678</p>
                </div>
              </div>
              <hr />
              <div class="row">
                <div class="col-sm-3">
                  <p class="mb-0">Mobile</p>
                </div>
                <div class="col-sm-9">
                  <p class="text-muted mb-0">(098) 765-4321</p>
                </div>
              </div>
              <hr />
              <div class="row">
                <div class="col-sm-3">
                  <p class="mb-0">Address</p>
                </div>
                <div class="col-sm-9">
                  <p class="text-muted mb-0">Bay Area, San Francisco, CA</p>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="card mb-4 mb-md-0">
                <div class="card-body">
                  <p class="mb-4">
                    <span class="text-primary font-italic me-1">assigment</span>
                    Project Status
                  </p>
                  <p class="mb-1" style="font-size: 0.77rem">Web Design</p>
                  <div class="progress rounded" style="height: 5px">
                    <div
                      class="progress-bar"
                      role="progressbar"
                      style="width: 80%"
                      aria-valuenow="80"
                      aria-valuemin="0"
                      aria-valuemax="100"
                    ></div>
                  </div>
                  <p class="mt-4 mb-1" style="font-size: 0.77rem">
                    Website Markup
                  </p>
                  <div class="progress rounded" style="height: 5px">
                    <div
                      class="progress-bar"
                      role="progressbar"
                      style="width: 72%"
                      aria-valuenow="72"
                      aria-valuemin="0"
                      aria-valuemax="100"
                    ></div>
                  </div>
                  <p class="mt-4 mb-1" style="font-size: 0.77rem">One Page</p>
                  <div class="progress rounded" style="height: 5px">
                    <div
                      class="progress-bar"
                      role="progressbar"
                      style="width: 89%"
                      aria-valuenow="89"
                      aria-valuemin="0"
                      aria-valuemax="100"
                    ></div>
                  </div>
                  <p class="mt-4 mb-1" style="font-size: 0.77rem">
                    Mobile Template
                  </p>
                  <div class="progress rounded" style="height: 5px">
                    <div
                      class="progress-bar"
                      role="progressbar"
                      style="width: 55%"
                      aria-valuenow="55"
                      aria-valuemin="0"
                      aria-valuemax="100"
                    ></div>
                  </div>
                  <p class="mt-4 mb-1" style="font-size: 0.77rem">
                    Backend API
                  </p>
                  <div class="progress rounded mb-2" style="height: 5px">
                    <div
                      class="progress-bar"
                      role="progressbar"
                      style="width: 66%"
                      aria-valuenow="66"
                      aria-valuemin="0"
                      aria-valuemax="100"
                    ></div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="card mb-4 mb-md-0">
                <div class="card-body">
                  <p class="mb-4">
                    <span class="text-primary font-italic me-1">assigment</span>
                    Project Status
                  </p>
                  <p class="mb-1" style="font-size: 0.77rem">Web Design</p>
                  <div class="progress rounded" style="height: 5px">
                    <div
                      class="progress-bar"
                      role="progressbar"
                      style="width: 80%"
                      aria-valuenow="80"
                      aria-valuemin="0"
                      aria-valuemax="100"
                    ></div>
                  </div>
                  <p class="mt-4 mb-1" style="font-size: 0.77rem">
                    Website Markup
                  </p>
                  <div class="progress rounded" style="height: 5px">
                    <div
                      class="progress-bar"
                      role="progressbar"
                      style="width: 72%"
                      aria-valuenow="72"
                      aria-valuemin="0"
                      aria-valuemax="100"
                    ></div>
                  </div>
                  <p class="mt-4 mb-1" style="font-size: 0.77rem">One Page</p>
                  <div class="progress rounded" style="height: 5px">
                    <div
                      class="progress-bar"
                      role="progressbar"
                      style="width: 89%"
                      aria-valuenow="89"
                      aria-valuemin="0"
                      aria-valuemax="100"
                    ></div>
                  </div>
                  <p class="mt-4 mb-1" style="font-size: 0.77rem">
                    Mobile Template
                  </p>
                  <div class="progress rounded" style="height: 5px">
                    <div
                      class="progress-bar"
                      role="progressbar"
                      style="width: 55%"
                      aria-valuenow="55"
                      aria-valuemin="0"
                      aria-valuemax="100"
                    ></div>
                  </div>
                  <p class="mt-4 mb-1" style="font-size: 0.77rem">
                    Backend API
                  </p>
                  <div class="progress rounded mb-2" style="height: 5px">
                    <div
                      class="progress-bar"
                      role="progressbar"
                      style="width: 66%"
                      aria-valuenow="66"
                      aria-valuemin="0"
                      aria-valuemax="100"
                    ></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import SocialLinks from './SocialLinks.vue';
export default {
  components: { SocialLinks },
  data() {
    return {
      socialMediaLogo: {
        github: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimage.flaticon.com%2Ficons%2Fpng%2F512%2F25%2F25231.png&f=1&nofb=1',
        instagram: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pinclipart.com%2Fpicdir%2Fbig%2F157-1577892_learn-more-instagram-logo-2018-transparent-background-clipart.png&f=1&nofb=1',
        facebook: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.freebiesupply.com%2Fimages%2Flarge%2F2x%2Ffacebook-logo-circle.png&f=1&nofb=1',
        twitter: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.freeiconspng.com%2Fuploads%2Flogo-twitter-circle-png-transparent-image-1.png&f=1&nofb=1',
        linkedin: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.freebiesupply.com%2Flogos%2Flarge%2F2x%2Flinkedin-icon-logo-png-transparent.png&f=1&nofb=1',
      }
    }
  }
};
</script>

<style></style>

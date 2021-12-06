import { createApp } from "vue";
import App from "./App.vue";
import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faBars,
  faChevronLeft,
  faChevronRight,
  faTimes,
} from "@fortawesome/free-solid-svg-icons";
// import {

// } from '@fortawesome/free-solid-'
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { createRouter, createWebHistory } from "vue-router";

import MyHeader from "./components/UI/MyHeader.vue";
import UeventsCard from "./components/UI/UeventsCard.vue";
import TeamCard from "./components/UI/TeamCard.vue";
import EventCard from "./components/UI/EventCard.vue";
import TechclubCard from "./components/UI/TechclubCard.vue";
import ShowImage from "./components/Gallery/ShowImage.vue";
import HomePage from "./components/Home/HomePage.vue";
import EventsPage from "./components/Events/EventsPage.vue";
import TeamPage from "./components/Team/TeamPage.vue";
import GalleryPage from "./components/Gallery/GalleryPage.vue";
import TechclubsPage from "./components/Technology Clubs/TechclubsPage.vue";
import RegistrationPage from "./components/Registration/RegistrationPage.vue";

// creating routes
const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", redirect: "/home" },
    { path: "/home", component: HomePage, alias: '/' },
    { path: "/events", component: EventsPage },
    { path: "/team", component: TeamPage },
    {
      path: "/gallery",
      component: GalleryPage,
      children: [
        {
          path: ":imageId",
          component: ShowImage,
          props: true
        },
      ],
    },
    { path: "/techclubs", component: TechclubsPage },
    { path: "/registration", component: RegistrationPage },
  ],
});

library.add(faChevronLeft, faChevronRight, faTimes, faBars);

const app = createApp(App);

app.component("my-header", MyHeader);
app.component("uevents-card", UeventsCard);
app.component("team-card", TeamCard);
app.component("event-card", EventCard);
app.component("font-awesome-icon", FontAwesomeIcon);
app.component("techclub-card", TechclubCard);
app.config.productionTip = false;

app.use(router);

app.mount("#app");

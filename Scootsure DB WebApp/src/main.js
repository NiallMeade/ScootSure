
import Vue from "vue";
import App from "./App";
import router from "./router/index";

import PaperDashboard from "./plugins/paperDashboard";
import "vue-notifyjs/themes/default.css";
import "babel-plugin-syntax-dynamic-import";
import "babel";
import "babel-cli";
import "@vue/cli-plugin-babel"
import "core-js/modules/es.promise";
import "core-js/modules/es.array.iterator";


Vue.use(PaperDashboard);import "core-js/modules/es.promise";
import "core-js/modules/es.array.iterator";


/* eslint-disable no-new */
new Vue({
  router,
  render: h => h(App)
}).$mount("#app");

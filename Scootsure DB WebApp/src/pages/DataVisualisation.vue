<template>
    <div>
        <div class="row">

            <div class="col-md-6 col-xl-3">

                <stats-card>
                    <div class="icon-big text-center" slot="header">
                        <i class="ti-user text-info"></i>
                    </div>
                    <div class="numbers" slot="content">
                        <p>Username</p>
                        {{userData.user}}
                    </div>
                </stats-card>

            </div>

            <div class="col-md-6 col-xl-3">

                <stats-card>
                    <div class="icon-big text-center" slot="header">
                        <i class="ti-info-alt text-danger"></i>
                    </div>
                    <div class="numbers" slot="content">
                        <p>Age</p>
                        {{userData.age}}
                    </div>
                </stats-card>

            </div>

            <div class="col-md-6 col-xl-3">

                <stats-card>
                    <div class="icon-big text-center" slot="header">
                        <i class="ti-target text-danger"></i>
                    </div>
                    <div class="numbers" slot="content">
                        <p>Average Speed</p>
                        {{userData.averageSpeed}}km/h
                    </div>
                </stats-card>

            </div>

            <div class="col-md-6 col-xl-3">

                <stats-card>
                    <div class="icon-big text-center" slot="header">
                        <i class="ti-map-alt text-error"></i>
                    </div>
                    <div class="numbers" slot="content">
                        <p>Average Distance</p>
                        {{userData.averageDistance}}km
                    </div>
                </stats-card>

            </div>

            <div class="col-md-6 col-xl-3">

                <stats-card>
                    <div class="icon-big text-center" slot="header">
                        <i class="ti-map text-info"></i>
                    </div>
                    <div class="numbers" slot="content">
                        <p>Total Journeys</p>
                        {{userData.totalJourneys}}
                    </div>
                </stats-card>

            </div>

            <div class="col-md-6 col-xl-3">

                <stats-card>
                    <div class="icon-big text-center" slot="header">
                        <i class="ti-money text-success"></i>
                    </div>
                    <div class="numbers" slot="content">
                        <p>Premium</p>
                        {{userData.premium}}
                    </div>
                </stats-card>

            </div>

        </div>

      <div>
        <mdb-tbl>
          <mdb-tbl-head>
            <tr>
              <th>User</th>
              <th>Average Speed</th>
              <th>Distance</th>
              <th>Time Taken</th>
              <th>Start Time</th>
              <th>Finish Time</th>
            </tr>
          </mdb-tbl-head>
          <mdb-tbl-body>
            <tr v-for="journey in journeys" :key="journey">
                <th>{{journey.user}}</th>
                <td>{{journey.averageSpeed}}km/h</td>
                <td>{{journey.distance}}km</td>
                <td>{{journey.timeTaken}} minutes</td>
                <td>{{journey.start}}</td>
                <td>{{journey.finish}}</td>
            </tr>
          </mdb-tbl-body>
        </mdb-tbl>
      </div>
          <iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~niall_scootsure/1.embed" height="525" width="100%"></iframe>

    </div>
</template>
<script>
import EditProfileForm from "./UserProfile/EditProfileForm.vue";
import UserCard from "./UserProfile/UserCard.vue";
import MembersCard from "./UserProfile/MembersCard.vue";
import "firebase/app";
import db from "@/components/firebaseinit.js";
import 'firebase/firestore';
import { StatsCard, ChartCard } from "@/components/index";
import { mdbTbl, mdbTblHead, mdbTblBody } from 'mdbvue';
import { PaperTable } from "@/components";

export default {

  components: {
    StatsCard,
    ChartCard,
    PaperTable,
    mdbTbl,
    mdbTblHead,
    mdbTblBody
  },

  created(){
      console.log(localStorage.user)

          db.collection("users").where("user", "==", localStorage.user).get().then((querySnapshot) => {
        querySnapshot.forEach((doc) => {
            this.userData = doc.data();
            console.log(doc.id, " => ", doc.data());
            console.log(this.userData.user);
        });
    });

          db.collection("journeys").where("user", "==", localStorage.user).get().then((querySnapshot) => {
        querySnapshot.forEach((doc) => {
            this.journeys.push(doc.data());
            console.log(doc.id, " => ", doc.data());
            console.log(this.journeys);
        });
    });

  },

    data() {

    return {

      userData: [],
      journeys: []

    };
  }

};
</script>
<style>
</style>

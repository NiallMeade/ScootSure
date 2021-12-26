<template>
  <div>

    <!--Stats cards-->
    <!-- <div class="row">
      <div class="col-md-6 col-xl-3" v-for="stats in statsCards" :key="stats.title">
        <stats-card>
          <div class="icon-big text-center" :class="`icon-${stats.type}`" slot="header">
            <i :class="stats.icon"></i>
          </div>
          <div class="numbers" slot="content">
            <p>{{stats.title}}</p>
            {{stats.value}} 
         </div>
          <div class="stats" slot="footer">
            <i :class="stats.footerIcon"></i> {{stats.footerText}}
          </div>
        </stats-card>
      </div>
    </div> -->


  <div class="row">
    <div class="col-md-6 col-xl-3">

      <stats-card>
        <div class="icon-big text-center" slot="header">
          <i class="ti-user text-info"></i>
        </div>
        <div class="numbers" slot="content">
          <p>Users</p>
          {{localtotalUsers}}
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
          {{localaverageSpeed}} km/h
        </div>
      </stats-card>

    </div>

    <div class="col-md-6 col-xl-3">

      <stats-card>
        <div class="icon-big text-center" slot="header">
          <i class="ti-money text-success"></i>
        </div>
        <div class="numbers" slot="content">
          <p>Average Premium</p>
          €{{localaveragePremium}}
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
          {{localaverageDistance}} km
        </div>
      </stats-card>

    </div>
  </div>


    


    <!--Charts-->
    <div class="row">

      <div class="col-12">
        <chart-card title="Journeys"
                    sub-title="24 Hours performance"
                    :chart-data="usersChart.data"
                    :chart-options="usersChart.options">
          <!-- <span slot="footer">
            <i class="ti-reload"></i> Updated 3 minutes ago
          </span> -->
          <div slot="legend">
            <i class="fa fa-circle text-info"></i> low Risk Customer
            <i class="fa fa-circle text-warning"></i> Medium Risk Customer
            <i class="fa fa-circle text-danger"></i> High Risk Customer
          </div>
        </chart-card>
      </div>

      <!-- <div class="col-md-6 col-12">
        <chart-card title="Email Statistics"
                    sub-title="Last campaign performance"
                    :chart-data="preferencesChart.data"
                    chart-type="Pie">
          <span slot="footer">
            <i class="ti-timer"></i> Campaign set 2 days ago</span>
          <div slot="legend">
            <i class="fa fa-circle text-info"></i> Open
            <i class="fa fa-circle text-danger"></i> Bounce
            <i class="fa fa-circle text-warning"></i> Unsubscribe
          </div>
        </chart-card>
      </div>

      <div class="col-md-6 col-12">
        <chart-card title="2015 Sales"
                    sub-title="All products including Taxes"
                    :chart-data="activityChart.data"
                    :chart-options="activityChart.options">
          <span slot="footer">
            <i class="ti-check"></i> Data information certified
          </span>
          <div slot="legend">
            <i class="fa fa-circle text-info"></i> Tesla Model S
            <i class="fa fa-circle text-warning"></i> BMW 5 Series
          </div>
        </chart-card>
      </div> -->

    </div>

  </div>
</template>
<script>
import { StatsCard, ChartCard } from "@/components/index";
import Chartist from 'chartist';
import "firebase/app";
import db from "@/components/firebaseinit.js";

import 'firebase/firestore';

export default {
  components: {
    StatsCard,
    ChartCard
  },

  /**
   * Chart data used to render stats, charts. Should be replaced with server data
   */

   created(){
    db.collection("users").where("master", "==", true).get().then((querySnapshot) => {
        querySnapshot.forEach((doc) => {
            console.log(doc.id, " => ", doc.data());
            this.statsData = doc.data();
            this.localtotalUsers = this.statsData.totalUsers;
            this.localaveragePremium = this.statsData.averagePremium;
            this.localaverageDistance = this.statsData.averageDistance;         
            this.localaverageSpeed = this.statsData.averageSpeed;     
            console.log("data collected");
        });
    });


  // db.collection("journeys").where("master", "==", false).get().then((querySnapshot) => {
  //       querySnapshot.forEach((doc) => {
  //           journeysToday++;
  //           console.log("number of journeys" + journeysToday)
  //           // doc.data() is never undefined for query doc snapshots
  //           console.log(doc.id, " => ", doc.data());
  //           console.log("done");
  //       });
  //   });
  
   },

  data() {


    return {


      journeysToday: Number,
      dateToday: Number,

      secondSeries: [],
      statsData: [],

      localtotalUsers: "",
      localaveragePremium: "",
      localaverageDistance: "",
      localaverageSpeed: "",
      

      statsCards: [
        
        {
          type: "info",
          icon: "ti-user",
          title: "Users",
          //value: "498",
          value: this.localtotalUsers,
          footerText: "Updated now",
          footerIcon: "ti-reload"
        },
        {
          type: "success",
          icon: "ti-money",
          title: "Average Premium",
          //value: "€289",
          value: this.localaveragePremium,
          footerText: "Updated an hour ago",
          footerIcon: "ti-timer"
        },
        {
          type: "danger",
          icon: "ti-target",
          title: "Average Speed",
          //value: "12km/h",
          value: this.localaverageSpeed,
          footerText: "Updated now",
          footerIcon: "ti-reload"
        },
        {
          type: "error",
          icon: "ti-map-alt",
          title: "Average Distance",
          //value: "312",
          value: this.localaverageDistance,
          footerText: "Updated now",
          footerIcon: "ti-reload"
        }
      ],
      usersChart: {
        data: {
          labels: [
            "00:00PM",
            "03:00AM",
            "06:00AM",
            "09:00AM",
            "12:00AM",
            "3:00PM",
            "6:00PM",
            "9:00PM",
            "00:00PM"
          ],
          series: [
            [15, 8, 25, 80, 35, 48, 112 , 45, 17],
            [12, 7, 18, 45, 25, 42, 65 , 32, 12],
            [23, 11, 8, 14, 15, 20, 38 , 52, 25]
          ]
        },
        options: {
          low: 0,
          high: 115,
          showArea: true,
          height: "245px",
          axisX: {
            showGrid: false
          },
          lineSmooth: Chartist.Interpolation.simple({
            divisor: 2.5
          }),
          showLine: true,
          showPoint: false
        }
      },
      activityChart: {
        data: {
          labels: [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "Mai",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec"
          ],
          series: [
            [542, 543, 520, 680, 653, 753, 326, 434, 568, 610, 756, 895],
            [230, 293, 380, 480, 503, 553, 600, 664, 698, 710, 736, 795]
          ]
        },
        options: {
          seriesBarDistance: 10,
          axisX: {
            showGrid: false
          },
          height: "245px"
        }
      },
      preferencesChart: {
        data: {
          labels: ["62%", "32%", "6%"],
          series: [62, 32, 6]
        },
        options: {}
      },

    };
  }

  // firestore () {
  //   return {
  //     secondSeries: db.collection("users").orderBy('createdAt')
  //   }
  //   console.log("RIGHT HERE",secondSeries)
  // },

  // created(){
  //   db.collection("users").get().then
  //   (
  //     querySnapshot => {
  //       querySnapshot.forEach
  //       (doc => {
  //         console.log("hello", doc.id);
  //         const data = {
  //           "id" : doc.id,
  //           "example" : doc.data().example,
  //           "random" : doc.data().random,
  //           "averageDistance" : doc.data().averageDistance,
  //           "averagePremium" : doc.data().averagePremium,
  //           "averageSpeed" : doc.data().averageSpeed,
  //           "totalUsers" : doc.data().totalUsers
  //         }
  //         this.secondSeries.push(data);
  //         console.log(secondSeries.totalUsers)
  //       })
  //     })
  // }

  //   created(){
  //   db.collection("users").get().then
  //   (
  //     querySnapshot => {
  //       querySnapshot.forEach
  //       (doc => {
  //         console.log("hello", doc.id);
  //         const data = {
  //           "id" : doc.id,
  //           "example" : doc.data().example,
  //           "random" : doc.data().random,
  //           "averageDistance" : doc.data().averageDistance,
  //           "averagePremium" : doc.data().averagePremium,
  //           "averageSpeed" : doc.data().averageSpeed,
  //           "totalUsers" : doc.data().totalUsers
  //         }
  //         this.secondSeries.push(data);
  //       })
  //     })
  // }



};
</script>
<style>
</style>

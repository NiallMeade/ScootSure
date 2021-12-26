<template>
    <div>

      <!-- <div class="col-12">
        <card :title="table.title" :subTitle="table.subTitle">
          <div slot="raw-content" class="table-responsive">
            <paper-table :data="users" :columns="table.columns" :v-on:click="getAllUserData()" @click.native="getAllUserData(data)">

            </paper-table>
          </div>
        </card>
      </div> -->

      <div>
        <mdb-tbl>
          <mdb-tbl-head>
            <tr>
              <th>User</th>
              <th>Premium</th>
              <th>Average Speed</th>
              <th>Average Distance</th>
              <th>Total Journeys</th>
              <th>Age</th>
            </tr>
          </mdb-tbl-head>
          <mdb-tbl-body>
            <tr v-for="user in users" :key="user" v-on:click="getAllUserData(user)">
              <th>{{user.user}}</th>
              <td>{{user.premium}}</td>
              <td>{{user.averageSpeed}}km/h</td>
              <td>{{user.averageDistance}}km</td>
              <td>{{user.totalJourneys}}</td>
              <td>{{user.age}}</td>
            </tr>
          </mdb-tbl-body>
        </mdb-tbl>
      </div>

    </div>
</template>
<script>
import { PaperTable } from "@/components";
import "firebase/app";
import db from "@/components/firebaseinit.js";
import 'firebase/firestore';
import { mdbTbl, mdbTblHead, mdbTblBody } from 'mdbvue';
import { json } from 'body-parser';

const tableColumns = ["User", "Premium", "Average "+"Speed", "Average "+"Distance", "Total "+"Journeys", "Age"];

export default {

  methods: {
    // allData: function (event) {

    //   console.log("success", this.newTableData.user)

    //   // // `this` inside methods points to the Vue instance
    //   // alert("click success")
    //   // // `event` is the native DOM event
    //   // if (event) {
    //   //   console.log("success")
    //   //   alert(event.target.tagName)
    //   // }
    // }

    getAllUserData(user){
      console.log("success" + user.user)
      localStorage.setItem("user" ,user.user)
      this.$router.push("data-visualisation")
    }
  },

  components: {
    PaperTable,
    mdbTbl,
    mdbTblHead,
    mdbTblBody
  },

   created(){
    db.collection("users").where("master", "==", false).get().then((querySnapshot) => {
        querySnapshot.forEach((doc) => {
            this.users.push(doc.data());
            // doc.data() is never undefined for query doc snapshots
            console.log(doc.id, " => ", doc.data());
            console.log(this.users);
        });
    });
  },

  data() {

    return {

      users: [],

      table: {
        title: "Stripped Table",
        subTitle: "Here is a subtitle for this table",
        columns: [...tableColumns]
      }
    };
  }
};
</script>
<style>
</style>

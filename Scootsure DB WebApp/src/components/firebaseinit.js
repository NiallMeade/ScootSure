import "firebase/firestore";
import firebaseConfig from "./firebaseConfig";
import firebase from 'firebase/app';
import 'firebase/auth';
const firebaseApp = firebase.initializeApp(firebaseConfig);
export default firebaseApp.firestore();
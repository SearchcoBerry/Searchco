import firebase from "firebase/app"
import "firebase/firestore";

if (!firebase.apps.length) {
    firebase.initializeApp({
        apiKey: "AIzaSyAMEW5wD-NBdmlu86ZTIUOvUfdNW_1cOF8",
        authDomain: "searchco-okiu.firebaseapp.com",
        projectId: "searchco-okiu",
        storageBucket: "searchco-okiu.appspot.com",
        messagingSenderId: "694889958300",
        appId: "1:694889958300:web:33a24e5d168e8309971659"
    })
}

export default firebase
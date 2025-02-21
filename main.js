var firebaseConfig = {
    apiKey: "AIzaSyCjGDrya5-MyZ0xNagscj-SNcV-5rpkpxM",
    authDomain: "remainders-43b61.firebaseapp.com",
    projectId: "remainders-43b61",
    storageBucket: "remainders-43b61.firebasestorage.app",
    messagingSenderId: "652379233415",
    appId: "1:652379233415:web:34532b038fc53c7abd6c22",
    measurementId: "G-YVQPEMGRWD"
    
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Firestore reference
var db = firebase.firestore();

function addReminder() {
    var reminder = document.getElementById('reminder').value;
    var reminderTime = document.getElementById('reminderTime').value;
    if (reminder && reminderTime) {
        db.collection("reminders").add({
            text: reminder,
            time: reminderTime
        }).then(() => {
            document.getElementById('reminder').value = '';
            document.getElementById('reminderTime').value = '';
            fetchReminders();
        }).catch((error) => {
            console.error("Error adding reminder: ", error);
        });
    }
}

function fetchReminders() {
    var reminderList = document.getElementById('reminderList');
    reminderList.innerHTML = '';
    db.collection("reminders").get().then((querySnapshot) => {
        querySnapshot.forEach((doc) => {
            var listItem = document.createElement('li');
            listItem.textContent = ${doc.data().text} - ${new Date(doc.data().time).toLocaleString()};
            reminderList.appendChild(listItem);
        });
    }).catch((error) => {
        console.error("Error fetching reminders: ", error);
    });
}

function checkReminders() {
    var currentTime = new Date().toISOString().slice(0, 16); // Get current time in YYYY-MM-DDTHH:MM format
    console.log("Current time: " + currentTime);

    db.collection("reminders").where("time", "<=", currentTime).get().then((querySnapshot) => {
        console.log("Checking reminders...");
        
        if (querySnapshot.empty) {
            console.log("No reminders to show.");
        } else {
            querySnapshot.forEach((doc) => {
                console.log("Reminder found: " + doc.data().text);
                alert(Reminder: ${doc.data().text});
                db.collection("reminders").doc(doc.id).delete(); // Optional: Delete the reminder after alerting
            });
        }
    }).catch((error) => {
        console.error("Error checking reminders: ", error);
    });
}


// Fetch reminders on page load
window.onload = function() {
    fetchReminders();
     setInterval(checkReminders, 60000); // Check reminders every minute
};
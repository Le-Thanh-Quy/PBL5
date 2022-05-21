import pyrebase
from datetime import datetime

config = {
    "apiKey": "AIzaSyCyArj4NRLaeQqVzgZZ07BGKyc90xpN6z0",
    "authDomain": "test-3107.firebaseapp.com",
    "databaseURL": "https://test-3107-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "test-3107",
    "storageBucket": "test-3107.appspot.com",
    "messagingSenderId": "63571418677",
    "appId": "1:63571418677:web:6f2b978844fd49edbd5b7c"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# data = {"age" : 21,  "time": datetime.now().strftime("%Y_%m_%d_%H_%M")}

data = {
  "first_customer": {
    "createdat": "2019-08-09T06:40:10+0000",
    "expires": 1572039000.0,
  },
  "second_customer": {
    "createdat": "2019-08-09T06:33:39+0000",
    "expires": 1570048200.0,
  }
}

db.child('user').push(data)

storage = firebase.storage()
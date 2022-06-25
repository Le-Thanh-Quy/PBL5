from time import sleep
import pyrebase
import threading

trangthai = 1

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

# data = {"TrangThai": 0}
# db.child("TrangThai").set(data)

def KiemTraVaNamTrangThai():
  while True:
    sleep(0.5)
    dt = db.child('TrangThai').get()
    tt = dt[0].val()
    print(tt)
    if tt < 5:
      tt += 1
    else:
      tt = 0
      
    data = {"TrangThai": tt}
    db.child("TrangThai").update(data)
  
# thr1 = threading.Thread(target=KiemTraVaNamTrangThai, args=())
# thr1.start()

def KiemTraTrangThai():
  while True:
    sleep(0.5)
    dt = db.child('TrangThai').get()
    global trangthai
    trangthai = dt[0].val()

def ChayTrangThai():
  thr1 = threading.Thread(target=KiemTraTrangThai, args=())
  thr1.start()

def GetTrangThai():
  return trangthai

def ChangeTrangThai(tt):
    data = {"TrangThai": tt}
    db.child("TrangThai").update(data)
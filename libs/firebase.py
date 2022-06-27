# import pyrebase

# config = {
#   "apiKey": "AIzaSyBlXTyFl3_jLC3j6dY-4uuATy6O0G4F79A",
#   "authDomain": "pi3b-162b7.firebaseapp.com",
#   "projectId": "pi3b-162b7",
#   "storageBucket": "pi3b-162b7.appspot.com",
#   "messagingSenderId": "701866663570",
#   "appId": "1:701866663570:web:70373fc27eab158b27904b",
#   "measurementId": "G-K5Z4ZWVYV9",
#   "databaseURL": ""
# };

# firebase_storage = pyrebase.initialize_app(config)
# storage = firebase_storage.storage()


# storage.child("Test").child("quy.JPG").put("C:\\Users\\ADMIN\\Desktop\\face.jpg")


import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'pi3b-162b7.appspot.com'
})

bucket = storage.bucket()
bucket.blob("Test/quy1.JPG").upload_from_filename("C:\\Users\\ADMIN\\Desktop\\face.jpg")

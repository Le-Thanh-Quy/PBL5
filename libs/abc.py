import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pi3b-162b7-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
ref = db.reference('/')
ref.child("Quy").set("ABC")

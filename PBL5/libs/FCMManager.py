import firebase_admin
from firebase_admin import db 
from firebase_admin import credentials, messaging

cred = credentials.Certificate('C:\\Users\\ADMIN\\Desktop\\DoAN\\Code\\PBL5\\serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pi3b-162b7-default-rtdb.asia-southeast1.firebasedatabase.app/',
    'storageBucket': 'pi3b-162b7.appspot.com'
})

def sendPush(title, msg, phone_number, dataObject=None):
    # See documentation on defining a message payload.
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=msg,
        ),
        data=dataObject,
        tokens=[db.reference("/Users/").child(phone_number).child("token").get()],
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send_multicast(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
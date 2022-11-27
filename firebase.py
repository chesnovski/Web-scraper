import pyrebase
import json
config={
    'apiKey': "AIzaSyA1FW1ulMOAYYZRBcxA6t5gUNePrw1XuQ0",
    'authDomain': "vinted-db.firebaseapp.com",
    'projectId': "vinted-db",
    'databaseURL':"https://vinted-db-default-rtdb.firebaseio.com/",
    'storageBucket':"vinted-db.appspot.com",
    'messagingSenderId': "695963442566",
    'appId': "1:695963442566:web:f04a44899fb0b458f4a007",
    'measurementId': "G-NMCX2JTWR6"
 }

firebase=pyrebase.initialize_app(config)
database=firebase.database()

# items=database.child('Data').order_by_child('Date').get()
# for item in items:   
#     print(item.val())
# data={
#     'Age': 43, 'Name': 'geo', 'Likes': True
# }





#-------------------------------------------------------------------------------------------------------
#Create Data

# database.child('Users').child('FirstPers').set(data)

# database.child('Users').child('SecondPers').set(data)

#-------------------------------------------------------------------------------------------------------
#Read data

# geo=database.child('Users').child('SecondPers').get()
# print(geo.val())

#-------------------------------------------------------------------------------------------------------
#Update data
# database.child('Users').child('SecondPers').update({'Name':'John'})

#-------------------------------------------------------------------------------------------------------
#Remove data 

# database.child('Users').child('FirstPers').child('Likes').remove()

# database.push(data)

# database.child('Users').child('First').set(data)



# database.child('Data').set(jsonStr)


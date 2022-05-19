# import pyrebase
#
# config = {
#     "apiKey": "AIzaSyAV6Zilk22PWRJCjbfWqxG582uj8o6_OLk",
#     "authDomain": "django-mani.firebaseapp.com",
#     "databaseURL": "https://django-mani.firebaseio.com",
#     "projectId": "django-mani",
#     "storageBucket": "django-mani.appspot.com",
#     "messagingSenderId": "574944528259" }
#
# # config = {
# #     "apiKey": "AIzaSyBZ85aqc2Mt63yc_VM8wBJiGhwJ0ixOAVg",
# #     "authDomain": "techutsav-tce.firebaseapp.com",
# #     "databaseURL": "https://techutsav-tce.firebaseio.com",
# #     "projectId": "techutsav-tce",
# #     "storageBucket": "techutsav-tce.appspot.com",
# #     "messagingSenderId": "224256675890",
# # }
#
# # da = open("/home/sachin/Desktop/photography.jpg")
# firebase = pyrebase.initialize_app(config)
# storage = firebase.storage()
# storage.child("filename").put("/home/sachin/Desktop/photography.jpg")

import json, sys, getopt, firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize credentials
cred = credentials.Certificate('fv-creds.json')
firebase_admin.initialize_app(cred)

peelId = input("Please enter student number / Peel number to update\n")

db = firestore.client()
user_ref = db.collection(u'users').document(peelId)

user = user_ref.get()
if user.exists:
    print(f"Current user data: {user.to_dict()}")

    # Set voted
    voted = ""
    while not voted:
        voted = input("Set voted to? (t/f)\n").lower()
        if voted == "t" or voted == "true":
            user_ref.update({u"voted": True})
        elif voted == "f" or voted == "false":
            user_ref.update({u"voted": False})
        else:
            print("Invalid input!")
            voted = ""

    # Set admin
    admin = ""
    while not admin:
        admin = input("Set admin to? (t/f)").lower()
        if admin == "t" or admin == "true":
            user_ref.update({u"admin": True})
        elif admin == "f" or admin == "false":
            user_ref.update({u"admin": False})
        else:
            print("Invalid input!")
            admin = ""
    
    user = user_ref.get()
    print(f"Current user data: {user.to_dict()}")
    print(f"Finished!")
else:
    print("Invalid user! Exiting...")
    exit

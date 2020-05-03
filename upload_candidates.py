import json, sys, getopt, firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize credentials
cred = credentials.Certificate('fv-creds.json')
firebase_admin.initialize_app(cred)

# Load JSON
path = sys.argv[1]
with open(path) as f:
    users = json.load(f)

db = firestore.client()
users_ref = db.collection(u'users')

for user in users:
    data = {
        u'admin': False,
        u'voted': False
    }
    users_ref.document(user).set(data)
    print(f"Setting data for {user}")


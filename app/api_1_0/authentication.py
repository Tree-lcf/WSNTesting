from flask_httpauth import HTTPBasicAuth
from flask import g

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user = User


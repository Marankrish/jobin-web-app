from flask import Blueprint
auth = Blueprint('auth',__name__)
@auth.route('/auth/')
def home():
    return "<h1>sample2</h1>"
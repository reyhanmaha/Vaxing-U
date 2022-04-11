from flask import Blueprint, render_template, jsonify, request, send_from_directory, url_for
from flask_jwt import jwt_required
from flask_login import LoginManager, UserMixin,login_required,current_user
import json
import requests

from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
)

mainPage_views = Blueprint('mainPage_views', __name__, template_folder='../templates')

@mainPage_views.route('/mainPage', methods = ['GET'])
@login_required
def show_main():

        #Covid Statistics API
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"Trinidad-and-Tobago"}

    headers = {
        "X-RapidAPI-Host": "covid-193.p.rapidapi.com",
        "X-RapidAPI-Key": "1942c9e20cmshed1754f2cb0a7d9p16ebe7jsn386a2f493715"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data=response.json()
    return render_template('index.html',data=data)

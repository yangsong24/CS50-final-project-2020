import requests
from flask import Flask, flash, jsonify, redirect, render_template, request

from boltiot import Bolt
import conf

app = Flask(__name__)


app.config["TEMPLATES_AUTO_RELOAD"] = True

api_key="d78d8253-1988-41d5-b288-1ef88c8c6774"
device_id="BOLT14855893"

mybolt = Bolt(api_key, device_id)

@app.route('/on', methods=["GET", "POST"])
def bolt():

    if request.method == "POST":

        if request.form['on'] == 'on':

            data = mybolt.digitalWrite('0', 'HIGH')
            print (data)

            return render_template("bolt.html")


    elif request.method == "GET":

        return render_template("intro.html")

@app.route('/off', methods=["GET", "POST"])
def boltoff():

    if request.method == "POST":

        if request.form['off'] == 'off':

            data = mybolt.digitalWrite('0', 'LOW')
            print (data)

            return render_template("bolt.html")

    elif request.method == "GET":

        return render_template("intro.html")


@app.route('/', methods=["GET", "POST"])
def submit():
    if request.method == "POST":

        if 'device' in request.form:

            return render_template("bolt.html")

        elif 'home' in request.form:

            return redirect("/")

    elif request.method == "GET":

        return render_template("intro.html")

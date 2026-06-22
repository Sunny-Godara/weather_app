from flask import Flask, url_for 
from markupsafe import escape
from flask import request
from flask import render_template
from weather_app import fetch_city_name
app = Flask(__name__)

@app.get('/')
def home():
    return render_template('home.html')

@app.post('/city_name')
def climate_info():
    city_name = request.form.get('city_name')
    weather_info = fetch_city_name(city_name)
    return f''' <h2>Here is the weather info :</h2> {weather_info}'''

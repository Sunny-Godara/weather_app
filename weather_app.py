
import requests
import json
import config

def fetch_city_name(city_name):
    city_name = 'sirsa'
    service_url = config.lat_long
    hmm  = dict()
    hmm['name'] = city_name
    hmm['count'] = 1 
    urlforlatlong = requests.get( service_url , params= hmm )
    print(urlforlatlong)
    data = urlforlatlong.json()
    latitude = data['results'][0]['latitude']
    longitude = data['results'][0]['longitude']

    weather_api = config.weatherapi
    weather = dict()
    weather['latitude'] = latitude
    weather['longitude'] = longitude
    weather['current'] = 'temperature_2m,windspeed_10m,relative_humidity_2m'

    weather_info = requests.get(weather_api , params = weather)
    weather_data = weather_info.json()
    temperature = weather_data['current']['temperature_2m']
    windspeed = weather_data['current']['windspeed_10m']
    relative_humidity = weather_data['current']['relative_humidity_2m']
        return f'''<h3>Here are your desired outputs : </h3>
        <br>
        {temperature} == Temperature <br>
        {windspeed} == Windspeed<br>
        {relative_humidity} == Relative Humidity'''





import urllib.request, urllib.parse
import json
import config
city = input('Enter the city name :')
serviceurl = config.lat_long 
hmm = dict()
hmm['name'] = city
hmm['count'] = 1
urlforlatandlong = serviceurl + urllib.parse.urlencode(hmm)
#print(url)
fhandle = urllib.request.urlopen(urlforlatandlong).read().decode()
data = json.loads(fhandle)
lat = json.dumps(data['results'][0]['latitude'] , indent = 4)

long = json.dumps(data['results'][0]['longitude'] , indent = 4)

weather = dict()
weather['latitude'] = lat
weather['longitude'] = long
weather['current'] = 'temperature_2m,windspeed_10m,relative_humidity_2m'
weatherapi = config.weatherapi
url = weatherapi + urllib.parse.urlencode(weather)
whandle = urllib.request.urlopen(url).read().decode()
info = json.loads(whandle)
print('Temprature:' , info['current']['temperature_2m'])
print('Windspeed:' , info['current']['windspeed_10m'])
print('relative humidity:' ,info['current']['relative_humidity_2m'])

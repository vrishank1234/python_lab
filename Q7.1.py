import requests

from datetime import datetime,timezone

api_key = 'acd6f15d1c237b3333f949075ba888ae'
url = 'http://api.openweathermap.org/data/2.5/weather'

city = input("Enter city: ")

params  = {
    'q': city,
    'appid' : api_key
}

response = requests.get(url, params=params)
data = response.json()

sunrise_timestamp = data ['sys']['sunrise']
sunset_timestamp = data ['sys']['sunset']

sunrise_time = datetime.fromtimestamp(sunrise_timestamp,tz=timezone.utc)
sunset_time = datetime.fromtimestamp(sunset_timestamp,tz=timezone.utc)

sunrise_time_str = sunrise_time.strftime('%H:%M')
sunset_time_str = sunset_time.strftime('%H:%M') 

# print(data)
print(f"Temperature: {data['main']['temp']} F")
print(f"Humidity: {data['main']['humidity']}%")
print(f"Sunrise time: {sunrise_time_str} UTC")
print(f"Sunset time: {sunset_time_str} UTC")

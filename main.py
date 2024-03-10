import requests
#get api and key from openweathermap
End_point = "https://api.openweathermap.org/data/2.5/forecast"
Api_Key = "68556584d4143e8e8483e6a60cacd67e"
parameter = {
    "lat":11.016010, #set your own lat annd lon
    "lon": 76.970306,
    "appid":Api_Key,
    "cnt":4,  #to take only 4 forecast
}

response = requests.get(url=End_point,params=parameter)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"])
will_rain = False
for data in weather_data["list"]:
    if int(data["weather"][0]["id"])<700:
        will_rain = True

if will_rain:
    print("Carry your umbrella")
else:
    print("Weather is clean")

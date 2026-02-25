import os
import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

API_KEY = os.getenv("API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")

if not all([API_KEY, TWILIO_SID, TWILIO_AUTH]):
    raise ValueError("Environment variables not loaded")

weather_params = {
    "lat": 12.971599,
    "lon": 77.594566,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data["list"][0]["weather"][0]["id"])

will_rain=False
# condition_code=[data["weather"][0]["id"] for data in weather_data["list"]]
for data in weather_data["list"]:
     condition_code=data["weather"][0]["id"]
     if int(condition_code)< 700:
         will_rain=True

if will_rain:
     client = Client(TWILIO_SID, TWILIO_AUTH)
     message=client.messages.create(
         body="It's going to rain today\n Please take a umbrella when you go outside 😊 ",
         from_="whatsapp:+14155238886",
         to="whatsapp:+91-8123354660"
     )

     print(message.status)

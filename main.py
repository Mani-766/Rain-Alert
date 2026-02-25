import requests
from twilio.rest import Client

OEM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_key = "23f6ceb7267c08d6d50e0d478691169f"
account_sid="AC639fe402050e14af9febe7a398bc64a4"
auth_token="344174a0a81a573f73efac7ebf9bbb6f"

weather_params = {
    "lat":12.971599,
    "lon":77.594566,
    "appid": api_key,
    "cnt":4
}

response = requests.get(OEM_Endpoint, params=weather_params)
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
     client=Client(account_sid,auth_token)
     message=client.messages.create(
         body="It's going to rain today\n Please take a umbrella when you go outside 😊 ",
         from_="whatsapp:+14155238886",
         to="whatsapp:+91-8123354660"
     )
     print(message.status)
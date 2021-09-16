import requests
import datetime as dt
import os


APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("NUTRIX_API_KEY")
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

nutrin_param = {
    "query": input("What workouts did you do today?"),
    "gender": "male",
    "weight_kg": 88.45,
    "height_cm": 177.8,
    "age": 21
}

response = requests.post(url=EXERCISE_ENDPOINT, json=nutrin_param, headers=headers)
response.raise_for_status()
data = response.json()
print(data)

# print(calories)

current_date = dt.datetime.today()
today = current_date.strftime("%d/%m/%Y")
# print(today)
time = current_date.strftime("%H:%M:%S")
# print(time)

SHEETY_PASSWORD = os.environ.get("SHEETY_PASSWORD")
sheety_header = {
"Authorization": SHEETY_PASSWORD
}
for exercise in data["exercises"]:
    sheety_param = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]

        }


    }

    shResponse = requests.post(url=SHEETY_ENDPOINT, json=sheety_param,headers=sheety_header)
    print(shResponse.text)
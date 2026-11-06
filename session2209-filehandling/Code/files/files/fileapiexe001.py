import requests

# 1. Ask the internet API for data (use the specific JSON endpoint)
response = requests.get("http://api.open-notify.org/iss-now.json")

# 2. Convert the response into a readable Python dictionary (JSON)
data = response.json()

# 3. Look inside the data to see where the space station is right now!
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

print(f"The Space Station is currently at Latitude: {latitude}, Longitude: {longitude}")

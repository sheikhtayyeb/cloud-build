import requests
import os

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def calculate_distance(source, destination):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": source,
        "destinations": destination,
        "key": GOOGLE_MAPS_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if data["status"] == "OK":
        distance = data["rows"][0]["elements"][0]["distance"]["value"] / 1000  # Convert meters to kilometers
        return distance
    else:
        raise Exception("Error fetching data from Google Maps API")

def get_directions(source, destination, mode):
    url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": source,
        "destination": destination,
        "mode": mode,
        "key": GOOGLE_MAPS_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if data["status"] == "OK":
        steps = data["routes"][0]["legs"][0]["steps"]
        directions = [step["html_instructions"] for step in steps]
        return directions
    else:
        raise Exception("Error fetching data from Google Maps API")

def calculate_price(distance, mode):
    base_price = 50
    price_per_km = 10 if mode == "car" else 5
    return base_price + (price_per_km * distance)

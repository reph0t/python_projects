import requests
import time


def get_iss_location():
    url = "http://api.open-notify.org/iss-now.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if the request was unsuccessful
        data = response.json()

        iss_position = data['iss_position']
        latitude = iss_position['latitude']
        longitude = iss_position['longitude']

        return latitude, longitude

    except requests.exceptions.RequestException as e:
        print(f"Error fetching ISS location: {e}")
        return None, None


while True:
    latitude, longitude = get_iss_location()

    if latitude and longitude:
        print(f"Current ISS Location: Latitude {latitude}, Longitude {longitude}")
    else:
        print("Failed to retrieve ISS location.")

    time.sleep(1)
import requests
import json

API_KEY = "w2V255WoWQ9WpLTRVkJpNUp3KDmjskck"

# Correct API endpoint for real-time weather from Tomorrow.io
url = "https://api.tomorrow.io/v4/timelines"

# Parameters
location = "25.761681,-80.191788"  # Location for Miami, FL

fields = [
    "temperature",
    "humidity",
    "windSpeed",
    "precipitationProbability",
    "uvIndex"
]
units = "imperial"
timesteps = "1d"  # Fetch current (real-time) data

# Query parameters
params = {
    "location": location,
    "fields": ",".join(fields),  # Comma-separated fields
    "units": units,
    "timesteps": timesteps,
    "apikey": API_KEY
}


def get_realtime_weather():
    try:
        # Make the GET request with query parameters
        response = requests.get(url, params = params, timeout = 5)
        response.raise_for_status()  # Raise an exception for bad responses

        # Parse the JSON response
        weather_data = response.json()

        # # Print the entire response for inspection
        # print(json.dumps(weather_data, indent=4))

        # Safely access the data, handle missing or empty values
        timelines = weather_data.get("data", {}).get("timelines", [])

        if not timelines:
            print("No timeline data found.")
            return

        intervals = timelines[0].get("intervals", [])

        if not intervals:
            print("No intervals data found.")
            return

        # Extract the first interval (current time) and the values
        values = intervals[0].get("values", {})

        # Extract specific fields
        temperature = values.get("temperature")
        humidity = values.get("humidity")
        wind_speed = values.get("windSpeed")
        precipitation_probability = values.get("precipitationProbability")
        uv_index = values.get("uvIndex")

        # Print the real-time data
        print(f"Location: {location}")
        print(f"Temperature: {temperature}°F")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} mph")
        print(f"Precipitation Probability: {precipitation_probability} %")
        print(f"UV Index: {uv_index}")

    except requests.exceptions.Timeout:
        print("The request timed out")

    except requests.exceptions.ConnectionError:
        print("A connection error occurred.")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching Forecast: {e}")
        return None




if __name__ == "__main__":
    get_realtime_weather()

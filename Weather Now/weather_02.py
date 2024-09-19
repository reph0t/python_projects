import requests
import json

def get_coordinates(city_name):
    loc_api = "5e90daf94d304b8dab802a61636d16fb"    # Opencage API
    url = "https://api.opencagedata.com/geocode/v1/json"    #Opencage URL


    # URL parameters for opencage
    params =  {
        "q" : city_name,
        "limit": "1",
        "language" : "en",
        "key" : loc_api

    }

    try:
        response = requests.get(url, params = params, timeout = 5)
        response.raise_for_status()
        location_data = response.json()

        if location_data["results"]:                # if there is results available
            geometry = location_data["results"][0]['geometry']      # go to 'results' dictionary and go into geometry
            lat, lng = geometry['lat'], geometry['lng']             # grab the coordinates
            location = ",".join([str(lat), str(lng)])               # join two variable into one
            # print(f"{city_name} Location: {location}")
            return location

        else:
            print(f"No result found for {city_name}")       # if the city input does not exist return none
            return None

    except requests.exceptions.RequestException as e:       # raise an error
        print(f"Error Occurred: {e}")
        return None

def parameters(location):

    API_KEY = "w2V255WoWQ9WpLTRVkJpNUp3KDmjskck"  # tomorrow.io API

    fields = [
        "temperature",
        "humidity",
        "windSpeed",
        "precipitationProbability",
        "uvIndex"
    ]


    while True:
        user_input = input("Choose 'F' for Fahrenheit or 'C' for celsius: ").strip().upper()

        if user_input == 'F':
            units = "imperial"
            break

        elif user_input == 'C':
            units = "metric"
            break

        else:
            print("Please enter the correct metric")

    params = {
        "location": location,
        "fields": ",".join(fields),  # Comma-separated fields
        "units": units,
        "apikey": API_KEY
    }

    return params

def get_realtime_weather(params):
    # Correct API endpoint for real-time weather from Tomorrow.io
    url = "https://api.tomorrow.io/v4/weather/realtime"

    try:

        # Make the GET request with query parameters
        response = requests.get(url, params = params, timeout = 5)
        response.raise_for_status()  # Raise an exception for bad responses

        # Parse the JSON response
        weather_data = response.json()

        # Safely access the data, handle missing or empty values
        values = weather_data.get("data", {}).get("values", {})

        if not values:
            print("No Value data found.")
            return

        temperature = values.get("temperature")
        humidity = values.get("humidity")
        wind_speed = values.get("windSpeed")
        precipitation_probability = values.get("precipitationProbability")
        uv_index = values.get("uvIndex")

        # Print the real-time Weather data
        if params.get("units") == "imperial":       # Checks if the unit is imperial
            print(f"Temperature: {temperature}°F")

        elif params.get("units") == "metric":       # Checks if the unit is metric
            print(f"Temperature: {temperature}°C")

        print(f"Humidity: {humidity}%")


        if params.get("units") == "imperial":
            print(f"Wind Speed: {wind_speed} mph")

        elif params.get("units") == "metric":
                print(f"Wind Speed: {wind_speed} m/s")

        # Precipitation Probability
        print(f"Precipitation Probability: {precipitation_probability}%")

        # UV Index
        if uv_index <= 2:   # if uv index is between 1 and 2 --> LOW
            print(f'UV Index: {uv_index} ("LOW")')

        elif uv_index <= 5:     # if uv index is between 3 and 5 --> LOW
            print(f'UV Index: {uv_index} ("MODERATE")')

        elif uv_index <= 7:     # if uv index is between 6 and 7 --> LOW
            print(f'UV Index: {uv_index} ("HIGH")')

        elif uv_index <= 10:        # if uv index is between 7 and 10 --> LOW
            print(f'UV Index: {uv_index}("VERY HIGH")')

        else:   # Anything Higher ---> Extreme 
            print("EXTREME")


    # Raising Exceptions
    except requests.exceptions.Timeout:     # If the request to the server has Timed out Print this message
        print("The request timed out")

    except requests.exceptions.ConnectionError:     # If lost connection print this message
        print("A connection error occurred.")

    except requests.exceptions.HTTPError as e:      # If the request to the server has Timed out Print this message
        print(f"HTTP error occurred: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching Forecast: {e}")
        return None

def main():

    while True:
        city_input = input("Enter City Name: ")
        coordinates = get_coordinates(city_input)

        if coordinates:
            params = parameters(coordinates)
            get_realtime_weather(params)

if __name__ == "__main__":
    main()

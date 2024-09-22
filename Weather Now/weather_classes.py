import requests
 

class Location:
    def __init__(self, city):
        self._city_name = city
        self._coordinates = None
        self.api_key = "5e90daf94d304b8dab802a61636d16fb"  # Opencage API

    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, city):
        if isinstance(city, str) and city.strip():
            self._city_name = city
        else:
            raise ValueError("City name must be a valid non-empty string")

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, location):
        if isinstance(location, str) and "," in location:
            self._coordinates = location
        else:
            raise ValueError("Coorindates must be a valid lat, lng string")

    def fetch_coordinates(self):
        url = "https://api.opencagedata.com/geocode/v1/json"
        params = {
            "q": self.city_name,
            "limit": "1",
            "language": "en",
            "key": self.api_key
        }

        try:
            response = requests.get(url, params = params, timeout = 5)
            response.raise_for_status()
            location_data = response.json()

            if location_data["results"]:
                geometry = location_data["results"][0]['geometry']
                lat, lng = geometry['lat'], geometry['lng']
                self.coordinates = f"{lat},{lng}"
                print(f"{self.city_name} Location: {self.coordinates}")
            else:
                print(f"No result found for {self.city_name}")
                self.coordinates = None

        except requests.exceptions.RequestException as e:
            print(f"Error Occurred: {e}")
            self.coordinates = None


class WeatherParameters:

    def __init__(self, location):
        self._location = location
        self.api_key = "w2V255WoWQ9WpLTRVkJpNUp3KDmjskck"  # tomorrow.io API
        self._units = None

    @property
    def units(self):
        return self._units


    @units.setter
    def units(self,unit):
        if unit in ["imperial", "metric"]:
            self._units = unit
        else:
            raise ValueError("Units must be either 'imperial' or 'metric'.")

    @property
    def location(self):
        return self._location


    def get_params(self):

        fields = [
            "temperature",
            "humidity",
            "windSpeed",
            "precipitationProbability",
            "uvIndex"
        ]
        attempts = 0
        while attempts < 3:
            user_input = input("Choose 'F' for Fahrenheit or 'C' for celsius: ").strip().upper()

            if user_input == 'F':
                self._units = "imperial"
                break
            elif user_input == 'C':
                self._units = "metric"
                break
            else:
                print("Please enter the correct metric")
                attempts += 1

        if attempts == 3:
            print("Invalid input. Defaulting to Fahrenheit.")
            self._units = "imperial"

        return {
            "location": self._location,
            "fields": ",".join(fields),  # Comma-separated fields
            "units": self._units,
            "apikey": self.api_key
        }

class Weather:

    def __init__(self, params):
        self._params = params
        self._temperature = None
        self._humidity = None
        self._wind_speed = None

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temp):
        if temp is not None and isinstance(temp,(int, float)):
            self._temperature = temp
        else:
            raise ValueError("Temperature must be a valid number.")


    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, humid):
        if humid is not None and 0 <= humid <= 100:
            self._humidity = humid

        else:
            raise ValueError("Humidity must be 0 and 100.")

    @property
    def wind_speed(self):
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, wind):
        if wind is not None and isinstance(wind,(int, float)):
            self._wind_speed = wind

        else:
            raise ValueError("Wind Speed must be a valid number")



    def fetch_realtime_weather(self):
        url = "https://api.tomorrow.io/v4/weather/realtime"

        try:
            response = requests.get(url, params = self._params, timeout = 5)
            response.raise_for_status()

            weather_data = response.json()

            # Safely access the data, handle missing or empty values
            values = weather_data.get("data", {}).get("values", {})

            if not values:
                print("No Value data found.")
                return None

            self.display_weather(values)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching Forecast: {e}")


    def display_weather(self, values):
        self._temperature = values.get("temperature")
        self._humidity = values.get("humidity")
        self._wind_speed = values.get("windSpeed")
        precipitation_probability = values.get("precipitationProbability")
        uv_index = values.get("uvIndex")

        if self._params["units"] == "imperial":
            print(f"Temperature: {self._temperature}°F")
            print(f"Wind Speed: {self._wind_speed} mph")
        else:
            print(f"Temperature: {self._temperature}°C")
            print(f"Wind Speed: {self._wind_speed} m/s")

        print(f"Humidity: {self._humidity}%")
        print(f"Precipitation Probability: {precipitation_probability}%")
        self.display_uv_index(uv_index)

    def display_uv_index(self, uv_index):
        if uv_index is not None:
            if uv_index <= 2:
                print(f'UV Index: {uv_index} ("LOW")')
            elif uv_index <= 5:
                print(f'UV Index: {uv_index} ("MODERATE")')
            elif uv_index <= 7:
                print(f'UV Index: {uv_index} ("HIGH")')
            elif uv_index <= 10:
                print(f'UV Index: {uv_index} ("VERY HIGH")')
            else:
                print("EXTREME")
        else:
            print("UV Index is not available.")




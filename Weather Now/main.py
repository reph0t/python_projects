from weather_classes import Location, WeatherParameters, Weather

class WeatherApp:
    def run(self):
        while True:
            city_input = input("Enter City Name: ")
            location = Location(city_input)
            location.fetch_coordinates()

            if location.coordinates:
                params = WeatherParameters(location.coordinates).get_params()
                weather = Weather(params)
                weather.fetch_realtime_weather()
            else:
                print("City does not exist. Please try again.")

if __name__ == "__main__":
    app = WeatherApp()
    app.run

import requests

#API URL for the astronauts in space
url = "http://api.open-notify.org/astros.json"

#Make a request to the API
response = requests.get(url)

#Convert the response to JSON format
data = response.json()

#Extract the number of astronauts
astronauts_in_space = data['number']

#Printthe result
print(f"There are currently {astronauts_in_space} astronauts in space.\n")

#Optional: List the names of the astronauts
for person in data['people']:
    print(f"{person['name']} is on the {person['craft']}")

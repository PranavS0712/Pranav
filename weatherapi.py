import requests

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(temperature):
    temp_in_celsius = round((temperature - 32) * 5 / 9, 2)
    return temp_in_celsius

# Input: Multiple cities separated by commas
cities = input("Enter the cities (separated by commas):\n").split(',')

# Loop over each city
for city in cities:
    city = city.strip()  # Remove any extra spaces
    url = f'http://api.weatherapi.com/v1/current.json?key=7e495e3681ca45b6a4e92359241910&q={city}&aqi=no'
    response = requests.get(url)
    json_data = response.json()
    temperature_f = json_data.get('current').get('temp_f')
    temperature_c = fahrenheit_to_celsius(temperature_f)
    description = json_data.get('current').get('condition').get('text')
    print(f"The weather in {city} today is {description} and {temperature_c} degrees Celsius.")
        

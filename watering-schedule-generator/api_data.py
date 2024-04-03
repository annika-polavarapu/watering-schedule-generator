import urllib.request
import json

def fetch_weather_data(latitude, longitude):
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relative_humidity_2m,precipitation_probability,precipitation,soil_temperature_6cm,soil_moisture_3_to_9cm"

    try:
        with urllib.request.urlopen(api_url) as response:
            data = json.loads(response.read().decode())

        temperature = data['hourly']['temperature_2m']
        humidity = data['hourly']['relative_humidity_2m']
        precipitation_probability = data['hourly']['precipitation_probability']
        precipitation = data['hourly']['precipitation']
        soil_temperature = data['hourly']['soil_temperature_6cm']
        soil_moisture = data['hourly']['soil_moisture_3_to_9cm']

        # Storing the weather data as dictionary
        return {
            'temperature': temperature,
            'humidity': humidity,
            'precipitation_probability': precipitation_probability,
            'precipitation': precipitation,
            'soil_temperature': soil_temperature,
            'soil_moisture': soil_moisture
        }
    except urllib.error.URLError as e:
        print("Error fetching weather data:", e)
        return None

if __name__ == "__main__":
    latitude = 37.3144
    longitude = -122.0566
    weather_data = fetch_weather_data(latitude, longitude)
    if weather_data:
        # Put data in variables
        temperature = weather_data['temperature']
        humidity = weather_data['humidity']
        precipitation_probability = weather_data['precipitation_probability']
        precipitation = weather_data['precipitation']
        soil_temperature = weather_data['soil_temperature']
        soil_moisture = weather_data['soil_moisture']
        
        # Print variables
        print("Temperature:", temperature)
        print("Humidity:", humidity)
        print("Precipitation Probability:", precipitation_probability)
        print("Precipitation:", precipitation)
        print("Soil Temperature:", soil_temperature)
        print("Soil Moisture:", soil_moisture)


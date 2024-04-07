import urllib.request
import json

def fetchWeatherData(latitude, longitude):
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relative_humidity_2m,precipitation_probability,precipitation,soil_temperature_6cm,soil_moisture_3_to_9cm"

    try:
        with urllib.request.urlopen(api_url) as response:
            data = json.loads(response.read().decode())

        temperature = data['hourly']['temperature_2m']
        humidity = data['hourly']['relativeHumidity_2m']
        precipitationProbability = data['hourly']['precipitationProbability']
        precipitation = data['hourly']['precipitation']
        soilTemperature = data['hourly']['soilTemperature6cm']
        soilMoisture = data['hourly']['soilMoisture3To9cm']

        # Storing the weather data as dictionary
        return {
            'temperature': temperature,
            'humidity': humidity,
            'precipitation_probability': precipitationProbability,
            'precipitation': precipitation,
            'soilTemperature': soilTemperature,
            'soilMoisture': soilMoisture
        }
    except urllib.error.URLError as e:
        print("Error fetching weather data:", e)
        return None

if __name__ == "__main__":
    latitude = 37.3144
    longitude = -122.0566
    weatherData = fetchWeatherData(latitude, longitude)
    if weatherData:
        # Put data in variables
        temperature = weatherData['temperature']
        humidity = weatherData['humidity']
        precipitationProbability = weatherData['precipitationProbability']
        precipitation = weatherData['precipitation']
        soilTemperature = weatherData['soilTemperature']
        soilMoisture = weatherData['soilMoisture']
        
        # Print variables
        print("Temperature:", temperature)
        print("Humidity:", humidity)
        print("Precipitation Probability:", precipitationProbability)
        print("Precipitation:", precipitation)
        print("Soil Temperature:", soilTemperature)
        print("Soil Moisture:", soilMoisture)


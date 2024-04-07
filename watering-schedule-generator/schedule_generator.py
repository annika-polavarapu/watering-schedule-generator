from api_data import fetchWeatherData

def shouldWater(temperature, humidity, precipitationProbability, precipitation, soilMoisture):
    # Min and max values for watering
    minTemperature = 20  
    maxHumidity = 80     
    maxPrecipitationProbability = 50 
    maxPrecipitation = 1  
    minSoilMoisture = 0.3  

    # Checking if any of the conditions are met to need watering
    if temperature > minTemperature \
        and humidity < maxHumidity \
        and precipitationProbability < maxPrecipitationProbability \
        and precipitation < maxPrecipitation \
        and soilMoisture < minSoilMoisture:
        return True
    else:
        return False

def generateWateringSchedule(weatherData):
    # Extracting weather variables from the data for 7 days
    temperature = weatherData['temperature'][:7]
    humidity = weatherData['humidity'][:7]
    precipitationProbability = weatherData['precipitationProbability'][:7]
    precipitation = weatherData['precipitation'][:7]
    soilMoisture = weatherData['soilMoisture'][:7]

    # Generating watering schedule
    wateringSchedule = []
    for day in range(len(temperature)):
        if shouldWater(temperature[day], humidity[day], precipitationProbability[day], precipitation[day], soilMoisture[day]):
            wateringSchedule.append(f"Day {day + 1}: Watering needed")
        else:
            wateringSchedule.append(f"Day {day + 1}: No watering needed")
    
    return wateringSchedule

def main():
    useHardcodedData = True

    if useHardcodedData:
        # Hardcoded weather data
        weatherData = {
            'temperature': [22, 24, 23, 20, 18, 21, 20],
            'humidity': [70, 75, 80, 78, 82, 75, 70],
            'precipitationProbability': [10, 20, 15, 5, 30, 10, 25],
            'precipitation': [0.1, 0.2, 0.0, 0.0, 0.5, 0.3, 0.0],
            'soilMoisture': [0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1]
        }
    else:
        # Fetching weather data from API
        latitude = 37.322998 # Cupertino
        longitude = -122.032181
        weatherData = fetchWeatherData(latitude, longitude)

    if weatherData:
        # Generating watering schedule
        wateringSchedule = generateWateringSchedule(weatherData)
        print("Watering Schedule for the Next 7 Days:")
        for entry in wateringSchedule:
            print(entry)
    else:
        print("Failed to fetch weather data. Please check your API connection or set useDardcodedData to True.")

if __name__ == "__main__":
    main()

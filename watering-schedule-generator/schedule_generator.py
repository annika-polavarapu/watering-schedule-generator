from api_data import fetchWeatherData

def shouldWater(temperature, humidity, precipitationProbability, precipitation, soilMoisture, wateringNeeds, sunlightExposure):
    # Min and max values for watering
    minTemperature = 20 - wateringNeeds * 2
    maxHumidity = 80 + wateringNeeds * 5  
    maxPrecipitationProbability = 50 - wateringNeeds * 10  
    maxPrecipitation = 1 - wateringNeeds * 0.2 
    minSoilMoisture = 0.3 - wateringNeeds * 0.1

    if sunlightExposure == "shade":
        maxHumidity -= 5

    # Checking if any of the conditions are met to need watering
    if temperature > minTemperature \
        and humidity < maxHumidity \
        and precipitationProbability < maxPrecipitationProbability \
        and precipitation < maxPrecipitation \
        and soilMoisture < minSoilMoisture:
        return True
    else:
        return False

def generateWateringSchedule(weatherData, wateringNeeds, sunlighExposure, lastWateredDay):
    # Extracting weather variables from the data for 7 days
    temperature = weatherData['temperature']#[:7]
    humidity = weatherData['humidity']#[:7]
    precipitationProbability = weatherData['precipitationProbability']#[:7]
    precipitation = weatherData['precipitation']#[:7]
    soilMoisture = weatherData['soilMoisture']#[:7]

    # Generating watering schedule
    wateringSchedule = []
    for day in range(len(temperature)):
        if shouldWater(temperature[day], humidity[day], precipitationProbability[day], precipitation[day], soilMoisture[day], wateringNeeds, sunlighExposure):
            wateringSchedule.append(f"Day {day + 1}: Watering needed")
            lastWateredDay = day
        else:
            wateringSchedule.append(f"Day {day + 1}: No watering needed")
    
    return wateringSchedule, lastWateredDay

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
        # Getting user input
        wateringNeeds = input("Enter watering needs (low, medium, high): ")
        sunlightExposure = input("Enter sunlight exposure (shade, sun): ")

        if wateringNeeds == "low":
            wateringNeeds = 1
        elif wateringNeeds == "medium":
            wateringNeeds = 2
        elif wateringNeeds == "high":
            wateringNeeds = 3
        else:
            print("Invalid watering needs. Defaulting to medium.")
            wateringNeeds = 2
        
        lastWateredDay = -1
        
        # Generating watering schedule
        wateringSchedule, lastWateredDay = generateWateringSchedule(weatherData, wateringNeeds, sunlightExposure, lastWateredDay)
        print("Watering Schedule for the Next 7 Days:")
        for entry in wateringSchedule:
            print(entry)
    else:
        print("Failed to fetch weather data. Please check your API connection or set useDardcodedData to True.")

if __name__ == "__main__":
    main()

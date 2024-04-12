import streamlit as st
from api_data import getWeatherData

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

def generateWateringSchedule(weatherData, wateringNeeds, sunlightExposure, lastWateredDay):
    # Extracting weather variables from the data for 7 days
    temperature = weatherData['temperature'][:7]
    humidity = weatherData['humidity'][:7]
    precipitationProbability = weatherData['precipitation_probability'][:7]
    precipitation = weatherData['precipitation'][:7]
    soilMoisture = weatherData['soil_moisture'][:7]

    # Generating watering schedule
    wateringSchedule = []
    for day in range(len(temperature)):
        if shouldWater(temperature[day], humidity[day], precipitationProbability[day], precipitation[day], soilMoisture[day], wateringNeeds, sunlightExposure):
            wateringSchedule.append(f"Day {day + 1}: Watering needed")
            lastWateredDay = day
        else:
            wateringSchedule.append(f"Day {day + 1}: No watering needed")
    
    return wateringSchedule, lastWateredDay

def main():
    st.title("Watering Schedule Generator")

    useHardcodedData = st.checkbox("Use hardcoded data")

    if useHardcodedData:
        # Hardcoded weather data
        weatherData = {
            'temperature': [22, 24, 23, 20, 18, 21, 20],
            'humidity': [70, 75, 80, 78, 82, 75, 70],
            'precipitation_probability': [10, 20, 15, 5, 30, 10, 25],
            'precipitation': [0.1, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0],
            'soil_moisture': [0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1]
        }
    else:
        # Fetching weather data from API
        latitude = st.number_input("Enter latitude coordinate of your location", value=37.322998)
        longitude = st.number_input("Enter longitude coordinate of your location", value=-122.032181)
        weatherData = getWeatherData(latitude, longitude)

    if weatherData:
        wateringNeeds = st.selectbox("Select watering needs", ["Low", "Medium", "High"])
        sunlightExposure = st.selectbox("Select sunlight exposure", ["Shade", "Sun"])

        if wateringNeeds == "Low":
            wateringNeeds = 1
        elif wateringNeeds == "Medium":
            wateringNeeds = 2
        elif wateringNeeds == "High":
            wateringNeeds = 3

        lastWateredDay = -1
        
        # Generating watering schedule
        wateringSchedule, lastWateredDay = generateWateringSchedule(weatherData, wateringNeeds, sunlightExposure.lower(), lastWateredDay)
        st.subheader("Watering Schedule for the Next 7 Days:")
        for entry in wateringSchedule:
            st.write(entry)
    else:
        st.error("Failed to fetch weather data. Please check your API connection or set useHardcodedData to True.")

if __name__ == "__main__":
    main()

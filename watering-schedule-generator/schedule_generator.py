from api_data import fetch_weather_data

def should_water(temperature, humidity, precipitation_probability, precipitation, soil_moisture):
    # Define thresholds
    min_temperature = 20  
    max_humidity = 80     
    max_precipitation_probability = 50 
    max_precipitation = 1  
    min_soil_moisture = 0.3  

    # Checking if any of the conditions are met to trigger watering
    if temperature > min_temperature \
        and humidity < max_humidity \
        and precipitation_probability < max_precipitation_probability \
        and precipitation < max_precipitation \
        and soil_moisture < min_soil_moisture:
        return True
    else:
        return False

def generate_watering_schedule(weather_data):
    # Extract weather variables from the data for 7 days
    temperature = weather_data['temperature'][:7]
    humidity = weather_data['humidity'][:7]
    precipitation_probability = weather_data['precipitation_probability'][:7]
    precipitation = weather_data['precipitation'][:7]
    soil_moisture = weather_data['soil_moisture'][:7]

    # Generate watering schedule based on weather data
    watering_schedule = []
    for day in range(len(temperature)):
        if should_water(temperature[day], humidity[day], precipitation_probability[day], precipitation[day], soil_moisture[day]):
            watering_schedule.append(f"Day {day + 1}: Watering needed")
        else:
            watering_schedule.append(f"Day {day + 1}: No watering needed")
    
    return watering_schedule

def main():
    # Option to use hardcoded data
    use_hardcoded_data = True

    if use_hardcoded_data:
        # Hardcoded weather data for demonstration
        weather_data = {
            'temperature': [22, 24, 23, 20, 18, 21, 20],
            'humidity': [70, 75, 80, 78, 82, 75, 70],
            'precipitation_probability': [10, 20, 15, 5, 30, 10, 25],
            'precipitation': [0.1, 0.2, 0.0, 0.0, 0.5, 0.3, 0.0],
            'soil_moisture': [0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1]
        }
    else:
        # Fetch weather data from API
        latitude = 37.322998 # Cupertino
        longitude = -122.032181
        weather_data = fetch_weather_data(latitude, longitude)

    if weather_data:
        # Generate watering schedule based on weather data
        watering_schedule = generate_watering_schedule(weather_data)
        print("Watering Schedule for the Next 7 Days:")
        for entry in watering_schedule:
            print(entry)
    else:
        print("Failed to fetch weather data. Please check your API connection or set use_hardcoded_data to True.")

if __name__ == "__main__":
    main()

import pytest
from schedule_generator import shouldWater, generateWateringSchedule

def test_generateWateringSchedule():
    weatherData = {
        'temperature': [22, 24, 23, 20, 18, 21, 20],
        'humidity': [70, 75, 80, 78, 82, 75, 70],
        'precipitationProbability': [10, 20, 15, 5, 30, 10, 25],
        'precipitation': [0.1, 0.2, 0.0, 0.0, 0.5, 0.3, 0.0],
        'soilMoisture': [0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1]
    }
    expectedSchedule = [
        "Day 1: No watering needed",
        "Day 2: No watering needed",
        "Day 3: No watering needed",
        "Day 4: Watering needed",
        "Day 5: No watering needed",
        "Day 6: No watering needed",
        "Day 7: Watering needed"
    ]
    assert generateWateringSchedule(weatherData) == expectedSchedule
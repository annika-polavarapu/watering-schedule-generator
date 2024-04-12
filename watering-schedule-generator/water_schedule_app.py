import streamlit as st
from schedule_generator import fetchWeatherData, generateWateringSchedule

def main():
    st.title("Watering Schedule Generator")
    st.write("This app helps you determine the most optimal days to water your garden based on weather data.")

    use_hardcoded_data = st.checkbox("Use hardcoded weather data", True)


if __name__ == "__main__":
    main()
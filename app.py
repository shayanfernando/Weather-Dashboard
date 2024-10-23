import streamlit as st
import requests
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.pexels.com/photos/1118873/pexels-photo-1118873.jpeg?cs=srgb&dl=pexels-jplenio-1118873.jpg&fm=jpg");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
def get_weather_data(latitude,longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    
    # Check if the API call was successful
    if response.status_code == 200:
        data = response.json()
        return data.get('current_weather', {})
    else:
        st.error("Failed to retrieve data")
        return {}
    # # Check if the API call was successful
    # if response.status_code == 200:
    #     data = response.json()
    #     return data.get('current_weather', {})
    # else:
    #     st.error("Failed to retrieve data")
    #     return {}
# print("Shayan")
# print(89+765)
# st.write("Shayan")
st.title("Weather Dashboard")

st.sidebar.header("location")
latitude = st.sidebar.text_input("Enter Latitude", value="52.52")  # Default: Sri Lanka
longitude = st.sidebar.text_input("Enter Longitude", value="13.41")  # Default: Sri Lanka

# Button to fetch weather data
if st.button("Get Weather"):
    weather_data = get_weather_data(latitude, longitude)
    
    # Display the weather data
    if weather_data:
        st.write(f"*Temperature:* {weather_data.get('temperature', 'N/A')}°C")
        st.write(f"*Pressure:* {weather_data.get('pressure_msl', 'N/A')} hPa")
        st.write(f"*Wind Speed:* {weather_data.get('windspeed', 'N/A')} m/s")
        
        # Simple weather interpretation
        temp = weather_data.get('temperature', 0)
        wind_speed = weather_data.get('windspeed', 0)
        
        if temp > 25:
            st.success("It's a warm day 🌞")
        elif temp > 15:
            st.info("It's a mild day 🌤️")
        else:
            st.warning("It's a cold day ❄️")
        
        if wind_speed > 10:
            st.warning("It's windy today 💨")
    else:
        st.error("No data found")
st.image("Unknown.png")
st.video("https://youtu.be/GDlkCkcIqTs?si=bnn_K7Ihxi1ITf-X")
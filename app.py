import streamlit as st
import requests
import os

# Get API Key 
api_key = st.secrets['api_key']

# Custom CSS
#def custom_css():
with open('css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Title
st.title('Weather Info')

city = st.text_input('Enter a city name')

# Function to search weather of a city
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    res = requests.get(url)

    if res.status_code == 404:
        st.write('City not found. Please make sure spelling is correct.')
        return None
    
    data = res.json()

    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    speed = data['wind']['speed']
    city = data['name']
    country = data['sys']['country']

    st.write(f'{city}, {country}')
    st.write(f'Weather: {description}')
    st.write(f'Temperature: {temperature}°F')
    st.write(f'Wind Speed: {speed}mph') 

if st.button('Get Weather'):
    get_weather(city)

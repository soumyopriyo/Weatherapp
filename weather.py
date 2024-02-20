from dotenv import load_dotenv #dotenv loads environment variables from a .env file
from pprint import pprint 
import requests #Python requests is a library for making HTTP requests
import os #it provides functions for interacting with the operating system

load_dotenv()

def get_current_weather(city="Durgapur",):
    #getting the data from using the api
    request_url=f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data=requests.get(request_url).jason()

    return weather_data

if __name__=="__main__":
    print("\n*** Get Current Weather Conditions ***\n")

    city=input("\n Please enter a city name:")
    weather_data=get_current_weather(city)
    print("\n")
    pprint(weather_data)


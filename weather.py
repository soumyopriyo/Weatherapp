from dotenv import load_dotenv #dotenv loads environment variables from a .env file
from pprint import pprint 
import requests #Python requests is a library for making HTTP requests
import os #it provides functions for interacting with the operating system

load_dotenv()#load_env() will only load environment variables that are not already set in the environment.
             #If an environment variable is already set, its value in the .env file will be ignored.

def get_current_weather(city="Durgapur"):
   
    #getting the data from using the api
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("New_API_KEY")}&q={city}&units=metric'
    #request_url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={os.getenv("New_API_KEY")}'
    
    weather_data=requests.get(request_url).json()

    return weather_data

if __name__=="__main__":
    print("\n*** Get Current Weather Conditions ***\n")

    city=input("\n Please enter a city name:")
    # #Check for empty entry or entry with spaces
    # if not bool(city.strip()):
    #     city="New Delhi"

    weather_data=get_current_weather(city)
    print("\n")
    pprint(weather_data)

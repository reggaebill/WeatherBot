import json
import discord
import requests
from geopy import Nominatim

#load weather API
weather_api = open('C:\\Users\\aaron\\Downloads\\openapi.json')
json.load(weather_api)

from discord.ext import commands

def parse_day(day):        #splits up the time parameter and returns day only
    time_list = day.split("T")
    time_day = time_list[0].split('-')
    time_day = time_day[1:]
    day_final = f'{time_day[0]}-{time_day[1]}'
    return day_final

def parse_time(time):     #splits up the time parameter and returns hour only
    time_list = time.split('T')
    time_time = time_list[1].split('-')
    hour_time = time_time[0].split(':')
    hour_time = hour_time[:2]
    hour_time = f'{hour_time[0]}:{hour_time[1]}'
    return hour_time
def get_geocode(location):     #turns text location into coordinates
    location = geolocator.geocode(location)
    print(location.latitude, location.longitude)
    return (f'{location.latitude},{location.longitude}')

def callWeather(x):      #sends lat, long to API, parses the returned info, and formats text
    hourly_outlook = ''
    i = 0
    response = requests.get(f'https://api.weather.gov/points/{x}')
    if response.status_code == 200:
        data = response.json()
        hourly_data = requests.get(data['properties']['forecastHourly'])
        hourly_data_parsed = hourly_data.json()
        list_data = hourly_data_parsed['properties']['periods']
        for item in list_data:
            day = parse_day(item['startTime'])
            time = parse_time(item['startTime'])
            temp = f'{item['temperature']}:{item['temperatureUnit']}'
            outlook = f'{item['shortForecast']}'
            hourly_outlook += f'{day} : {time} | {temp} | {outlook}\n'
            i += 1
            if i == 25:
                break
        return hourly_outlook
    else:
        return "https://tenor.com/view/wouldnt-you-like-to-know-weather-boy-gif-15559185"





#intialize geopy

geolocator = Nominatim(user_agent="weatherbot")

#initialize requests module
r = requests.get('https://api.weather.gov')
r.status_code

r.headers['content-type'] = 'application/json'
r.encoding = 'utf-8'

#initialize discord api

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
client = discord.Client(intents=intents)

#discord bot commands

@client.event
async def on_message(message):
    if message.author == client.user:
        return

@client.event
async def on_ready():
    message.send('dis the bot')

@bot.command()
async def hourly(message, postal_code):
    coordinates = get_geocode(postal_code)
    await message.send(callWeather(coordinates))

@bot.command()
async def ping(message):
    await message.send('pong')


bot.run('MTM0MzM1NzIzMDMwNDU5MjAwNQ.GjVA4D.FtCugN4KGMi0JCFpPq-HQLSuHuag00DQCQRn0w')

"""
Helper file to uncrowd the weather.py
"""
# IMPORTS
from config import *
import os
import sys
import time
import netatmo
import requests
import importlib
from PIL import Image, ImageDraw, ImageFont
import epd7in5_V2


# ICON LOOKUPS
def get_thermometer(temp):
  icon = "\uf2c9"  # half
  if float(temp) <= 0:
    icon = "\uf768"  # frigid
  elif float(temp) <= 10:
    icon = "\uf2cb"  # empty
  elif float(temp) <= 18:
    icon = "\uf2ca"  # quarter
  elif float(temp) <= 22:
    icon = "\uf2c9"  # half
  elif float(temp) <= 26:
    icon = "\uf2c8"  # three-quarter
  elif float(temp) <= 30:
    icon = "\uf2c7"  # full
  elif float(temp) > 30:
    icon = "\uf76a"  # hot
  return icon


def get_battery(value):
  icon = "\uf244"  # empty
  if float(value) <= 10:
    icon = "\uf244"  # empty
  elif float(value) <= 25:
    icon = "\uf243"  # quarter
  elif float(value) <= 50:
    icon = "\uf242"  # half
  elif float(value) <= 75:
    icon = "\uf241"  # three-quarter
  elif float(value) > 75:
    icon = "\uf240"  # full
  return icon


def get_signal(value):
  icon = "\uf690"  # empty
  if float(value) < 56:
    icon = "\uf690"  # full
  elif float(value) <= 65:
    icon = "\uf693"  # three-quarter
  elif float(value) <= 71:
    icon = "\uf692"  # half
  elif float(value) <= 83:
    icon = "\uf691"  # quarter
  elif float(value) <= 86:
    icon = "\uf694"  # empty
  return icon


def get_quality(value):
  icon = "\uf128"  # question
  if float(value) <= 600:
    icon = "\uf762"  # stars
  elif float(value) <= 1000:
    icon = "\uf005"  # star
  elif float(value) <= 1700:
    icon = "\uf5c0"  # half-star
  elif float(value) <= 2500:
    icon = "\uf12e"  # puzzle
  elif float(value) <= 3000:
    icon = "\uf619"  # poop
  elif float(value) > 3000:
    icon = "\uf2fe"  # poo
  return icon


# Get netatmo data
ws = netatmo.WeatherStation({
    'client_id': NA_CLIENT_ID,
    'client_secret': NA_CLIENT_SECRET,
    'username': NA_USERNAME,
    'password': NA_PASSWORD,
    'default_station': NA_DEFAULT_STATION})
ws.get_data()
na_battery = ws.devices[0]["modules"][0]["battery_percent"]
na_signal = ws.devices[0]["modules"][0]["rf_status"]
na_temp_in = round(float(ws.devices[0]["dashboard_data"]["Temperature"]), 1)
na_temp_in_min = round(float(ws.devices[0]["dashboard_data"]["min_temp"]), 1)
na_temp_in_max = round(float(ws.devices[0]["dashboard_data"]["max_temp"]), 1)
na_temp_in_co2 = ws.devices[0]["dashboard_data"]["CO2"]
na_temp_in_noise = ws.devices[0]["dashboard_data"]["Noise"]
na_temp_in_humid = ws.devices[0]["dashboard_data"]["Humidity"]
na_temp_out = round(
    float(ws.devices[0]["modules"][0]["dashboard_data"]["Temperature"]), 1)
na_temp_out_min = round(
    float(ws.devices[0]["modules"][0]["dashboard_data"]["min_temp"]), 1)
na_temp_out_max = round(
    float(ws.devices[0]["modules"][0]["dashboard_data"]["max_temp"]), 1)

# Get openweathermap data
owm_url = f'https://api.openweathermap.org/data/2.5/onecall?lat={OWM_LAT}&lon={OWM_LON}&exclude=hourly,minutely&units={OWM_UNITS}&lang={OWM_LANG}&appid={OWM_APPID}'
owm_response = requests.get(owm_url).json()
current_weather_icon_code = owm_response['current']['weather'][0]['icon']
forecast_weather_icon_code = owm_response['daily'][0]['weather'][0]['icon']
forecast_weather_temp = round(
    float(owm_response['daily'][0]['temp']['day']), 1)
forecast_weather_min = round(float(owm_response['daily'][0]['temp']['min']), 1)
forecast_weather_feel = round(
    float(owm_response['daily'][0]['feels_like']['day']), 1)

# Specify fontawesome icons for owm code
icons = {
    '01d': "\uf185",  # sun
    '02d': "\uf6c4",  # cloud-sun
    '03d': "\uf0c2",  # cloud
    '04d': "\uf744",  # clouds
    '09d': "\uf73f",  # cloud-showers
    '10d': "\uf743",  # cloud-sun-rain
    '11d': "\uf76c",  # thunderstorm
    '13d': "\uf2dc",  # snowflake
    '50d': "\uf74e",  # fog
    '01n': "\uf186",  # moon
    '02n': "\uf6c3",  # cloud-moon
    '03n': "\uf0c2",  # cloud
    '04n': "\uf744",  # clouds
    '09n': "\uf73f",  # cloud-showers
    '10n': "\uf73c",  # cloud-moon-rain
    '11n': "\uf76c",  # thunderstorm
    '13n': "\uf2dc",  # snowflake
    '50n': "\uf74e",  # fog
}
current_weather_icon = icons.get(current_weather_icon_code, "\uf75b")
forecast_weather_icon = icons.get(forecast_weather_icon_code, "\uf75b")

# Set fonts and fontawesome
fontLg = ImageFont.truetype(OPENSANS, 72)
fontMd = ImageFont.truetype(OPENSANS, 32)
fontSm = ImageFont.truetype(OPENSANS, 18)
fasLg = ImageFont.truetype(FAS5, 84)
fasMd = ImageFont.truetype(FAS5, 48)
fasSm = ImageFont.truetype(FAS5, 36)
farLg = ImageFont.truetype(FAR5, 84)
farMd = ImageFont.truetype(FAR5, 48)
farSm = ImageFont.truetype(FAR5, 36)

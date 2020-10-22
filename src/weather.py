#!/usr/bin/python3
# -*- coding:utf-8 -*-
from config import *
from weather_helper import *


try:
  # New PIL
  Himage = Image.new('1', (800, 480), 255)  # 255: clear the frame
  draw = ImageDraw.Draw(Himage)

  # Draw line pattern in background
  draw.line((400, 0, 400, 480), fill=0, width=4)
  draw.line((0, 80, 800, 80), fill=0, width=2)
  draw.line((400, 250, 800, 250), fill=0)

  # Write standard text
  currentTime = time.strftime("%H:%M", time.localtime())
  currentDate = time.strftime("%d.%m.%y", time.localtime())
  dateString = f'{currentDate}'
  timeString = f'Updated: {currentTime}'
  draw.text((60, 40), dateString, font=fontMd, fill=0)
  draw.text((200, 55), timeString, font=fontSm, fill=0)
  draw.text((340, 40), 'IN', font=fontMd, fill=0)
  draw.text((670, 40), 'OUT', font=fontMd, fill=0)

  draw.text((420, 45), text=get_battery(na_battery), font=fasSm, fill=0)
  draw.text((480, 50), f'{na_battery}%', font=fontSm, fill=0)

  draw.text((570, 40), text=get_signal(na_signal), font=fasSm, fill=0)

  # Draw IN values
  # Temperature
  draw.text((65, 100), text=get_thermometer(na_temp_in), font=fasLg, fill=0)
  draw.text((160, 85), f'{na_temp_in}°', font=fontLg, fill=0)

  draw.text((65, 200), '\uf0d7', font=fasMd, fill=0)
  draw.text((100, 200), f'{na_temp_in_min}°', font=fontMd, fill=0)

  draw.text((240, 200), '\uf0d8', font=fasMd, fill=0)
  draw.text((280, 200), f'{na_temp_in_max}°', font=fontMd, fill=0)

  # CO2, Humidity, Noise
  draw.text((60, 250), 'Luftqualität', font=fontMd, fill=0)
  draw.text((60, 300), text=get_quality(na_temp_in_co2), font=fasLg, fill=0)
  draw.text((160, 285), f'{na_temp_in_co2}', font=fontLg, fill=0)
  draw.text((350, 350), 'ppm', font=fontSm, fill=0)
  draw.text((60, 400), '\uf6a8', font=fasMd, fill=0)
  draw.text((120, 400), f'{na_temp_in_noise} dB', font=fontMd, fill=0)
  draw.text((240, 400), '\uf750', font=fasMd, fill=0)
  draw.text((290, 400), f'{na_temp_in_humid}%', font=fontMd, fill=0)

  # Draw OUT values
  # Weather and temperature
  draw.text((420, 100), f'{current_weather_icon}', font=fasLg, fill=0)
  draw.text((520, 85), f'{na_temp_out}°', font=fontLg, fill=0)

  draw.text((430, 200), '\uf0d7', font=fasMd, fill=0)
  draw.text((470, 200), f'{na_temp_out_min}°', font=fontMd, fill=0)

  draw.text((600, 200), '\uf0d8', font=fasMd, fill=0)
  draw.text((640, 200), f'{na_temp_out_max}°', font=fontMd, fill=0)

  # Forecast
  draw.text((420, 250), 'Morgen in Frankfurt', font=fontMd, fill=0)
  draw.text((420, 300), f'{forecast_weather_icon}', font=fasLg, fill=0)
  draw.text((520, 285), f'{forecast_weather_temp}°', font=fontLg, fill=0)

  draw.text((430, 400), '\uf0d7', font=fasMd, fill=0)
  draw.text((470, 400), f'{forecast_weather_min}°', font=fontMd, fill=0)
  draw.text((600, 400), text=get_thermometer(
      forecast_weather_feel), font=fasMd, fill=0)
  draw.text((640, 400), f'{forecast_weather_feel}°', font=fontMd, fill=0)

  # Initialize and clear display
  epd = epd7in5_V2.EPD()
  epd.init()

  # Print everything to the display
  epd.display(epd.getbuffer(Himage))
  time.sleep(2)

  # Sending display to sleep
  epd.sleep()
  epd.Dev_exit()

except IOError as e:
  print(e)

except KeyboardInterrupt:
    print("ctrl + c:")
    epd.epdconfig.module_exit()
    exit()

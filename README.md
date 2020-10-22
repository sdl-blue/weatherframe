# Netatmo Picture Frame

## Introduction and personal "bla bla"
This little home-improvement project was born, because of just one simple fact: I don't want to use my mobile phone, whenever I want to take a look at the information provided by my netatmo weatherstation.

So I asked myself, how would I like to see the information when I'm at home? Things took some time, but during the holidays I saw the solution right before my eyes, while I was reading on my Kindle. Wouldn't it be cool, to have a picture frame with the information right on the wall? With an e-ink display, it would also be possible to show some comics or nice messages...

## What I already had
- Netatmo indoor station incl. outdoor module

## Shopping-list
- Raspberry Pi Zero W (Don't forget micro USB cable and 5V, 2A power adapter)
- Waveshare e-ink display 7.5' V2 incl. HAT
- IKEA picture frame "HOVSTA" 13*18 cm
  - Because this one has a depth of almost 3cm

## My little helpers
- Energy (Thank you Benjamin)
- 2 Really small screws to mount the pi to the rear plate of the frame
- Hammer and Nail
- Keyboard
- Mini-HDMI adapter
- Micro USB to USB Adapter
- 8G micro SD-Card

## Required tools
- A computer
- your own bare hands for...
- a screwdriver
- Time...

## What I did
1. Wait for all packages to arrive
2. Brew some coffee
3. Download NOOBS from RaspberryPi Download-Page and copy to SD-Card
4. Stack all components together
5. Install a no GUI Distro on SD-Card (faster)
6. Configure Updates, SSH, and Firewall
7. Raspi config
   1. Enable SPI interface
8. Download the following software:
   1. GIT
   2. BCM2835 libraries
   3. wiringPi
   4. PIP3
      1. Pillow
      2. numPy
      3. Netatmo
   5. Download Waveshare e-Paper classes
9. Start fiddeling around with PIL
10. Brew some more coffee
11. Keep fiddeling, cause it's somewhat cool to see the results
12. Extend crontab with my personal day and night update-cycle
13. Glue everything together
    1.  Arrange the e-Paper display somewhat central on the frame
    2.  Fixate display with adhesive tape
    3.  Cut hole in rear plate at height of connector
    4.  More adhesive tape to fixate wiring
    5.  Screw pi onto rear plate 
    6.  Connect juice
14. Take hammer and nail, and get that thing on the wall
15. Happy days!

## File organization
My organization looks like this:
- /home/pi
  - weatherpi/
    - fonts/
      - OpenSans.ttf (for clear texts)
      - fas5.otf (fontawesome pro solid >5.10)
      - far5.otf (fontawesome pro regular >5.10)
    - lib/ (for e-Paper communication)
      - epd7in5_V2.py (depending on your display maybe another one)
      - epdconfig.py
      - sysfs_gpio.so
      - sysfs_software_spi.so
    - media/
      - any pictures in correct resolution (800x480) if used as picture frame
    - config.py (all the static variables)
    - image.py (if frame gets used for displaying pictures)
    - weather.py (draws the weatherstation on the e-paper)
    - weather_helper.py (helps to unclutter the weather.py)

## Extend root crontab
```Bash
0 0-4,23 * * *  /usr/bin/python3 /home/pi/weatherpi/weather.py
*/15 5-22 * * * /usr/bin/python3 /home/pi/weatherpi/weather.py
```
The first line updates the display once per hour from 11 pm to 4 am.
The second line updates it every 15 minutes from 5 am to 11 pm.

## Finishing words
Thanks for your interest. If you have any ideas on improving this fancy frame, please go ahead. If you like this project, be kind and say 'thanks', otherwise send me a hateful mail with all the stuff you didn't like.

Cheers!
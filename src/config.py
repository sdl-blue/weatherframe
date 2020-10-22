"""
Configuration of static values
"""
import os, sys

#
# LOCAL CONFIGURATION
#
CWD = os.path.dirname(__file__)
LIBDIR = os.path.join(CWD, 'lib')                 # library directory for epd-configuration
if os.path.exists(LIBDIR):
    sys.path.append(LIBDIR)

FONTDIR = os.path.join(CWD, 'fonts')              # fonts directory
OPENSANS = os.path.join(FONTDIR, "OpenSans.ttf")  # name your display font
FAS5 = os.path.join(FONTDIR, "fas5.otf")          # name your fontawesome solid PRO(!) file
FAR5 = os.path.join(FONTDIR, "far5.otf")          # name your fontawesome regular PRO(!) file

#
# NETATMO CONFIGURATION
# create your ID and SECRET at https://dev.netatmo.com/
#
NA_CLIENT_ID = '01234567890123456789'
NA_CLIENT_SECRET = 'abcdefghijklmnopqrstuvwxyz'
NA_USERNAME = 'username'
NA_PASSWORD = 'password'
NA_DEFAULT_STATION = '70:ee:50:xx:xx:xx'

#
# OPENWEATHERMAP CONFIGURATION
# create your APPID at https://openweathermap.org/api
#
OWM_APPID = '01234567890123456789'
OWM_LAT = '00.1234'
OWM_LON = '0.1234'
OWM_LANG = 'de'
OWM_UNITS = 'metric'

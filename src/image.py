#!/usr/bin/python3
import os
import sys
import time
from PIL import Image

_CWD = os.path.dirname(__file__)
libdir = os.path.join(_CWD, 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
import epd7in5_V2


def displayImage(image):
  """
  Displays the given image to the epd
  """
  try:
    # Initialize and clear display
    epd = epd7in5_V2.EPD()
    epd.init()

    # Print everything to the display
    Dimage = Image.open(image)
    epd.display(epd.getbuffer(Dimage))
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


if __name__ == "__main__":
  if sys.argv[1]:
    image = sys.argv[1]
    displayImage(image)
  else:
    print(f"Please provide an image file as first argument\nE.g.: sudo image.py my_picture.png")
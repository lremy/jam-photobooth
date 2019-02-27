from jam_picamera import JamPiCamera
from auth import CON_KEY, CON_SEC, ACC_TOK, ACC_SEC
from text import get_text
from gpiozero import Button
from time import sleep
import logging
import subprocess
import glob

logger = logging.getLogger('photobooth')
logging.basicConfig(level=logging.INFO)
logger.info("starting")

text = get_text(language='fr')

photo_path = "/home/pi/Pictures"
default_photo = "/home/pi/Pictures/default_photo.jpg"
slideshow_delay = 5
slideshow_base = ["fbi","-a","--noverbose"]

camera = JamPiCamera()
button = Button(14, hold_time=5)

camera.resolution = (1024, 768)
camera.annotate_text_size = 70

def quit():
    logger.info("quitting")
    camera.close()

def countdown(n):
    logger.info("running countdown")
    for i in reversed(range(n)):
        camera.annotate_text = '{}...'.format(i + 1)
        sleep(1)
    camera.annotate_text = None

#capture a photo
def capture_photo():
    camera.annotate_text = text['ready']
    button.wait_for_release()
    logger.info("button released")
    sleep(1)
    countdown(3)
    logger.info("capturing photo")
    photo = camera.capture()
    logger.info("captured photo: {}".format(photo))
    return photo

#run a slideshow with the specified list of photos or default photo if empty list
#returns the proc id
def slideshow(photos):
    logger.info("[slideshow] start")
    if len(photos) > 0:
        logger.info("[slideshow] use list of photos")
        proc = subprocess.Popen(slideshow_base + ["-t",str(slideshow_delay)] + photos)
    else:
        logger.info("[slideshow] use default photo")
        proc = subprocess.Popen(slideshow_base + [default_photo])
    return proc

#list all png files in the specified folder
def list_photos(folder):
    return glob.glob(folder+"/*.png")

button.when_held = quit

photos = list_photos(photo_path)

while True:
    logger.info("start slideshow")
    proc = slideshow(photos)
    camera.stop_preview()
    button.wait_for_press()
    logger.info("button pressed")
    logger.info("terminate slideshow")
    camera.start_preview()
    proc.terminate()
    logger.info("capture photo")
    photo = capture_photo()
    photos = [photo] + photos

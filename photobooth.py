from jam_picamera import JamPiCamera
from auth import CON_KEY, CON_SEC, ACC_TOK, ACC_SEC
from text import get_text
from gpiozero import Button
from time import sleep
import logging
import subprocess

photos = []

logger = logging.getLogger('photobooth')
logging.basicConfig(level=logging.INFO)
logger.info("starting")

text = get_text(language='en')

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

def capture_photos(n):
    """
    Capture n photos in sequence and return a list of file paths
    """
    for pic in range(n):
        #camera.annotate_text = text['photo number'].format(pic + 1, n)
        #sleep(1)
        logger.info("button pressed")
        button.wait_for_release()
        logger.info("button released")
        sleep(1)
        countdown(3)
        logger.info("capturing photo")
        photo = camera.capture()
        logger.info("captured photo: {}".format(photo))
        #photos.append(photo)
    return photo

button.when_held = quit

while True:
    #camera.annotate_text = text['ready']
    logger.info("waiting for button press")
    camera.annotate_text = text['press to capture']
    button.wait_for_press()
    camera.start_preview()
    logger.info("button pressed")
    photo = capture_photos(1)
    photos.append(photo)
    camera.stop_preview
    proc = subprocess.Popen(["fbi","-a",photo])
    sleep(6)
    proc.terminate()
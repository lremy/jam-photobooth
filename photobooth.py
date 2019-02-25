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

def capture_photo():
    """
    Capture n photos in sequence and return a list of file paths
    """
    camera.start_preview()
    button.wait_for_release()
    logger.info("button released")
    countdown(3)
    logger.info("capturing photo")
    photo = camera.capture()
    logger.info("captured photo: {}".format(photo))
    camera.stop_preview()
    proc = subprocess.Popen(["fbi","-a",photo])
    sleep(6)
    proc.terminate()
    
    return photo

button.when_held = quit

while True:
    logger.info("waiting for button press")
    camera.annotate_text = text['press to capture']
    button.wait_for_press()
    logger.info("button pressed")
    photo = capture_photo()
    photos.append(photo)
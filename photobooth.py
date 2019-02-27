from jam_picamera import JamPiCamera
from auth import CON_KEY, CON_SEC, ACC_TOK, ACC_SEC
from text import get_text
from gpiozero import Button
from time import sleep
import logging

logger = logging.getLogger('photobooth')
logging.basicConfig(level=logging.INFO)
logger.info("starting")

text = get_text(language='en')

camera = JamPiCamera()
button = Button(14, hold_time=5)
if CON_KEY:
    twitter = Twython(CON_KEY, CON_SEC, ACC_TOK, ACC_SEC)
else:
    twitter = None

camera.resolution = (1024, 768)
camera.start_preview()
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
    camera.annotate_text = text['press to capture']
    button.wait_for_press()
    logger.info("button pressed")
    button.wait_for_release()
    logger.info("button released")
    sleep(1)
    countdown(3)
    logger.info("capturing photo")
    photo = camera.capture()
    logger.info("captured photo: {}".format(photo))
    return photo

button.when_held = quit

while True:
    photo = capture_photo()

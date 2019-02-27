# Raspberry Jam Photobooth with slideshow

This is an update from the Raspberry Jam Photobooth project.

Features have been changed to the following:

- run a slideshow with all photos or a default photo if no photos have been taken
- when button pressed, stop slideshow and take one photo, the restart slideshow with the last taken photo first

## Requirements

Hardware:

- Raspberry Pi (any model with a camera port)
- Raspberry Pi camera module
- Any kind of standard GPIO push button ([arcade button](https://www.modmypi.com/raspberry-pi/sensors-1061/buttons-and-switches-1098/arcade-button-30mm-translucent-red)
with [quick-connect wire](https://www.modmypi.com/raspberry-pi/sensors-1061/buttons-and-switches-1098/arcade-button-quick-connect-wires-set-of-10-pairs)
reccomended)

Software:

- Picamera
- GPIO Zero
- fbi

## Installation

Start with a Raspbian Stretch desktop image.

1. Connect the camera module and wire your button to GPIO14.

1. Enable the camera module using the Raspberry Pi Configuration Tool in the
main menu, or using `raspi-config` on the command line.

1. Reboot.

1. Open a Terminal window.

1. Install the requirements:

    ```
    sudo apt update
    sudo apt install python3-gpiozero python3-picamera python3-pip fbi git -y
    ```

1. Git clone this repository:

    ```
    git clone https://github.com/lremy/jam-photobooth
    ```

1. Create folder to store photos

    ```
    mkdir /home/pi/Pictures
    ```

1. Enter the project directory and run the photobooth script:

    ```
    python3 photobooth.py
    ```

1. You should see the default image

1. Press the button to capture a photo

1. Press and hold the GPIO button for 5 seconds to close the application.

1. To make the program run on boot, add the following entry using `crontab -e`:

    ```
    @reboot python3 /home/pi/jam-photobooth/photobooth.py &
    ```

## Languages

Simply edit `text.py`, which contains dictionaries of the strings used as camera
text annotations, and add a copy of the English language dictionary `text_en`
below, renaming it as appropriate. Then replace the dictionary values (right
hand side) with the translated equivalents, leaving the keys (left hand side)
the same.

**Please note that the camera firmware does not support non-ASCII characters.**

To select a language, edit the following line in `photobooth.py`:

```python
text = get_text(language='en')
```

Current language support:

- English - `en`
- German (Deutsche) - `de`
- French (Français) - `fr`
- Spanish (Español) - `es`

Pull requests with more language support welcome, as are any improvements to
existing translations (they were all done using Google Translate).

## Modifications

Feel free to edit the code to your own specification. Note that the
`JamPiCamera` class is a slightly modified version of `PiCamera` (as you can
see in `jam_picamera.py`).

You may wish to rotate your picture around 180 degrees if your camera is
upside-down. Simply add `camera.rotation = 180` after `camera = JamPicamera()`.

You can also change the overlay image to another image. Just make sure it's the
same size as whatever the camera resolution is set to (here it is set to
`1024x768`).

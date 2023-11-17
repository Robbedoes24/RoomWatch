from gpiozero import LED, Button
from picamera2 import Picamera2
import threading
import time
import os

# Config
DELAY = 1 # in seconds
BUTTON_PIN = 3
LED_PIN = 27

# Create objects
switch = Button(BUTTON_PIN)
led = LED(LED_PIN)
camera = Picamera2()
stop_event = threading.Event()

# Main function
def main():
  # Stop camera if it is already running
  camera.stop() 
  # Start camera
  camera.start()
  # Wait for camera to start
  time.sleep(2)
  # Loop forever
  while True:
    if switch.is_active:
      # Print message
      print("Switch Active!")
      # Turn on LED if it is off
      if not led.is_active:
        led.on()
      # Get start time in a semi human readable format
      start_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
      # Create directory for images
      save_path = f"RoomWatch/firmware/data_acquisition/data/{start_time}"
      # Create directory if it doesn't exist
      if not os.path.exists(save_path):
        os.makedirs(save_path)
      # Reset count
      count = 0
      # Loop until stop event is set
      while not stop_event.is_set():
        # Capture image
        camera.capture_file(f"{save_path}/image_{count:05d}.jpg")
        # Increment count
        count += 1
        # Check if switch is still active
        if not switch.is_active:
          # Set stop event
          stop_event.set()
          # Close camera object
          camera.close()
        # Wait for delay
        time.sleep(DELAY)
    else:
      # Wait for switch to be pressed
      time.sleep(1)
      # Print message
      print("Waiting for switch to be active...")
      # Turn off LED if it is on
      if led.is_active:
        led.off()

if __name__ == "__main__":
  main()
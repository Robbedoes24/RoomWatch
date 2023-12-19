import os
import cv2
import time
import json
from ultralytics import YOLO
from dotenv import load_dotenv
import paho.mqtt.client as mqtt

# --- Load environment variables ---
load_dotenv()

# --- Setings ---
MQTT_HOST = os.getenv("MQTT_HOST")
MQTT_PORT = int(os.getenv("MQTT_PORT"))
MQTT_TOPIC = os.getenv("MQTT_TOPIC")
ROOM_NAME = os.getenv("ROOM_NAME")

CAMERA_WIDTH = 1920
CAMERA_HEIGHT = 1080
CAMERA_FPS = 1

DETECTION_THRESHOLD = 0.5 # 0.0 - 1.0 (confidence threshold)
DETECTION_FREQUENCY = 5 # seconds (run detection every x seconds, make sure this is higher than the inference time)
DETECTION_PUBLISH_FREQUENCY = 60 # seconds (publish detection average every x seconds, make sure this is a multiple of the DETECTION_FREQUENCY for consistent results)

# --- Pre run config/setup ---
# Load the model
model = YOLO('../../models/best.pt')

# Create a camera object (for image capture)
cap = cv2.VideoCapture(0)
# Edit camera settings
cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)   # Set width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT) # Set height
cap.set(cv2.CAP_PROP_FPS, CAMERA_FPS)             # Set FPS

# Create a MQTT client
client = mqtt.Client()

# --- Functions ---
def amountOfPeople(frame):
  # Run the model on the frame
  results = model.predict(frame, classes=0, conf=DETECTION_THRESHOLD)

  # Return the amount of people detected
  return len(results[0])

def calculateAverage(list):
  # Calculate the average
  sum = 0
  for item in list:
    sum += item
  average = sum / len(list)

  # Return the average as an integer
  return round(average)

def publishDetectionAverage(client, average, start_time):
  # Create the payload
  payload = {
    "uptime": round(time.time() - start_time),
    "people": average
  }

  # Publish the payload to the MQTT broker
  client.publish(MQTT_TOPIC + "/" + ROOM_NAME, json.dumps(payload, indent=4))

# --- Main ---
def main():
  # --- Setup ---
  # Connect to the MQTT broker
  print("Connecting to MQTT broker")
  client.connect(MQTT_HOST, MQTT_PORT)

  # Start loop to run detection every x seconds
  start_time = time.time()
  last_detection_time = start_time
  last_publish_time = start_time

  # Publish initial message to the MQTT broker
  print("Publishing initial message")
  publishDetectionAverage(client, 0, start_time)

  # List with detected amounts
  detection_amounts = []

  # --- Detection loop ---
  print("Starting detection loop")
  while True:
    # Get the current time
    current_time = time.time()

    # continually capture frames from the camera (to prevent the buffer from filling up)
    success, frame = cap.read()

    # If the camera is not working, send error message and exit loop
    if not success:
      # Print error message
      print("Camera malfunction")
      # Send malfuction message to the MQTT broker
      client.publish(MQTT_TOPIC + "/" + ROOM_NAME, "Error: Camera malfunction")
      # Exit the loop
      break

    # --- Detection ---
    # If x seconds have passed since the last detection
    if current_time - last_detection_time > DETECTION_FREQUENCY:
      # Reset the last detection time (before running detection, because it takes time)
      last_detection_time = time.time()

      # Read a frame from the camera
      success, frame = cap.read()

      # Get the amount of people detected
      amount_of_people = amountOfPeople(frame) 

      # Add the amount of people detected to the list
      detection_amounts.append(amount_of_people)

    # --- Publish ---
    # If x seconds have passed since the last publish
    if current_time - last_publish_time > DETECTION_PUBLISH_FREQUENCY:
      # Reset the last publish time
      last_publish_time = time.time()

      # Calculate the average
      average = calculateAverage(detection_amounts)

      # Publish the average to the MQTT broker
      print("\nPublishing average: " + str(average) + " people")
      publishDetectionAverage(client, average, start_time)

      # Clear the list
      detection_amounts.clear()
  
  # --- Cleanup ---
  # Release the camera
  cap.release()

  # Disconnect from the MQTT broker
  print("Disconnecting from MQTT broker")
  client.disconnect()

  # Close the program
  exit()

# --- Run main ---
if __name__ == "__main__":
  main()

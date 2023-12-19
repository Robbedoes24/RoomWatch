# File to capture images every x seconds from the webcam and save them in the same folder
import os
import cv2
import time

# Config
folder = 'images/'
name_base = 'image'
delay = 30 # seconds
camera_width = 1920
camera_height = 1080
camera_fps = 1

# Opens the Video file
cap = cv2.VideoCapture(0)
# Edit camera settings
cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)   # Set width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height) # Set height
cap.set(cv2.CAP_PROP_FPS, camera_fps)             # Set FPS

# Create the folder if it doesn't exist
if not os.path.exists(folder):
    os.makedirs(folder)

# Loop to capture images every x seconds
last_capture_time = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    # Check if delay has passed
    current_time = time.time()
    if current_time - last_capture_time >= delay:
        # save the image
        cv2.imwrite(folder + name_base + str(round(current_time)) + '.jpg', frame)
        # update last capture time
        last_capture_time = current_time
    
cap.release()
cv2.destroyAllWindows()
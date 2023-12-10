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

# Opens the Video file
cap = cv2.VideoCapture(0)
# Edit camera settings
cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)  # Set width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height) # Set height

# Create the folder if it doesn't exist
if not os.path.exists(folder):
    os.makedirs(folder)

# Loop to capture images every x seconds
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    # time in seconds since epoch (to add to the name)
    current_time = round(time.time())
    # save the image
    cv2.imwrite(folder + name_base + str(current_time) + '.jpg', frame)
    # wait x seconds
    time.sleep(delay)
    
cap.release()
cv2.destroyAllWindows()
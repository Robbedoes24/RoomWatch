import cv2
import time
from ultralytics import YOLO

# --- Setings ---

CAMERA_WIDTH = 1920
CAMERA_HEIGHT = 1080
CAMERA_FPS = 1

INFERENCE_FREQUENCY = 5 # seconds (run inference every x seconds, make sure this is higher than the inference time)
DETECTION_THRESHOLD = 0.80 # 0.0 - 1.0 (confidence threshold)

# --- Pre run config/setup ---
# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

# Create a camera object (for image capture)
cap = cv2.VideoCapture(0)
# Edit camera settings
cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)   # Set width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT) # Set height
cap.set(cv2.CAP_PROP_FPS, CAMERA_FPS)             # Set FPS


# --- Main ---
def main():
  previous_frame_time = 0
  # Loop through the video frames
  while cap.isOpened():
    # Get the current time
    current_frame_time = time.time()

    # Read a frame from the video
    success, frame = cap.read()

    if success:
      # Only run inferance every x seconds
      if current_frame_time - previous_frame_time >= INFERENCE_FREQUENCY:
        # Update the previous frame time
        previous_frame_time = current_frame_time
        
        # Run YOLOv8 inference on the frame
        results = model.predict(frame, classes=0, conf=DETECTION_THRESHOLD)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("Inference", annotated_frame)

      # Break the loop if 'q' is pressed
      if cv2.waitKey(1) & 0xFF == ord("q"):
          break
    else:
       # Break the loop if the end of the video is reached
      break

  # Release the video capture object and close the display window
  cap.release()
  cv2.destroyAllWindows()
    

# --- Run ---
if __name__ == "__main__":
  main()
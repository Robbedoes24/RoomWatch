from ultralytics import YOLO
import os
from PIL import Image

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

model = YOLO('yolov8n.yaml')

results = model.train(data='config.yaml', epochs=100)         #100 for finaal training

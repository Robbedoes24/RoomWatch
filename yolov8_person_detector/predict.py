import os
from PIL import Image
from ultralytics import YOLO


os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
model_path = os.path.join('.', 'runs', 'detect', 'train8', 'weights', 'last.pt')

# Load a model
model = YOLO(model_path)  # load a custom model

im1 = Image.open("img/test.jpg")
results = model.predict(source=im1, save=True)  # save plotted images   # save predictions as labels       show_labels=False, show_conf=False,

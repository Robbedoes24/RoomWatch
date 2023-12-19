# RoomWatch

## About

RoomWatch is an research project to create a system that can monitor a room and detect if there are people present in the room.
The system is based on a Raspberry Pi with a webcam. The webcam is used to take pictures of the room.
These pictures are then analyzed on the Raspberry Pi using an ai model to detect if there are people present in the room.
The Raspberry Pi then sends a simple mqtt message to an mqtt broker containing how many people are present in the room.

## File structure

The project has the following file structure:

```
.
├── firmware
│   ├── data_acquisition
│   ├── detection
│   └── testing
├── frontend
├── models
└── training
```

The `firmware` directory contains the code that runs on the Raspberry Pi.
It contains three subdirectories:

- `data_acquisition`: This directory contains the code that is used to gather image data for training the model.
- `detection`: This directory contains the code that is used to detect people in the images.
- `testing`: This directory contains the code that is used to test the camera position and have a visual representation of the detection.

The `frontend` directory contains the code that is used to display the data that is gathered by the Raspberry Pi.

The `models` directory contains the trained models that are used to detect people in the images.

The `training` directory contains the code that is used to train the models.

## Firmware

### Installation

First, you need to install the Raspberry Pi OS on your Raspberry Pi.
You can find the installation instructions [here](https://www.raspberrypi.org/documentation/installation/installing-images/).

After you have installed the Raspberry Pi OS, you need to install the dependencies for the RoomWatch system.
Depending on which part of the system you want to use, you need to install different dependencies.
Each part of the firmware has its own requirements file.

To install the dependencies for the data acquisition part, run the following command:

```bash
pip3 install -r firmware/data_acquisition/requirements.txt
```

To install the dependencies for the detection part, run the following command:

```bash
pip3 install -r firmware/detection/requirements.txt
```

To install the dependencies for the testing part, run the following command:

```bash
pip3 install -r firmware/testing/requirements.txt
```

Now you have installed all the dependencies for the RoomWatch system.

### Usage

> [!NOTE]
> When running the python scripts make sure you are in the correct directory.
> The scripts use relative paths to access the models and if you are not in the directory where the script is located, the script will not be able to find the models.

#### Data acquisition

To use the data acquisition part of the firmware, you need to run the `capture.py` script.
This script takes a picture of the room and saves it to the `data_acquisition/images` directory.
Before you run the script, you can configure the script by changing the values of the variables at the top of the script.

You can run the script by running the following command:

```bash
cd firmware/data_acquisition
python3 capture.py
```

#### Detection

To use the detection part of the firmware, you need to run the `detect.py` script.
This script takes a picture of the room and detects if there are people present in the room.
Before you can run the script, you need to copy the `copy.env` file to a new file called `.env` and fill in the values in the `.env` file.
Then you can configure the script by changing the values of the variables at the top of the script, this is optional.

You can run the script by running the following command:

```bash
cd firmware/detection
python3 detect.py
```

#### Testing

To use the testing part of the firmware, you need to run the `test.py` script.
This script takes a picture of the room and shows the picture with the detected people.
Before you run the script, you can configure the script by changing the values of the variables at the top of the script.

You can run the script by running the following command:

```bash
cd firmware/testing
python3 test.py
```

### Detection

Here is some more information about the detection part of the firmware.
The detection script has 2 delays, one for the time between taking pictures and one for the time between sending the mqtt message.

The delay between taking pictures is set to 5 seconds by default.
This means that the script will take a picture every 5 seconds and then analyze the picture.

The delay between sending the mqtt message is set to 60 seconds by default.
This means that the script will send a mqtt message every 60 seconds containing the average number of people present in the room for the last 60 seconds.

The message that is sent to the mqtt broker is a simple json string containing the number of people present in the room and the time the script has been running.
The message is formatted as follows: `{"uptime": <uptime>, "people": <people>}`

## Frontend

### Install the dependencies

```bash
yarn
# or
npm install
```

### Start script for mqtt scrapping

```bash
node mqttScript.js
```

### Start the app in development mode (hot-code reloading, error reporting, etc.)

```bash
quasar dev
```

## Models

The models directory contains the trained models that are used to detect people in the images.
The models are trained using transfer learning from [YOLOv8](https://docs.ultralytics.com/).

## Training

??

Fitup Pro is a real-time motion detection game designed to encourage exercise and workouts, developed using Python Unity 3D.
# Push-Up Counter

This project, developed during the Smart India Hackathon (SIH) 2023, utilizes Python to count push-ups using the MediaPipe library for pose detection. The program captures video from the webcam, detects push-up movements, and counts the number of push-ups performed, sending this count over UDP to a specified server.

## Features

- Real-time push-up counting using computer vision.
- Pose detection using MediaPipe.
- UDP communication for sending push-up counts.
- Simple and user-friendly interface.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe

You can install the required libraries using pip:

```bash
pip install opencv-python mediapipe

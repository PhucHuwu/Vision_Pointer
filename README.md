# Eye Control Pointer

A computer vision application that allows you to control your mouse cursor using eye movements and perform clicks by blinking.

## Overview

Eye Control Pointer uses facial landmark detection to track eye movements and translate them into mouse cursor movements on your screen. The application creates a virtual trackpad that follows your face, allowing you to move the cursor by looking in different directions within this trackpad area. It also detects eye blinks to trigger mouse clicks.

## Features

- **Eye-Controlled Mouse Movement**: Move your cursor by looking in different directions
- **Blink to Click**: Perform a mouse click by blinking your left eye
- **Real-time Visualization**: See the tracking points and virtual trackpad overlay
- **Adjustable Sensitivity**: Customize the size of the virtual trackpad area

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- MediaPipe
- PyAutoGUI
- PIL (Python Imaging Library)

## Installation

1. Clone this repository or download the source code
2. Install the required dependencies:

```bash
pip install opencv-python mediapipe pyautogui pillow
```

## Usage

1. Run the script:

```bash
python eye_control_pointer.py
```

2. Position yourself in front of your webcam
3. Keep your head relatively stable
4. A blue rectangle will appear on the screen - this is your virtual trackpad
5. Move your eyes within this trackpad to control the mouse cursor
6. Blink your left eye to perform a mouse click
7. Press `ESC` to exit the application

## How It Works

The application uses MediaPipe's Face Mesh to detect facial landmarks, particularly around the eyes:

1. The webcam captures your face
2. Face landmarks are detected and tracked in real-time
3. A virtual trackpad is created based on your eye position
4. Eye movements within this trackpad are translated to cursor movements
5. The application detects left eye blinks by measuring the distance between upper and lower eyelid landmarks
6. When a blink is detected, a mouse click is triggered

## Customization

You can adjust the sensitivity and behavior by modifying these parameters in the code:

- `ratio = 0.15`: Controls the size of the virtual trackpad (smaller value = more sensitive)
- Eye blink threshold: Adjust the condition `(left_eye[0].y - left_eye[1].y < 0.01)` to make blinking detection more or less sensitive

## Troubleshooting

- **Poor tracking**: Ensure you have adequate lighting and your face is clearly visible
- **Unresponsive clicks**: Adjust the blink threshold for your specific eye shape
- **Cursor jumps**: Try keeping your head more stable or increase the tracking area

## License

This project is released under the MIT License.

## Acknowledgements

This project uses the MediaPipe face mesh solution developed by Google.

# Eye Control Pointer

## Introduction
Eye Control Pointer is an application that uses OpenCV, MediaPipe, and PyAutoGUI to control the mouse cursor using eye movements. The program utilizes facial recognition and eye tracking to move the cursor and perform click actions by blinking.

## Features
- **Cursor Movement**: Tracks eye movements and moves the mouse cursor accordingly.
- **Click Action**: Performs a mouse click by blinking.
- **Face Tracking**: Uses MediaPipe Face Mesh for real-time face detection and tracking.

## Installation
### System Requirements
- Python 3.7+
- Webcam
- Operating System: Windows, macOS, Linux

### Install Dependencies
Run the following command to install the required libraries:
```bash
pip install opencv-python mediapipe pyautogui pillow
```

## Usage
1. Run the program using:
   ```bash
   python eye_control.py
   ```
2. Ensure the webcam is enabled and your face is clearly visible.
3. **Move your eyes** to control the mouse cursor.
4. **Blink your left eye** to perform a click action.
5. Press `Esc` to exit the program.

## Code Structure
- `face_mesh_landmarks`: Initializes the face recognition model from MediaPipe.
- `cap`: Opens the webcam to capture image data.
- `pyautogui.size()`: Retrieves the screen dimensions.
- Main loop:
  - Reads and processes the webcam image.
  - Detects eyes and mouth.
  - Moves the cursor based on eye position.
  - Blinks to perform a click action.

## Notes
- The program requires access to the webcam.
- Accuracy may be affected by lighting conditions.
- If the face is not detected, ensure proper positioning and a clear view of the webcam.

## Contribution
If you would like to improve or contribute to the project, please open a pull request or contact me via GitHub.


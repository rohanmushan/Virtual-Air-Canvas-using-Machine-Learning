# Air Canvas Using OpenCV

Air Canvas is a computer vision application that allows you to draw in the air using hand gestures captured by your webcam. This project combines OpenCV for image processing with MediaPipe for hand tracking to create an interactive drawing experience.

## Features

- Draw on a virtual canvas using natural hand movements
- Toggle drawing on/off with pinch gestures
- Color selection through an interactive color picker
- Adjustable brush sizes (use '+' and '-' keys)
- Canvas clearing function
- Save your drawings as PNG files
- Smooth drawing with optimized tracking

## Demo

The project creates drawings like these:
- Sample drawings are saved as PNG files in the project root

## Requirements

- Python 3.8+
- OpenCV
- MediaPipe
- NumPy
- tkinter (for color picker UI)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/Air-Canvas-using-OpenCV.git
   cd Air-Canvas-using-OpenCV
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the main application:
   ```
   python code/AirCanvas.py
   ```

2. UI Controls:
   - Hold your hand up to the webcam
   - Pinch your thumb and index finger together to start/stop drawing
   - Use the on-screen buttons to:
     - CLEAR: Reset the canvas
     - COLOR: Open color picker to change drawing color
     - SAVE: Save your drawing as a PNG file
   - Keyboard controls:
     - '+' or '=': Increase brush size
     - '-': Decrease brush size
     - 'q': Quit the application

## How It Works

1. The webcam captures video input
2. MediaPipe detects hand landmarks in real-time
3. The application tracks the position of the index fingertip
4. A pinch gesture (distance between index and thumb) toggles drawing mode
5. When drawing is enabled, the movement path is drawn on both the display and persistent canvas
6. On-screen buttons provide additional functionality

## Project Structure

- `code/AirCanvas.py`: Main application code
- `code/color_palette.py`: Color picker interface
- `assets/`: Directory for project assets
- Generated PNG files: Saved drawings

## Troubleshooting

- Ensure your webcam is properly connected and has permissions
- Adequate lighting improves hand detection
- If hand tracking is unstable, try adjusting your distance from the camera
- For color picker issues, make sure tkinter is properly installed

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Thanks to the OpenCV and MediaPipe teams for their excellent libraries 

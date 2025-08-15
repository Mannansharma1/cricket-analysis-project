# AI-Powered Cricket Cover Drive Analysis

This project provides real-time biomechanical analysis of a cricket cover drive from a video. It uses OpenCV for video processing and MediaPipe for pose estimation to evaluate the shot based on key metrics.

## Setup

1.  **Clone the repository or download the files.**
2.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # OR
    venv\Scripts\activate   # On Windows
    ```
3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Download the video** for analysis and save it in the root project directory as `input_video.mp4`.

## How to Run

With the virtual environment activated, run the main script from the terminal:

```bash
python cover_drive_analysis_realtime.py
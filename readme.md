# AI-Powered Cricket Cover Drive Analysis 🏏

This project provides real-time biomechanical analysis of a cricket cover drive from a video. It uses OpenCV for video processing and Google's MediaPipe for pose estimation to evaluate the shot based on key metrics. The project is deployed as a Streamlit web application.

**[➡️ View the Live Deployed App Here](https://your-streamlit-app-url.streamlit.app/)**

---

## Features
* **Real-Time Pose Estimation:** Tracks the batter's key body joints frame-by-frame.
* **Biomechanical Metrics:** Calculates critical angles and alignments, including elbow elevation, spine lean, and head position.
* **Live Video Overlays:** Generates an annotated video with the pose skeleton and real-time metric feedback.
* **Final Shot Evaluation:** Provides a multi-category score and actionable feedback on the shot's quality.
* **Interactive Web App:** Allows users to upload any video for analysis via a simple Streamlit interface.

---

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
---

## How to Run Locally

1. **Download a video** for analysis and save it in the root project directory.
2. With the virtual environment activated, run the Streamlit app from the terminal:

    ```bash
    streamlit run cover_drive_analysis_realtime.py
    ```
---

## Deliverables

Running the script locally will generate the following outputs in the `/output` folder:
* `/output/annotated_video.mp4`: The original video with pose overlays and real-time metrics.
* `/output/evaluation.json`: A summary of the shot's performance with scores and feedback.

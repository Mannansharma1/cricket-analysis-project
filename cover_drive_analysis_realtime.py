import cv2
import mediapipe as mp
import numpy as np
import json
import math
import os
import streamlit as st # <-- NEW: Import Streamlit
import tempfile # <-- NEW: To handle temporary file from Streamlit

# (Your calculate_angle function stays exactly the same)
def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    if angle > 180.0:
        angle = 360 - angle
    return angle

# --- The analysis logic is now inside this function ---
def analyze_cover_drive(video_path):
    # Initialize MediaPipe Pose
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()

    # --- NEW: Data collection list ---
    analysis_data = []

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        st.error("Error: Could not open video file.")
        return None, None

    # Get video properties for output
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    # --- NEW: Save output video to a temporary file ---
    output_video_path = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4').name
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Use a common codec
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_count += 1
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # (The landmark extraction and drawing logic is the same)
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            # ... (all the code to get shoulder, elbow, etc.)
            
            # --- Data Analysis: Collect metrics for each frame ---
            elbow_angle = calculate_angle(...) # your existing calculation
            spine_lean = ... # your existing calculation
            head_knee_distance = ... # your existing calculation

            # Store the data
            analysis_data.append({
                "frame": frame_count,
                "elbow_angle": elbow_angle,
                "spine_lean": spine_lean,
                "head_knee_distance": head_knee_distance
            })

            # ... (all your cv2.putText and mp_drawing.draw_landmarks code)
        
        out.write(image)

    cap.release()
    out.release()
    pose.close()

    # --- Data Analysis: Create a dynamic evaluation from collected data ---
    # Example: Find the maximum elbow angle achieved during the shot
    max_elbow_angle = 0
    if analysis_data:
        max_elbow_angle = max(d['elbow_angle'] for d in analysis_data)

    # Make feedback dynamic based on data
    swing_score = 8 if max_elbow_angle > 150 else 5
    swing_feedback = f"Good high elbow, reached {int(max_elbow_angle)} degrees." if swing_score >= 8 else "Elbow could be higher for better swing path."

    evaluation_summary = {
        "swing_control": {"score": swing_score, "feedback": swing_feedback},
        # ... (you can make other scores dynamic too)
    }

    return output_video_path, evaluation_summary


# --- NEW: This is the main part of the Streamlit App ---
st.title('Athlete Rise - Cricket Cover Drive Analysis 🏏')
st.write("Upload a video of a cover drive to get an AI-powered analysis of the shot.")

uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    # Save the uploaded file to a temporary path
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    
    st.video(tfile.name)
    
    if st.button('Analyze Shot'):
        with st.spinner('Processing video... This might take a moment.'):
            # Run the analysis on the uploaded video
            annotated_video_path, evaluation = analyze_cover_drive(tfile.name)

            if annotated_video_path and evaluation:
                st.success('Analysis Complete!')
                
                # Display the annotated video
                st.subheader("Annotated Video")
                video_file = open(annotated_video_path, 'rb')
                video_bytes = video_file.read()
                st.video(video_bytes)
                
                # Display the evaluation
                st.subheader("Shot Evaluation")
                st.json(evaluation)

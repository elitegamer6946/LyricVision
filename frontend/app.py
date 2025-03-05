import sys
import os
import requests

# Add the backend directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "backend"))

# Now you can import music_analysis
from music_analysis import extract_beats

# Streamlit app
import streamlit as st

st.title("AI Music Video Generator")

# Upload song
uploaded_file = st.file_uploader("Upload a song", type=["mp3"])

if uploaded_file:
    st.audio(uploaded_file)
    if st.button("Generate Video"):
        with st.spinner("Generating..."):
            # Send file to backend
            files = {"file": uploaded_file}
            try:
                response = requests.post("http://localhost:5001/process", files=files, timeout=10)
                response.raise_for_status()  # Raise an error for bad status codes
                response_data = response.json()

                if response_data.get("status") == "success":
                    video_path = response_data["video_path"]
                    st.video(video_path)
                else:
                    st.error(f"Backend error: {response_data.get('message', 'Unknown error')}")
            except requests.exceptions.RequestException as e:
                st.error(f"Failed to connect to the backend: {e}")


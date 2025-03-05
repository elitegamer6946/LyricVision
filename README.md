# LyricVision: AI-Powered Music Video Generator

LyricVision is an AI-powered application that generates music videos from song lyrics and beats. It uses OpenAI Whisper for lyrics extraction, librosa for beat and tempo analysis, and Zeroscope for video generation.

## Features
- **Lyrics Extraction**: Automatically extracts lyrics from uploaded songs using OpenAI Whisper.
- **Beat and Tempo Analysis**: Analyzes the song's beats and tempo using librosa.
- **Visual Prompt Generation**: Generates a visual prompt based on the lyrics using GPT-Neo.
- **Video Generation**: Creates a music video synchronized with the song's beats using Zeroscope.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/LyricVision.git
   cd LyricVision
   
2. Install the dependencies:
   ```bash
   pip install -r backend/requirements.txt

3. Run the backend:
   ```bash
   python backend/app.py
   
4. Run the frontend:
   ```bash
   streamlit run frontend/app.py


# Usage
1.Upload a song in the frontend.
2.The backend will process the song, extract lyrics, and generate a music video.
3.Download the generated video from the output directory.

# Technologies Used
- **OpenAI Whisper**: For lyrics extraction.
- **librosa**: For beat and tempo analysis.
- **GPT-Neo**: For visual prompt generation.
- **Zeroscope**: For video generation.
- **Flask**: Backend server.
- **Streamlit**: Frontend interface.

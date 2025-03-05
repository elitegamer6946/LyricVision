from flask import Flask, request, jsonify
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "backend"))


from music_analysis import extract_beats
from music_analysis import transcribe_audio
from lyrics_analysis import generate_visual_prompt
from video_generation import generate_video

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process_song():
    try:
        # Get uploaded file
        file = request.files["file"]
        file_path = f"assets/input_songs/{file.filename}"
        file.save(file_path)

        # Extract beats and tempo
        tempo, beat_times = extract_beats(file_path)

        # Transcribe audio to lyrics using Whisper
        lyrics = transcribe_audio(file_path)

        if not lyrics:
            return jsonify({"status": "error", "message": "Failed to transcribe lyrics"}), 500

        # Generate visual prompt
        prompt = generate_visual_prompt(lyrics)

        # Generate video synchronized with beats
        output_path = f"assets/output_videos/{file.filename.replace('.mp3', '.mp4')}"
        generate_video(prompt, beat_times, output_path)

        return jsonify({"status": "success", "video_path": output_path})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    os.makedirs("assets/input_songs", exist_ok=True)
    os.makedirs("assets/output_videos", exist_ok=True)
    app.run(debug=True, port=5001)
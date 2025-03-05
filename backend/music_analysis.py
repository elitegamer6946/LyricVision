import librosa
from pydub import AudioSegment
import whisper


def convert_to_wav(audio_path, output_path="output.wav"):
    # Load the audio file
    audio = AudioSegment.from_file(audio_path)
    # Export as WAV
    audio.export(output_path, format="wav")
    return output_path

def transcribe_audio(file_path):
    model = whisper.load_model("base")  # Use "small", "medium", or "large" for better accuracy
    result = model.transcribe(file_path)
    return result["text"]


def extract_beats(audio_path):
    # Convert to WAV format
    wav_path = convert_to_wav(audio_path)

    # Load audio file
    y, sr = librosa.load(wav_path, sr=None, mono=True, res_type='kaiser_fast')

    # Extract tempo and beats
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    return tempo, beat_times


# Example usage
if __name__ == "__main__":
    audio_path = "assets/input_songs/song.mp3"
    tempo, beat_times = extract_beats(audio_path)
    print(f"Tempo: {tempo} BPM")
    print(f"Beats: {beat_times}")
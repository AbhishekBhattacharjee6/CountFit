import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import os

# Load Whisper model (this may take a few seconds)
print("🔄 Loading Whisper model...")
try:
    model = whisper.load_model("base")
    print("✅ Whisper model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading Whisper model: {e}")
    exit()

# Recording settings
SAMPLERATE = 44100  # Sample rate for recording
DURATION = 5  # Record for 5 seconds
TEMP_FILENAME = "temp_audio.wav"

print("🎤 Speak now... (Recording for 5 seconds)")

try:
    # Record audio from microphone
    audio_data = sd.rec(int(SAMPLERATE * DURATION), samplerate=SAMPLERATE, channels=1, dtype=np.int16)
    sd.wait()  # Wait until recording is finished
    print("✅ Recording complete!")
    
    # Save recorded audio
    wav.write(TEMP_FILENAME, SAMPLERATE, audio_data)

    # Ensure file was saved
    if not os.path.exists(TEMP_FILENAME):
        print("❌ Failed to save the audio file.")
        exit()

    print("📝 Transcribing...")
    result = model.transcribe(TEMP_FILENAME)

    # Get the transcribed text
    transcribed_text = result["text"].lower()
    print("\nTranscription:", transcribed_text)

    # Check if "start" is detected
    if "start" in transcribed_text:
        print("✅ Whisper working properly!")
    else:
        print("❌ Whisper did not detect 'start'. Try again.")

except Exception as e:
    print(f"❌ Error: {e}")


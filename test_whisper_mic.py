import whisper
import speech_recognition as sr
import pyttsx3

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

print("🔄 Loading Whisper model...")
model = whisper.load_model("base")  # You can change to "small", "medium", etc.
print("✅ Whisper model loaded successfully!")

# Initialize the recognizer
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Say something...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

    print("🛠️ Processing audio...")
    try:
        # Save recorded audio to a temporary file
        with open("temp_audio.wav", "wb") as f:
            f.write(audio.get_wav_data())

        # Transcribe with Whisper
        result = model.transcribe("temp_audio.wav")
        transcription = result["text"]
        
        print("📝 Whisper Transcription:", transcription)

        # Speak out the transcription
        speak(f"Model worked successfully! You said: {transcription}")

    except Exception as e:
        print("❌ Error:", str(e))
        speak("An error occurred while processing the audio.")


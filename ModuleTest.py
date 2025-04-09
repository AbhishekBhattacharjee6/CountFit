from elevenlabs import generate, Voice, VoiceSettings, set_api_key
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO

# Set your API key
set_api_key("sk_c196362448bd560248ca13fdbea016f28955f01e12e02456")

# Generate audio from ElevenLabs
audio = generate(
    text="Your ElevenLabs voice is now working perfectly, Abhishek!",
    voice=Voice(
        voice_id="EaBs7G1VibMrNAuz2Na7",  #Monica
        settings=VoiceSettings(stability=0.75, similarity_boost=0.75)
    )
)

# Convert MP3 byte stream to audio segment
audio_segment = AudioSegment.from_file(BytesIO(audio), format="mp3")

# Play the audio
print("🔊 Playing clean human voice...")
play(audio_segment)
print("✅ Done!")




from elevenlabs import stream
from elevenlabs.client import ElevenLabs
client = ElevenLabs(
  api_key="sk_c196362448bd560248ca13fdbea016f28955f01e12e02456",
)
audio_stream = client.text_to_speech.convert_as_stream(
    text="This is a test",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2"
)
# option 1: play the streamed audio locally
stream(audio_stream)
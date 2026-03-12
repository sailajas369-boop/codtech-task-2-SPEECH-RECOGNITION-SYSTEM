import sounddevice as sd
import soundfile as sf
import speech_recognition as sr

# === RECORD AUDIO ===
fs = 16000  # Must be 16000 Hz for Google recognizer
seconds = 5
filename = "my_audio.wav"

print("🎤 Recording started... Speak now!")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()
print("✅ Recording complete.")

# Save in PCM WAV format (correct format!)
sf.write(filename, recording, fs, subtype='PCM_16')

# === TRANSCRIBE AUDIO ===
recognizer = sr.Recognizer()

with sr.AudioFile(filename) as source:
    print("🧠 Transcribing audio...")
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio)
    print("📝 Transcribed Text:", text)
except sr.UnknownValueError:
    print("❌ Could not understand the audio.")
except sr.RequestError as e:
    print("⚠️ Could not request results from Google: {0}".format(e))

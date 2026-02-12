import os
import time
from gtts import gTTS

def generate_audio(topic, level, text):
    folder = 'static'
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Use a unique timestamp to prevent "File in Use" errors
    filename = f"audio_{int(time.time())}.mp3"
    file_path = os.path.join(folder, filename)

    try:
        # Clean up old audio files in the folder to save space
        for old_file in os.listdir(folder):
            if old_file.endswith(".mp3"):
                try: os.remove(os.path.join(folder, old_file))
                except: continue

        tts = gTTS(text=text, lang='en')
        tts.save(file_path)
        return filename 
    except Exception as e:
        print(f"Audio Error: {e}")
        return None
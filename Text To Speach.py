# pip install gtts
from gtts import gTTS
import os


language = "en"


audio = gTTS(text="hello world",lang=language, slow=False)

audio.save("1.wav")
os.system("1.wav")

#this script is perfectly running Coqui tts on terminal

import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Text to speech to a file
tts.tts_to_file(text="My name is Bitan Paul. I am an artificial intelligence specialist.", speaker_wav="/content/bark_voices/speaker/female.wav", language="en", file_path="output.wav")
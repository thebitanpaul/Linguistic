#this script is perfectly running the gtts on terminal

import os
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def text_to_speech(text):
    # Generate speech
    tts = gTTS(text=text, lang='en')
    audio_file = "output.mp3"
    tts.save(audio_file)

    # Convert the audio file to a format pydub can play
    audio_segment = AudioSegment.from_file(audio_file, format="mp3")

    # Play the audio
    play(audio_segment)

    # Clean up the audio file
    os.remove(audio_file)

if __name__ == "__main__":
    text_input = input("Enter text to convert to speech: ")
    if text_input:
        text_to_speech(text_input)
    else:
        print("Please enter some text to convert.")

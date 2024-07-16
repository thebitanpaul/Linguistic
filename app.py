from flask import Flask, request, send_file, render_template, jsonify, url_for
import torch
from TTS.api import TTS
from gtts import gTTS
import os

# Agree to Coqui TTS license terms
os.environ["COQUI_LICENSE"] = "Otherwise, I agree to the terms of the non-commercial CPML: https://coqui.ai/cpml"

app = Flask(__name__, static_folder='static')

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Define available voices
available_voices = [
    {"id": "en", "name": "English"},
    {"id": "en-au", "name": "English (Australia)"},
    {"id": "en-ca", "name": "English (Canada)"},
    {"id": "en-gb", "name": "English (UK)"},
    {"id": "en-in", "name": "English (India)"},
    {"id": "fr", "name": "French"},
    {"id": "fr-ca", "name": "French (Canada)"},
    {"id": "es", "name": "Spanish"},
    {"id": "es-es", "name": "Spanish (Spain)"},
    {"id": "es-mx", "name": "Spanish (Mexico)"},
    {"id": "de", "name": "German"},
    {"id": "it", "name": "Italian"},
    {"id": "pt", "name": "Portuguese"},
    {"id": "pt-br", "name": "Portuguese (Brazil)"},
    {"id": "nl", "name": "Dutch"},
    {"id": "ru", "name": "Russian"},
    {"id": "ja", "name": "Japanese"},
    {"id": "zh-cn", "name": "Chinese (Simplified)"},
    {"id": "zh-tw", "name": "Chinese (Traditional)"},
    {"id": "ko", "name": "Korean"},
    {"id": "ar", "name": "Arabic"}
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/tts', methods=['GET', 'POST'])
def tts_route():
    if request.method == 'POST':
        text = request.form['text']
        file = request.files['file']
        language = request.form.get('language', 'en')

        # Save the uploaded wav file
        wav_path = "sample_uploaded.wav"
        file.save(wav_path)

        # Generate TTS
        output_path = "Ai_cloned_voice.wav"
        tts.tts_to_file(text=text, speaker_wav=wav_path, language=language, file_path=output_path)

        return send_file(output_path, as_attachment=True, mimetype="audio/wav")
    else:
        return render_template('index.html')

@app.route('/gtts/voices')
def gtts_voices():
    return jsonify({"voices": available_voices})

@app.route('/gtts', methods=['GET', 'POST'])
def gtts_route():
    if request.method == 'POST':
        text = request.form['text']
        voice = request.form.get('voice', 'en')

        if text:
            # Ensure the static directory exists
            if not os.path.exists('static'):
                os.makedirs('static')

            # Generate speech
            tts = gTTS(text=text, lang=voice)
            audio_file = "static/output.mp3"
            tts.save(audio_file)

            return jsonify({"audio_url": url_for('static', filename='output.mp3')})
        else:
            return jsonify({"error": "Please enter some text to convert."}), 400
    else:
        return render_template('gtts.html')


if __name__ == '__main__':
    app.run(debug=True)

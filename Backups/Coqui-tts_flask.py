#this script is perfectly integrating Coqui tts with flask

from flask import Flask, request, send_file, render_template
import torch
from TTS.api import TTS
import os

app = Flask(__name__)

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tts', methods=['POST'])
def tts_route():
    text = request.form['text']
    file = request.files['file']
    language = request.form.get('language', 'en')

    # Save the uploaded wav file
    wav_path = "uploaded.wav"
    file.save(wav_path)

    # Generate TTS
    output_path = "output.wav"
    tts.tts_to_file(text=text, speaker_wav=wav_path, language=language, file_path=output_path)

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)


#html for this script is as fllow
# <!DOCTYPE html>
# <html lang="en">

# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Text to Speech</title>
# </head>

# <body>
#     <h1>Text to Speech</h1>
#     <form action="/tts" method="post" enctype="multipart/form-data">
#         <label for="text">Text:</label>
#         <input type="text" id="text" name="text" required><br><br>
#         <label for="file">Upload WAV File:</label>
#         <input type="file" id="file" name="file" accept=".wav" required><br><br>
#         <label for="language">Language:</label>
#         <input type="text" id="language" name="language" value="en"><br><br>
#         <input type="submit" value="Submit">
#     </form>
# </body>

# </html>
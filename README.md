# Linguistic: Real-Time Text to Speech and Voice Cloning AI

Welcome to the **Linguistic** project! This project leverages multiple TTS (Text to Speech) models, including Google Text to Speech (gTTS), Bark TTS, and Coqui TTS, to provide simple real-time text-to-speech generation and extensive voice cloning capabilities for free.

![Linguistic](https://github.com/user-attachments/assets/0c848569-db29-43d6-a9cf-9354520fd695)

## Features

- **Real-Time Text to Speech**: Convert text to speech in real-time using Google TTS.
- **Generative Text to Speech**: Generate high-quality speech using Bark and Coqui TTS models.
- **Voice Cloning**: Clone voices by providing a sample `.wav` file.
- **User-Friendly Interface**: Intuitive web interface to easily interact with the TTS models.

## Technology Stack

- **Backend**: Flask, PyTorch
- **Frontend**: HTML, CSS, JavaScript
- **TTS Models**: Google TTS (gTTS), Bark TTS, Coqui TTS

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/linguistic.git
    cd linguistic
    ```

2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Download TTS Models**:
    Download and place the required TTS models (Bark TTS and Coqui TTS) in the appropriate directory.

## Usage

1. **Run the Flask Application**:
    ```bash
    flask run
    ```

2. **Access the Web Interface**:
    Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Project Structure

- **app.py**: Main application file containing the Flask routes and logic.
- **templates/**: Directory containing HTML templates for the web pages.
  - `home.html`: Home page with navigation options.
  - `index.html`: Page for Generative TTS.
  - `gtts.html`: Page for Google TTS.
- **static/**: Directory for static files (CSS, JavaScript, etc.).

## Flask Routes

- **Home Page** (`/`):
  - Description: Welcome page with navigation buttons to TTS and gTTS pages.
  - Template: `home.html`

- **Generative TTS** (`/tts`):
  - Description: Page for generating speech using Bark and Coqui TTS models.
  - Template: `index.html`
  - Method: `POST`
  - Form Inputs: 
    - `text`: Text to be converted to speech.
    - `file`: Upload a `.wav` file for voice cloning.
    - `language`: Language code (default is `en`).
  - Output: Generates and downloads the speech file.

- **Google TTS** (`/gtts`):
  - Description: Page for generating speech using Google TTS.
  - Template: `gtts.html`
  - Method: `POST`
  - Form Inputs: 
    - `text`: Text to be converted to speech.
  - Output: Generates and plays the speech file in the browser.

## How to Contribute

1. **Fork the Repository**: Click on the "Fork" button at the top right of the repository page.
2. **Clone the Forked Repository**: Clone the forked repository to your local machine.
3. **Create a New Branch**: Create a new branch for your feature or bugfix.
    ```bash
    git checkout -b feature-name
    ```
4. **Make Changes**: Make your changes in the new branch.
5. **Commit and Push**: Commit and push your changes to the new branch.
    ```bash
    git add .
    git commit -m "Description of changes"
    git push origin feature-name
    ```
6. **Create a Pull Request**: Go to the original repository and create a pull request from your fork.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Acknowledgments

Special thanks to the developers and contributors of the following libraries and models:
- [Google Text to Speech (gTTS)](https://pypi.org/project/gTTS/)
- [Bark TTS](https://github.com/suno-ai/bark)
- [Coqui TTS](https://github.com/coqui-ai/TTS)

## 🚀 About Me
I am an AI Specialist and Data Engineer at Navikenz & growing Android Developer (kotlin). Both the fields, Machine Learning and Android Development, fascinates me a lot. And I also have worked on Azure Cloud Computing platform to deploy machine learning models.

To know more about me, type ```"Bitan Paul"``` on your google search.

## 🔗 Links
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/thebitanpaul)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/thebitanpaul)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/thebitanpaul_)






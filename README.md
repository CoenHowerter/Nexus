# Nexus Engineering Assistant

Nexus is a voice-activated, Python-based AI assistant powered by Google's Gemini 2.5 Flash model. It listens for a wake word ("nexus"), processes voice commands, captures images via webcam upon request, speaks the response aloud, and sends a transcript of the response to your email.

## Features
* **Voice Recognition:** Listens for the wake word "nexus" in the ambient background using `SpeechRecognition`.
* **Vision Capabilities:** Triggered by saying "take a picture", Nexus will capture a frame from your webcam using `OpenCV` and send it to the Gemini vision model for analysis.
* **Text-to-Speech:** Reads out Gemini's responses using `gTTS` and `pygame`.
* **Email Integration:** Automatically emails you a copy of the AI's response using `smtplib`.

## Prerequisites
* Python 3.8 or higher
* A working microphone and webcam
* A Google Gemini API Key
* A Gmail account with an App Password generated for the SMTP email functionality

## Installation

1. Download or clone this repository to your local machine and navigate into the project folder using your terminal.
2. Install the required dependencies:
   `pip install opencv-python SpeechRecognition google-genai gTTS pygame pyaudio`
3. Set up your environment variables. You will need to export them in your terminal or set them up in your system environment before running the script:
   * `GEMINI_API_KEY`: Your Google Gemini API key.
   * `EMAIL_USER`: Your Gmail address.
   * `EMAIL_PASS`: Your Gmail App Password.

## Usage

Run the main script from your terminal:

`python nexus.py`

The console will display `Nexus Online` and begin listening. 
* To ask a standard question, say: *"Nexus, what is the speed of light?"*
* To analyze an object, say: *"Nexus, take a picture and tell me what you see."*

## Troubleshooting
* **Microphone not detected:** Ensure your system microphone permissions allow terminal/Python access. If `pyaudio` fails to install, you may need to install audio build tools specific to your operating system.
* **Email failing to send:** Ensure you are using a Google App Password, not your standard Gmail password, as Google blocks standard password logins for SMTP scripts.

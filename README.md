# Nexus Engineering Assistant

Nexus is a voice-activated, Python-based AI assistant powered by Google's Gemini 2.5 Flash model. It listens for a wake word ("nexus"), processes voice commands, captures images via webcam upon request, speaks the response aloud, and sends a transcript of the response to your email.

## Features
* **Voice Recognition:** Listens for the wake word "nexus" in the ambient background.
* **Vision Capabilities:** Triggered by saying "take a picture", Nexus will capture a frame from your webcam and send it to the Gemini vision model for analysis.
* **Text-to-Speech:** Reads out Gemini's responses using `gTTS` and `pygame`.
* **Email Integration:** Automatically emails you a copy of the AI's response.

## Prerequisites
* Python 3.8+
* A working microphone and webcam.
* A Google Gemini API Key.
* A Gmail account with an [App Password](https://support.google.com/accounts/answer/185833?hl=en) generated for the SMTP email functionality.

## Installation

1. **Clone the repository:**
   ```bash
   git clone 

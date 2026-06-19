import os
import cv2
import speech_recognition as sr
from google import genai
from google.genai import types
from gtts import gTTS
import pygame
import time
import smtplib
from email.message import EmailMessage

#init API
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
recognizer = sr.Recognizer()

def send_email(text):
    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = "Nexus Engineering Assistant Response"
    msg['From'] = os.environ.get("EMAIL_USER")
    msg['To'] = os.environ.get("EMAIL_USER")
   
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(os.environ.get("EMAIL_USER"), os.environ.get("EMAIL_PASS"))
            smtp.send_message(msg)
        print("Email Sent successfully.")
    except Exception as e:
        print(f"Email failed to send: {e}")

def speak(text):
    print(f"\n[Nexus]: {text}")
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("response.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("response.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        pygame.mixer.quit()
        os.remove("response.mp3")
    except Exception as e:
        print(f"[Audio Error]: {e}")

def capture_image():
    cap = cv2.VideoCapture(0)
    # Give the camera sensor half a second to adjust to room lighting
    time.sleep(0.5)
    ret, frame = cap.read()
    cap.release()
    if ret:
        success, buffer = cv2.imencode('.jpg', frame)
        return buffer.tobytes() if success else None
    return None

def main():
	print("Nexus Online")
   
    with sr.Microphone() as source:
        while True:
            # Continuously sample ambient noise to prevent false triggers
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("\n [Listening]")
           
            try:
                # Capture audio from the microphone
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)
                text = recognizer.recognize_google(audio).lower()
                print(f"[Heard] '{text}'")
               
                # Check for the wake word
                if "nexus" in text:
                    contents = [text]
                   
                    # Logic branch: Picture vs Voice-Only
                    if "take a picture" in text:
                        print("[Action] Taking photo")
                        img = capture_image()
                        if img:
                            # Attach the image to the Gemini payload
                            contents.append(types.Part.from_bytes(data=img, mime_type='image/jpeg'))
                        else:
                            print("[Warning] Camera capture failed")
                    else:
                        print("[Action]")
                   
                    print("[System]")
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=contents
                    )
                   
                    # Clean the text by removing all asterisks
                    clean_text = response.text.replace("*", "")
                   
                    # Output the cleaned response
                    speak(clean_text)
                    send_email(clean_text)
                   
            except sr.WaitTimeoutError:
                pass
            except sr.UnknownValueError:
                pass
            except Exception as e:
                print(f"[Error]: {e}")

if __name__ == "__main__":
    main()
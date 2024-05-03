# Install the Required Library

pip install SpeechRecognition

# Python Code


import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

def main():
    try:
        print("Listening... (Speak something)")
        with sr.Microphone() as source:
            audio = recognizer.listen(source, timeout=5)  # Record audio for 5 seconds

        # Recognize the speech
        text = recognizer.recognize_google(audio)
        print(f"Recognized text: {text}")

    except sr.WaitTimeoutError:
        print("Timeout: No speech detected.")
    except sr.UnknownValueError:
        print("Error: Unable to recognize speech.")
    except sr.RequestError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

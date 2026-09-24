import os
import speech_recognition as sr
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY is not set")

print("API KEY: ", api_key)

client = genai.Client(api_key=api_key)


def main():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            recognizer.pause_threshold = 2
            print("Speak Something...")
            audio = recognizer.listen(source)
            print("Processing audio... (STT)")
            stt = recognizer.recognize_google(audio)
            print("You said:", stt)
            print("Getting AI response...")
            interaction = client.interactions.create(
                model="gemini-2.5-flash", input=stt
            )

            print("Agent replied:", interaction.output_text)

    except sr.UnknownValueError:
        print("Could not understand the audio.")

    except sr.RequestError as e:
        print("Speech recognition service error:", e)
    except Exception as e:
        print("Error:", e)
    finally:
        print("exit")


if __name__ == "__main__":
    main()

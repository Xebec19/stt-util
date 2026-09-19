import speech_recognition as sr


def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2

        print("Speak Something...")
        audio = r.listen(source)

        print("Processing audio... (STT)")

        stt = r.recognize_google(audio)

        print("You said:", stt)


if __name__ == "__main__":
    main()

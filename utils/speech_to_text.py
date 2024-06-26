import speech_recognition as sr


recognizer = sr.Recognizer()

def convert_speech_to_text(filename):
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)

    return recognizer.recognize_sphinx(audio)


if __name__ == "__main__":
    filename = "justin_recording/Recording_28_surprised.wav"
    text = convert_speech_to_text(filename)
    print(filename, "\n", text, "\n")

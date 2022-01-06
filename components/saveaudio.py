import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0])


def save_content_to_mp3(book_name, content):
    try:
        engine.save_to_file(content, "mp3/" + book_name + ".mp3")
        engine.runAndWait()
    except:
        print("failed")
    else:
        print("success")
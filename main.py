import speech_recognition as sr
import webbrowser as wb

r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()


with sr.Microphone() as source:
    print("say (open youtube) to start")
    print("speak now")

    audio=r3.listen(source)


if ("open " in r2.recognize_google(audio)) or ("youtube" in r2.recognize_google(audio)):
    r2=sr.Recognizer()
    url="https://www.youtube.com/"
    with sr.Microphone() as source:
        print("search your query")

        audio=r2.listen(source)


        try:
            get=r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)

        except:
            print("voice is not clear  ")

#importing library (use pip install PyAudio)

import speech_recognition as sr

# Recognizer class

r = sr.Recognizer()

# Listening
# listening and storing it in audio

with sr.Microphone() as source:
    print("Speak")
    audio = r.listen(source)
    print("Time over, thanks")
# exception handling
    try:
        # using google speech recognition
        print("Text: "+r.recognize_google(audio))
    except:
         print("Sorry, I did not get that")

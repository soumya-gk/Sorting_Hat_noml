import json
import speech_recognition as sr
from gcpkey import getkey

GOOGLE_CLOUD_SPEECH_CREDENTIALS = None

def initRecogs():    
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = getkey()

def getRecognizer():
    return sr.Recognizer()

def getSpeech2Text(recog):
    # obtain audio from the microphone
    text = None

    with sr.Microphone() as source:
        print("Recording...")
        recog.adjust_for_ambient_noise(source)
        audio = recog.listen(source)

    # text = sphinxRec(recog,audio)
    if GOOGLE_CLOUD_SPEECH_CREDENTIALS:
        text = gcpRec(recog,audio)
    else:
        text = googleRec(recog,audio)

    return text

def sphinxRec(recog,audio):
    text = None
    try:
        text = recog.recognize_sphinx(audio)
        print("Sphinx thinks you said: " + text)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

    return text

def googleRec(recog,audio):
    text = None
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        text = recog.recognize_google(audio)
        print("Google Speech Recognition thinks you said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return text

def gcpRec(recog,audio):
    text = None
    
    try:
        text = recog.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
        print("Google Cloud Speech thinks you said: " + text)
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))
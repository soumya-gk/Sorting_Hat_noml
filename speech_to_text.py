import json
import speech_recognition as sr
from gcpkey import getkey

# Note that GOOGLE_CLOUD_SPEECH_CREDENTIALS key 
# is not provided in this github repo.
# This key can be obtained on signing up on Google Cloud Platform
# and using their Speech-to-Text API
GOOGLE_CLOUD_SPEECH_CREDENTIALS = getkey()
INDEX = 5

def getRecognizer():
    return sr.Recognizer()

def getSpeech2Text(recog):
    # obtain audio from the microphone
    text = None

    with sr.Microphone(device_index=INDEX) as source:
        print("Recording...")
        recog.adjust_for_ambient_noise(source)
        audio = recog.listen(source)

    # get text from speech 
    if GOOGLE_CLOUD_SPEECH_CREDENTIALS:
        text = gcpRec(recog,audio)
        print "gcp selected"
    else:
        print "google_service selected"
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

    return text
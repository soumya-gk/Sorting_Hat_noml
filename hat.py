import pygame           #to play sound files
import serial           #to connect to arduino through USB
import sys 
import time

import constants
from constants import *
from engine_hat import analyzeSpeech, analyzeSpeechShort, getRandomElem, UserSession, getWelcomeSpeech
from speech_to_text import getSpeech2Text, getRecognizer

SONG_END = pygame.USEREVENT + 1

def pauseAWhile():
    time.sleep(SLEEP_TIME)

def playSpeech(dialog_box,SERL):
    #start speaking
    dialog_box.play()
    if SERL:
        SERL.write(START_HAT)

def raiseHat(SERL):
    if SERL:
        SERL.write(RAISE_HAT)

def lowerHat(SERL):
    if SERL:
        SERL.write(LOWER_HAT)

def stopSpeech(SERL):
    notdone = True
    while notdone:
        for event in pygame.event.get():
            if event.type == SONG_END:
                if SERL:
                    SERL.write(END_HAT)
                notdone = False

def readSerial():
    # if SERL.inWaiting()>0:
    #   print "entered loop"
    #   mydata = SERL.readline()
    #   print mydata, len(mydata)
    return None

def loadDialog(dialog_box,dialog):
    #load dialog from 
    print "Hat says: {}".format(dialog[TEXT])
    dialog_box.load(dialog[PATH])
    pauseAWhile()
    dialog_box.set_endevent(SONG_END)
    
def loadAndPlayDialogs(dialog_box,dialogs,SERL):
    
    #stop speech
    dialog_box.stop()
    
    n = len(dialogs)

    raiseHat(SERL)
    for i in range(n):
        loadDialog(dialog_box,dialogs[i])
        if constants.DEBUG:
            print "playing: ",dialogs[i][PATH]
        playSpeech(dialog_box,SERL)
        pygame.mixer.music.set_volume(1)
        stopSpeech(SERL)
    lowerHat(SERL)

def startConv(dialog_box,recog,SERL=None,MIC_INDEX=None):

    isShort = False # change to True if you want a shorter conversation

    session = UserSession(isShort)
    
    #load and play welcome speech
    welcome_speech = getWelcomeSpeech(session)

    if constants.DEBUG:
        print("Welcoming new student...")
    loadAndPlayDialogs(dialog_box,welcome_speech,SERL)

    while not session.decisionMade:
        
        #get speech from user and convert to text
        text = None
        # text = getSpeech2Text(recog,MIC_INDEX)

        if not text:
            # print "Provide text input"
            text = raw_input("What did you say?...")

        #get list of audio files to play as response
        resp = analyzeSpeech(text,session)

        loadAndPlayDialogs(dialog_box,resp,SERL)

def getPort(argv):
    i = 0
    last_index = len(argv)-1
    while(argv[i] != "-p") and i < last_index:
        i += 1
    if i < last_index:
        return argv[i+1]

    return None

def getMic(argv):
    i = 0
    last_index = len(argv)-1
    while(argv[i] != "-m") and i < last_index:
        i += 1
    if i < last_index:
        return argv[i+1]

    return None

def getDebug(argv):
    i = 0
    last_index = len(argv)-1
    while(argv[i] != "-d") and i < last_index:
        i += 1
    if i < last_index:
        if argv[i+1].lower() == "true":
            return True

    return False

def main(argv):
    '''
    Talk to the Sorting Hat, answer his questions and get sorted into 
    one of four Hogwarts houses - Gryffindor, Hufflepuff, Ravenclaw & Slytherin.
    To run this program enter command (arguments are optional):
        python hat.py -p <arduino_port_num> -m <mic_index_num>

    arduino_port_num - this is the port number to which arduino 
    controlling the hat movements is connected. (in Linux environment only)
    Not providing it runs only the conversational agent 

    mic_index_num - this argument is the index of the preferred microphone(mic)
    If not provided, program selects the default system mic.

    Run "mics.py" to get a list of available microphones and their indices.
    '''
    #check for arduino port number argument else exit
    SERL = None
    MIC_INDEX = None
    if len(argv) > 0:
        #set arduino port number and and initialize serial
        port = getPort(argv)
        if port:
            port = "/dev/ttyACM"+port
            SERL = serial.Serial(port)
        MIC_INDEX = getMic(argv)
        constants.DEBUG = getDebug(argv)

    if constants.DEBUG:
        print("Set command line parameters")

    #initialize pygame for speech response playback
    pygame.init()
    pauseAWhile()
    if constants.DEBUG:
        print("Initialized pygame")
    dialog_box = pygame.mixer.music

    #initialize recognizer
    recog = getRecognizer()
    if constants.DEBUG:
        print("Initialized recognizer")
    
    try:
        while True:
            reply = raw_input("Press enter to wake up the hat!")

            #startconversation
            startConv(dialog_box,recog,SERL,MIC_INDEX)

    except KeyboardInterrupt:
        print "\nHat says: Farewell student!"
        if SERL:
            SERL.close()
        dialog_box.stop()
        exit()

if __name__ == "__main__":
    main(sys.argv[1:])
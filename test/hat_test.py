import pygame
import serial
import sys
import time
import traceback

from constants import *
from engine_hat import analyzeSpeech, UserSession
from speech_to_text import initRecogs, getSpeech2Text, getRecognizer

SONG_END = pygame.USEREVENT + 1

def pauseAWhile():
    time.sleep(SLEEP_TIME)

def playSpeech(dialog_box,ISARDUINO,SERL):
    #start speaking
    dialog_box.play()
    if ISARDUINO:
        SERL.write(START_HAT)

def pauseSpeech(ISARDUINO,SERL):
    notdone = True
    while notdone:
        for event in pygame.event.get():
            if event.type == SONG_END:
                print("The hat has spoken!")  #TODO: add what the hat spoke
                print ISARDUINO
                if ISARDUINO:
                    print "writing to serial: ",END_HAT
                    SERL.write(END_HAT)
                notdone = False
    return None

def readSerial():
    # if SERL.inWaiting()>0:
    #   print "entered loop"
    #   mydata = SERL.readline()
    #   print mydata, len(mydata)
    return None

def loadDialog(dialog_box,dialog):
    #load first dialog
    dialog_box.load(dialog)
    pauseAWhile()
    dialog_box.set_endevent(SONG_END)
    
def loadAndPlayDialogs(dialog_box,dialogs,ISARDUINO,SERL):
    
    #stop speech
    dialog_box.stop()
    
    n = len(dialogs)

    for i in range(n):
        print "loading: ",dialogs[i]
        loadDialog(dialog_box,dialogs[i])
        print "playing: ",dialogs[i]
        playSpeech(dialog_box,ISARDUINO,SERL)
        pygame.mixer.music.set_volume(1)
        pauseSpeech(ISARDUINO,SERL)
    
    return None

def startConv(dialog_box,recog,ISARDUINO,SERL):

    #load and play welcome speech
    loadDialog(dialog_box,SP_PATHS[WELCOME_HOUSE])  #TODO - add multiple random welcome speeches
    print("Loaded Welcome2")
    pauseAWhile()
    playSpeech(dialog_box,ISARDUINO,SERL)
    pauseSpeech(ISARDUINO,SERL)

    session = UserSession()
    count = 3

    while count != 0:
        
        #py2.7 console input
        # reply = input("Press enter to speak")

        #get speech from user and convert to text
        print "What do you say?..."
        text = getSpeech2Text(recog)

        if not text:
            #TODO - add error handling hat reply
            continue

        resp = []
        #get list of audio files to play - single file!
        if count == 3:
            resp = [SP_PATHS[LETSFINDOUT],SP_PATHS[CHOC_FROG]]
        elif count == 2:
            resp = [SP_PATHS[QUIDLIBRARY]]
        elif count == 1:
            resp = [SP_PATHS[RIGHT_THEN],SP_PATHS[I_SORT_YOU_INTO],SP_PATHS[RAVENCLAW]]

        loadAndPlayDialogs(dialog_box,resp,ISARDUINO,SERL)

        count -= 1

def main(argv):

    #check for arduino port number argument else exit
    if len(argv) < 1:
        print "Provide 2 arguments: True if arduino is connected (else False) and its corresponding port number!"
        exit()

    #set arduino port number and and initialize serial
    ISARDUINO = (argv[0] == "True")
    if ISARDUINO:
        port = "/dev/ttyACM"+argv[1]
        SERL = serial.Serial(port)
        # print ISARDUINO, SERL

    #init GCP recognizer
    try:
        initRecogs()
    except Exception:
        print "Error reading GCP file containing credentials"
        traceback.print_exc()

    #initialize pygame for playing speech
    pygame.init()
    pauseAWhile()
    print("Initialized pygame")
    dialog_box = pygame.mixer.music

    #initialize recognizer
    recog = getRecognizer()
    print("Got recognizer")
    
    try:
        while True:
            reply = raw_input("Press enter to talk to the hat!")

            #startconversation
            startConv(dialog_box,recog,ISARDUINO,SERL)

    except KeyboardInterrupt:
        print "Closing port and exiting"
        if ISARDUINO:
            SERL.close()
        dialog_box.stop()
        exit()

if __name__ == "__main__":
   main(sys.argv[1:])
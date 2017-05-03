#To run this program (python 2):
#1) ensure arduino is connected via serial cable
#2) find out which port arduino is connected to and note down its name
#3) provide the port name as an argument when running the program
# Command to run:
# python testArdSpeech.py COM8


import pygame
import serial
import sys
import time

START_HAT = 's'
END_HAT = 'e'
SONG_END = pygame.USEREVENT + 1
PATH2MUSIC = "ravenclaw.mp3"

def main(argv):

    #check for arduino port number argument else exit
    if len(argv) < 1:
        print "Provide arduino port number! eg. /dev/ttyACM0 (for linux) or COM8 (for windows)"
        exit()

    #set arduino port number and and initialize serial
    isArduino = argv[0]
    ard_main = None
    if isArduino:
        port = argv[1]
        ard_main = serial.Serial(port)

    #initialize pygame for playing speech
    pygame.init()
    print("Initialized pygame")

    #load welcome speech
    pygame.mixer.music.load(PATH2MUSIC)
    print("Loaded song")
    pygame.mixer.music.set_endevent(SONG_END)
    print("Set End event")

    #start speaking
    pygame.mixer.music.play()
    if ard_main:
        ard_main.write(START_HAT)
    else:
        print "No Arduino serial connection found"

    notdone = True
    
    while notdone:
        for event in pygame.event.get():
            if event.type == SONG_END:
                print("speech ended")
                if ard_main:
                    ard_main.write(END_HAT)
                notdone = False
    
    # pygame.mixer.music.stop() - nullifies all in queue
    # pygame.mixer.music.queue - queue a music file to follow the current while one is playing
    return None

if __name__ == "__main__":
   main(sys.argv[1:])
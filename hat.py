import pygame
import serial
import sys
import time

from engine_hat import *
from speech_to_text import getSpeech2Text, getRecognizer

COUNT = 2
START_HAT = 's'
END_HAT = 'e'
SONG_END = pygame.USEREVENT + 1

def playPause(hat_speech,serl):

	#start speaking
	hat_speech.play()
	serl.write(START_HAT)

	notdone = True
	
	while notdone:
		for event in pygame.event.get():
        	if event.type == SONG_END:
        		serl.write(END_HAT)
        		notdone = False
	
	# pygame.mixer.music.stop() - nullifies all in queue
	# pygame.mixer.music.queue - queue a music file to follow the current
	return None

def startConv(hat_speech,serl,recog,count):

	while count != 0:
		#play welcome speech initially then other
		playPause(hat_speech,serl)
	
		#py2.7 console input
		reply = raw_input("Press enter to speak")
		# reply = input("Press enter to speak")

		#get speech to text
		text = getSpeech2Text(recog)

		#get list of audio files to play
		resp = analyzeSpeech(text)

		#enqueue music files
		for file in resp:
			hat_speech.queue(file)

		count -= 1

def readSerial(serl):
	# if ard_main.inWaiting()>0:
	# 	print "entered loop"
	# 	mydata = ard_main.readline()
	# 	print mydata, len(mydata)
	return None

def main(argv):

	#check for arduino port number argument else exit
	if len(argv) < 1:
		print "Provide arduino port number as argument!"
		exit()

	#set arduino port number and and initialize serial
	port = "/dev/ttyACM"+argv[0]
	ard_main = serial.Serial(port)

	#initialize pygame for playing speech
	pygame.init()

	#load welcome speech
	pygame.mixer.music.load(SP_PATHS[WELCOME])
	pygame.mixer.music.set_endevent(SONG_END)

	#initialize recognizer
	recog = getRecognizer()

	#startconversation
	try:
		startConv(pygame.mixer.music,ard_main,recog,COUNT)

	except KeyboardInterrupt:
		print "Closing port and exiting"
		ard_main.close()
		pygame.mixer.music.stop()
		exit()

if __name__ == "__main__":
   main(sys.argv[1:])
import pygame

SONG_END = pygame.USEREVENT + 1

COUNT = 3


AHGOON = "ah_go_on"
ALLEY = "alley_question"
HUFFLEPUFF = "hufflepuff"
RAVENCLAW = "ravenclaw"
GRYFFINDOR = "gryffindor"
SLYTHERIN = "slytherin"
SORT_SLYTHERIN = "sort_slytherin"
RIGHT_GRYFFINDOR = "right_gryffindor"
TELL_MEMORY = "tell_memory"
WELCOME1 = "welcome1"
WHICH_HOUSE = "which_house"
WHY_DO_YOU_THINK = "why_do_you_think"
I_SORT_YOU_INTO = "I_sort_you_into"
RIGHT_THEN = "right_then"
WELCOME2 = "welcome2"
EARTH = "earth"
CHOC_FROG = "choc_frog"

SP_PATHS = {
    AHGOON : "raw/ah_go_on.mp3",
    ALLEY : "raw/alley_sound.mp3",
    HUFFLEPUFF : "raw/hufflepuff.mp3",
    RAVENCLAW : "raw/ravenclaw.mp3",
    GRYFFINDOR : "raw/gryffindor.mp3",
    SLYTHERIN : "raw/slytherin.mp3",
    SORT_SLYTHERIN : "raw/sort_slytherin.mp3",
    RIGHT_GRYFFINDOR : "raw/right_gryffindor.mp3",
    TELL_MEMORY : "raw/tell_memory.mp3",
    WELCOME1 : "raw/welcome1.mp3",
    WELCOME2 : "raw/welcome2.mp3",
    WHICH_HOUSE : "raw/which_house.mp3",
    WHY_DO_YOU_THINK : "raw/why_do_you_think.mp3",
    I_SORT_YOU_INTO : "raw/Isortyouinto.mp3",
    RIGHT_THEN : "raw/right_then.mp3",
    CHOC_FROG : "raw/chocfrog.mp3",
    EARTH : "raw/earthsky.mp3"
}

def playPause(hat_speech):

    #start speaking
    hat_speech.play()
    # serl.write(START_HAT)

    notdone = True
    
    while notdone:
        for event in pygame.event.get():
            if event.type == SONG_END:
                print("song ended")
                # serl.write(END_HAT)
                notdone = False
    
    # pygame.mixer.music.stop() - nullifies all in queue
    # pygame.mixer.music.queue - queue a music file to follow the current
    return None


pygame.init()
hat_speech = pygame.mixer.music

#load welcome speech
hat_speech.load(SP_PATHS[WELCOME2])
hat_speech.set_endevent(SONG_END)

count = COUNT
while count >= 0:
    #play welcome speech initially then other
    playPause(hat_speech)

    #py2.7 console input
    reply = raw_input("Press enter to speak")
    # reply = input("Press enter to speak")

    #get speech to text
    # text = getSpeech2Text(recog)

    #get list of audio files to play
    # resp = analyzeSpeech(text)
    if count == 3:
    	resp = [SP_PATHS[I_SORT_YOU_INTO]]
    elif count == 2:
    	resp = [SP_PATHS[GRYFFINDOR],SP_PATHS[HUFFLEPUFF]]
    elif count == 1:
    	resp = [SP_PATHS[SLYTHERIN]]
    # resp = [SP_PATHS[I_SORT_YOU_INTO],SP_PATHS[GRYFFINDOR]]

    #enqueue music files
    hat_speech.stop()
    print "stopped hat speech"
    hat_speech.load(resp[0])
    print "loaded ",resp[0]
    for i in range(1,len(resp)):
        print "added to queue", resp[i]
        hat_speech.queue(resp[i])

    count -= 1
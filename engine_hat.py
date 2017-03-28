
AHGOON = "ah_go_on"
ALLEY = "alley_question"
HUFFLEPUFF = "hufflepuff"
RAVENCLAW = "ravenclaw"
GRYFFINDOR = "gryffindor"
SLYTHERIN = "slytherin"
SORT_SLYTHERIN = "sort_slytherin"
RIGHT_GRYFFINDOR = "right_gryffindor"
TELL_MEMORY = "tell_memory"
WELCOME = "welcome"
WHICH_HOUSE = "which_house"
WHY_DO_YOU_THINK = "why_do_you_think"
I_SORT_YOU_INTO = "I_sort_you_into"
RIGHT_THEN = "right_then"

SP_PATHS = {
	AHGOON : "raw/ah_go_on.mp3",
	ALLEY : "raw/alley_sound.m4a",
	HUFFLEPUFF : "raw/hufflepuff.mp3",
	RAVENCLAW : "raw/ravenclaw.mp3",
	GRYFFINDOR : "raw/gryffindor.mp3",
	SLYTHERIN : "raw/slytherin.mp3",
	SORT_SLYTHERIN : "raw/sort_slytherin.mp3",
	RIGHT_GRYFFINDOR : "raw/right_gryffindor.mp3",
	TELL_MEMORY : "raw/tell_memory.m4a",
	WELCOME : "raw/welcome.mp3",
	WHICH_HOUSE : "raw/which_house.m4a",
	WHY_DO_YOU_THINK : "raw/why_do_you_think.m4a",
	I_SORT_YOU_INTO : "raw/I_sort_you_into.mp3",
	RIGHT_THEN : "raw/right_then.m4a"
}

scores = {GRYFFINDOR:0, HUFFLEPUFF:0, RAVENCLAW:0, SLYTHERIN:0}

#analyze speech and send a list of music files to play
def analyzeSpeech(text):
	return None
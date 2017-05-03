from constants import *

scores = {GRYFFINDOR:0, HUFFLEPUFF:0, RAVENCLAW:0, SLYTHERIN:0}

argmax = lambda x : max(x.iteritems(),key=lambda y : y[1])[0]

yes_response = {"yes":1,"yeah":1,"yep":1}
no_response = {"no":1,"nah":1,"don't":1,"dont":1,"nope":1,"not":1}
earth = {"earth":1}
sky = {"sky":1}
gryffindor = {"gryffindor":1}
ravenclaw = {"ravenclaw":1}
slytherin = {"slytherin":1}
hufflepuff = {"hufflepuff":1}

class UserSession:

    def __init__(self):
        self.decisionMade = False
        self.hpknowledge = False
        self.housePref = False

    def endSession(self):
        self.decisionMade = True

def checkhouse(word):
    if word in gryffindor:
        scores[GRYFFINDOR] += 1
        print "Added 1 point to Gryffindor"
    elif word in ravenclaw:
        scores[RAVENCLAW] += 1
        print "Added 1 point to Ravenclaw"
    elif word in hufflepuff:
        scores[HUFFLEPUFF] += 1
        print "Added 1 point to Hufflepuff"
    elif word in slytherin:
        scores[SLYTHERIN] += 1
        print "Added 1 point to Slytherin"

#analyze speech and send a list of music files to play
def analyzeSpeech(text,count):
    words = text.lower().split()
    print(("tokens are: ",words))

    resp = AHGOON

    if count == 3:
        for word in words:
            checkhouse(word)
        resp = SP_PATHS[Q1]
    elif count == 2:
        for word in words:
            if word in earth:
                scores[SLYTHERIN] += 1
                scores[HUFFLEPUFF] += 1
                print "Added 1 point to Hufflepuff and Slytherin"
            elif word in sky:
                scores[RAVENCLAW] += 1
                scores[GRYFFINDOR] += 1
                print "Added 1 point to Ravenclaw and Gryffindor"
        resp = SP_PATHS[Q2]
    elif count == 1:
        for word in words:
            if word in yes_response:
                scores[GRYFFINDOR] += 1
                scores[HUFFLEPUFF] += 1
                print "Added 1 point to Gryffindor and Hufflepuff"
            elif word in no_response:
                scores[SLYTHERIN] += 1
                scores[RAVENCLAW] += 1
                print "Added 1 point to Ravenclaw and Slytherin"
        key = argmax(scores)
        print "scores: ",scores
        resp = SP_PATHS[key]

    return resp
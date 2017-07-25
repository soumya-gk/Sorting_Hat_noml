import random as ran
import string
import constants
from constants import *

argmax = lambda x : max(x.iteritems(),key=lambda y : y[1])[0]

yes_response = {"yes":1,"yeah":1,"yep":1,"will":1,"would":1,"ok":1,"alright":1,"right":1,"open":1}
hp_words = {"hogwarts":1,"gryffindor":1,"slytherin":1,"ravenclaw":1,"hufflepuff":1}
no_response = {"no":1,"nah":1,"dont":1,"nope":1,"not":1,"never":1,"wouldnt":1,"wont":1}
earth = {"earth":1}
sky = {"sky":1}
self_ans = {"library":1,"myself":1,"alone":1,"escape":1,"explore":1,"safe":1,"school":1,"ground":1,"grounds":1}
others_ans = {"quidditch":1,"play":1,"others":1,"friends":1,"warn":1,"group":1,"friend":1}
gryffindor = {"gryffindor":1,"red":1,"lion":1,"fire":1}
ravenclaw = {"ravenclaw":1,"blue":1,"eagle":1,"water":1}
slytherin = {"slytherin":1,"green":1,"serpant":1,"snake":1,"air":1}
hufflepuff = {"hufflepuff":1,"yellow":1,"badger":1,"earth":1}

class UserSession:

    def __init__(self, isShort):
        self.decisionMade = False
        self.hpknowledge = False
        self.state = ST_WELCOME
        self.question = None
        self.seen = []
        self.isShort = isShort
        self.scores = {GRYFFINDOR:0, HUFFLEPUFF:0, RAVENCLAW:0, SLYTHERIN:0}
        if isShort:
            self.count = 3
        else:
            self.count = 0

    def endSession(self):
        self.decisionMade = True

    def addscore(self,index,score):
        self.scores[index] += score
        if constants.DEBUG:
            print "Added {} to {}".format(score,index)

    def getMaxHouse(self):
        return argmax(self.scores)

def getRandomElem(arr):
    return arr[ran.randint(0,len(arr)-1)]

def getSpeechPathAndText(keys):
    dialogs = []
    for key in keys:
        dialogBundle = {}
        dialogBundle[TEXT] = SP_TEXTS[key]
        dialogBundle[PATH] = SP_PATHS[key]
        dialogs.append(dialogBundle)

    return dialogs

def getWelcomeSpeech(session):
    welcome = getRandomElem(STATES[ST_WELCOME])
    pref = getRandomElem(STATES[ST_HP_KNOWLEDGE])
    welcomeSpeech = getSpeechPathAndText([welcome,pref])
    session.state = ST_HP_KNOWLEDGE
    session.question = pref
    return welcomeSpeech

def checkhouse(word,session):
    if word in gryffindor:
        session.addscore(GRYFFINDOR,0.5)
    elif word in ravenclaw:
        session.addscore(RAVENCLAW,0.5)
    elif word in hufflepuff:
        session.addscore(HUFFLEPUFF,0.5)
    elif word in slytherin:
        session.addscore(SLYTHERIN,0.5)

def checkYes(words):
    for word in words:
        if word in yes_response:
            return True
    return False

def checkNo(words):
    for word in words:
        if word in no_response:
            return True
    return False

def checkHP(words):
    for word in words:
        if word in hp_words:
            return True
    return False

#analyze speech and send a list of music files to play
def analyzeSpeech(text,session):

    if session.isShort:
        resp = analyzeSpeechShort(text,session)
        return resp

    print "You said: {}".format(text)
    text = text.translate(None,string.punctuation)
    words = text.lower().split()
    resp = []
    yes = False
    no = False

    if session.state == ST_HP_KNOWLEDGE:
        yes = checkYes(words)
        no = checkNo(words)
        hp = checkHP(words)
        if hp or yes:
            session.hpknowledge = True
        else:
            session.hpknowledge = False
            if session.question == SORTING_HAT or session.question == HOG_STUDY:
                session.endSession()
                dialogs = getSpeechPathAndText([FAREWELL])
                return dialogs
        session.state = ST_ALRIGHT
        session.question = getRandomElem(STATES[ST_PREF])
        resp = [getRandomElem(STATES[ST_WELL]),
                getRandomElem(STATES[ST_BEGIN]),
                session.question]
    elif session.state == ST_ALRIGHT:
        for word in words:
            checkhouse(word,session)
        session.question = getRandomElem(STATES[ST_GRYFFINDOR])
        session.state = ST_GRYFFINDOR
        resp.append(STATES[ST_ALRIGHT][0])
        resp.append(session.question)
    elif session.state == ST_GRYFFINDOR:
        session.state = ST_HUFFLEPUFF
        yes = checkYes(words)
        no = checkNo(words)
        if no:
            session.addscore(SLYTHERIN,0.5)
            session.addscore(HUFFLEPUFF,0.5)
            if session.question != Q_CAKE:
                session.addscore(RAVENCLAW,0.5)
            resp.append(F_SAFE)
        elif yes:
            session.addscore(GRYFFINDOR,1)
            if session.question == Q_CAKE:
                session.addscore(RAVENCLAW,0.5)
            resp.append(F_ADVENTURE)
        resp.append(getRandomElem(STATES[ST_Q_TRANS]))
        session.question = getRandomElem(STATES[ST_HUFFLEPUFF])
        resp.append(session.question)
    elif session.state == ST_HUFFLEPUFF:
        session.state = ST_SLYTHERIN
        yes = checkYes(words)
        no = checkNo(words)
        if no:
            session.addscore(RAVENCLAW,0.5)
            session.addscore(HUFFLEPUFF,1)
            resp.append(F_KNOWN)
        elif yes:
            session.addscore(GRYFFINDOR,0.5)
            session.addscore(SLYTHERIN,0.5)
            resp.append(F_UNKNOWN)
        resp.append(getRandomElem(STATES[ST_Q_TRANS]))
        session.question = getRandomElem(STATES[ST_SLYTHERIN])
        resp.append(session.question)
    elif session.state == ST_SLYTHERIN:
        session.state = ST_RAVENCLAW
        yes = checkYes(words)
        no = checkNo(words)
        if no:
            if session.question == Q_CHEATING:
                session.addscore(GRYFFINDOR,0.5)
                session.addscore(SLYTHERIN,1.0)
                resp.append(F_BEND_RULES)
            else:
                session.addscore(RAVENCLAW,0.5)
                session.addscore(HUFFLEPUFF,0.5)
                resp.append(F_JUSTICE)
        elif yes:
            if session.question == Q_CHEATING:
                session.addscore(RAVENCLAW,0.5)
                session.addscore(HUFFLEPUFF,0.5)
                resp.append(F_JUSTICE)
            else:
                session.addscore(GRYFFINDOR,0.5)
                session.addscore(SLYTHERIN,1.0)
                resp.append(F_BEND_RULES)
        resp.append(getRandomElem(STATES[ST_Q_TRANS]))
        session.question = getRandomElem(STATES[ST_RAVENCLAW])
        resp.append(session.question)
    elif session.state == ST_RAVENCLAW:
        others = False
        self_ = False
        # yes = checkYes(words)
        # no = checkNo(words)
        for word in words:
            if word in self_ans:
                self_ = True
            if word in others_ans:
                others = True      
        if self_:
            session.addscore(RAVENCLAW,1.0)
            session.addscore(SLYTHERIN,0.5)
            resp.append(F_SELF)
        elif others:
            session.addscore(GRYFFINDOR,0.5)
            session.addscore(HUFFLEPUFF,0.5)
            resp.append(F_OTHERS)
        resp.append(STATES[ST_FINALLY][0])
        session.question = getRandomElem(STATES[ST_RANDOM])
        session.state = ST_RANDOM
        resp.append(session.question)
    elif session.state == ST_RANDOM:
        result = session.getMaxHouse()
        resp.append(getRandomElem(STATES[ST_CHOICE]))
        resp.append(STATES[ST_RIGHT_THEN][0])
        resp.append(STATES[ST_DECLARE][result])
        resp.append(STATES[ST_I_SORT][0])
        resp.append(result)
        session.endSession()

    dialogs = getSpeechPathAndText(resp)
    
    if constants.DEBUG:
        print("Current State: {}".format(session.state))

    return dialogs

def declare(session):
    resp = []
    result = session.getMaxHouse()
    resp.append(STATES[ST_RIGHT_THEN][0])
    resp.append(STATES[ST_DECLARE][result])
    resp.append(STATES[ST_I_SORT][0])
    resp.append(result)
    session.endSession()
    resp = getSpeechPathAndText(resp)
    return resp

def analyzeSpeechShort(text,session):
        
    #TODO - analyze speech when conversation is meant to be short

    return dialogs
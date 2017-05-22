from constants import *
import random as ran

scores = {GRYFFINDOR:0, HUFFLEPUFF:0, RAVENCLAW:0, SLYTHERIN:0}

argmax = lambda x : max(x.iteritems(),key=lambda y : y[1])[0]

yes_response = {"yes":1,"yeah":1,"yep":1,"will":1,"would":1,"ok":1,"alright":1,"right":1}
hp_words = {"hogwarts":1,"gryffindor":1,"slytherin":1,"ravenclaw":1,"hufflepuff":1}
no_response = {"no":1,"nah":1,"don't":1,"dont":1,"nope":1,"not":1,"never":1,"wouldn't":1,"won't":1}
earth = {"earth":1}
sky = {"sky":1}
gryffindor = {"gryffindor":1,"red":1,"lion":1,"fire":1}
ravenclaw = {"ravenclaw":1,"blue":1,"eagle":1,"water":1}
slytherin = {"slytherin":1,"green":1,"serpant":1,"snake":1,"air":1}
hufflepuff = {"hufflepuff":1,"yellow":1,"badger":1,"earth":1}

class UserSession:

    def __init__(self):
        self.decisionMade = False
        self.hpknowledge = False
        self.housePref = False
        self.state = ST_HP_KNOWLEDGE
        self.question = None
        self.seen = []

    def endSession(self):
        self.decisionMade = True

def getRandomElem(arr):
    return arr[ran.randint(0,len(arr)-1)]

def addscore(index,score):
    scores[index] += score
    print "Added {} to {}".format(score,index)

def checkhouse(word):
    if word in gryffindor:
        addscore(GRYFFINDOR,0.5)
    elif word in ravenclaw:
        addscore(RAVENCLAW,0.5)
    elif word in hufflepuff:
        addscore(HUFFLEPUFF,0.5)
    elif word in slytherin:
        addscore(SLYTHERIN,0.5)

def checkYes(word):
    if word in yes_response:
        return True
    return False

def checkNo(word):
    if word in no_response:
        return True
    return False

def checkHP(word):
    if word in hp_words:
        return True
    return False

#analyze speech and send a list of music files to play
def analyzeSpeech(text,session,count):
    words = text.lower().split()
    print(("User said: ",words))
    resp = []
    yes = False
    no = False

    if session.state == ST_HP_KNOWLEDGE:
        for word in words:
            yes = checkYes(word)
            no = checkNo(word)
            hp = checkHP(word)
        if hp or yes:
            session.housePref = True
        else:
            session.housePref = False
        session.state = ST_ALRIGHT
        session.question = getRandomElem(STATES[ST_PREF])
        resp = [SP_PATHS[getRandomElem(STATES[ST_WELL])],
                SP_PATHS[getRandomElem(STATES[ST_BEGIN])],
                SP_PATHS[session.question]]
        return resp
    elif session.state == ST_ALRIGHT:
        if session.question == WHICH_HOUSE:
            for word in words:
                checkhouse(word)
        session.question = getRandomElem(STATES[ST_GRYFFINDOR])
        if session.question[:2] == "hp" and session.hpknowledge:
            session.question = 0
        session.state = ST_GRYFFINDOR
        resp.append(SP_PATHS[STATES[ST_ALRIGHT][0]])
        resp.append(SP_PATHS[session.question])
        return resp
    elif session.state == ST_GRYFFINDOR:
        session.state = ST_HUFFLEPUFF
        for word in words:
            yes = checkYes(word)
            no = checkNo(word)
        if no:
            addscore(SLYTHERIN,0.5)
            addscore(HUFFLEPUFF,0.5)
            if session.question != Q_CAKE:
                addscore(RAVENCLAW,0.5)
            resp.append(SP_PATHS[F_SAFE])
        elif yes:
            addscore(GRYFFINDOR,1)
            if session.question == Q_CAKE:
                addscore(RAVENCLAW,0.5)
            resp.append(SP_PATHS[F_ADVENTURE])
        resp.append(SP_PATHS[getRandomElem(STATES[ST_Q_TRANS])])
        session.question = getRandomElem(STATES[ST_HUFFLEPUFF])
        if session.question[:2] == "hp" and session.hpknowledge:
            session.question = 0
        resp.append(SP_PATHS[session.question])
    elif session.state == ST_HUFFLEPUFF:
        session.state = ST_SLYTHERIN
        for word in words:
            yes = checkYes(word)
            no = checkNo(word)
        if no:
            addscore(RAVENCLAW,0.5)
            addscore(HUFFLEPUFF,1)
            resp.append(SP_PATHS[F_KNOWN])
        elif yes:
            addscore(GRYFFINDOR,0.5)
            addscore(SLYTHERIN,0.5)
            resp.append(SP_PATHS[F_UNKNOWN])
        resp.append(SP_PATHS[getRandomElem(STATES[ST_Q_TRANS])])
        session.question = getRandomElem(STATES[ST_SLYTHERIN])
        if session.question[:2] == "hp" and session.hpknowledge:
            session.question = 0
        resp.append(SP_PATHS[session.question])
    elif session.state == ST_SLYTHERIN:
        session.state = ST_RAVENCLAW
        for word in words:
            yes = checkYes(word)
            no = checkNo(word)
        if no:
            addscore(RAVENCLAW,0.5)
            addscore(HUFFLEPUFF,0.5)
            resp.append(SP_PATHS[F_JUSTICE])
        elif yes:
            addscore(GRYFFINDOR,0.5)
            addscore(SLYTHERIN,1.0)
            resp.append(SP_PATHS[F_BEND_RULES])
        resp.append(SP_PATHS[getRandomElem(STATES[ST_Q_TRANS])])
        session.question = getRandomElem(STATES[ST_RAVENCLAW])
        if session.question[:2] == "hp" and session.hpknowledge:
            session.question = 0
        resp.append(SP_PATHS[session.question])
    elif session.state == ST_RAVENCLAW:
        others = False
        selfi = False
        for word in words:
            yes = checkYes(word)
            no = checkNo(word)
            if word in ["library","myself","alone","escape","explore","safe"]:
                selfi = True
            if word in ["Quidditch","play","others","friends","warn"]:
                others = True      
        if selfi:
            addscore(RAVENCLAW,1.0)
            addscore(SLYTHERIN,0.5)
            resp.append(SP_PATHS[F_SELF])
        elif others:
            addscore(GRYFFINDOR,0.5)
            addscore(HUFFLEPUFF,0.5)
            resp.append(SP_PATHS[F_OTHERS])
        resp.append(SP_PATHS[STATES[ST_FINALLY][0]])
        session.question = getRandomElem(STATES[ST_RANDOM])
        session.state = ST_RANDOM
        resp.append(SP_PATHS[session.question])
    elif session.state == ST_RANDOM:
        result = argmax(scores)
        resp.append(SP_PATHS[getRandomElem(STATES[ST_CHOICE])])
        resp.append(SP_PATHS[STATES[ST_RIGHT_THEN][0]])
        resp.append(SP_PATHS[STATES[ST_DECLARE][result]])
        resp.append(SP_PATHS[STATES[ST_I_SORT][0]])
        resp.append(SP_PATHS[result])
        session.endSession()

    return resp

def analyzeSpeechShort(text,session,count):
    words = text.lower().split()
    print(("User said: ",text))
    resp = []
    yes = False
    no = False

    if session.state == ST_HP_KNOWLEDGE:
        for word in words:
            yes = checkYes(word)
            no = checkNo(word)
            hp = checkHP(word)
        if hp or yes:
            session.housePref = True
        else:
            session.housePref = False
        session.state = ST_ALRIGHT
        session.question = getRandomElem(STATES[ST_PREF])
        resp = [SP_PATHS[getRandomElem(STATES[ST_WELL])],
                SP_PATHS[getRandomElem(STATES[ST_BEGIN])],
                SP_PATHS[session.question]]
        return resp
    elif session.state == ST_ALRIGHT:
        for word in words:
            checkhouse(word)
        session.state = getRandomElem(STATES[ST_STRONG])
        session.question = getRandomElem(STATES[session.state])
        session.seen.append(session.state)
        if session.question[:2] == "hp" and session.hpknowledge:
            session.question = 0
        resp.append(SP_PATHS[STATES[ST_ALRIGHT][0]])
        resp.append(SP_PATHS[session.question])
        return resp
    elif session.state == ST_GRYFFINDOR:
        if count == 0:
            resp = declare(session)
            return resp 
        new_state = list(set(STATES[ST_STRONG]) - set(session.seen))
        session.state = getRandomElem(new_state)
        for word in words:
            yes = checkYes(word)
            no = checkNo(word)
        if no:
            addscore(SLYTHERIN,0.5)
            addscore(HUFFLEPUFF,0.5)
            if session.question != Q_CAKE:
                addscore(RAVENCLAW,0.5)
            resp.append(SP_PATHS[F_SAFE])
        elif yes:
            addscore(GRYFFINDOR,1)
            if session.question == Q_CAKE:
                addscore(RAVENCLAW,0.5)
            resp.append(SP_PATHS[F_ADVENTURE])
        resp.append(SP_PATHS[getRandomElem(STATES[ST_Q_TRANS])])
        session.question = getRandomElem(STATES[session.state])
        if session.question[:2] == "hp" and session.hpknowledge:
            session.question = 0
        resp.append(SP_PATHS[session.question])
    elif session.state == ST_HUFFLEPUFF:
        if count == 0:
            resp = declare(session)
            return resp 
        new_state = list(set(STATES[ST_STRONG]) - set(session.seen))
        session.state = getRandomElem(new_state)
        for word in words:
            yes = checkYes(word)
            no = checkNo(word)
        if no:
            addscore(RAVENCLAW,0.5)
            addscore(HUFFLEPUFF,1)
            resp.append(SP_PATHS[F_KNOWN])
        elif yes:
            addscore(GRYFFINDOR,0.5)
            addscore(SLYTHERIN,0.5)
            resp.append(SP_PATHS[F_UNKNOWN])
        resp.append(SP_PATHS[getRandomElem(STATES[ST_Q_TRANS])])
        session.question = getRandomElem(STATES[session.state])
        if session.question[:2] == "hp" and session.hpknowledge:
            session.question = 0
        resp.append(SP_PATHS[session.question])
    elif session.state == ST_SLYTHERIN:
        if count == 0:
            resp = declare(session)
            return resp 
        new_state = list(set(STATES[ST_STRONG]) - set(session.seen))
        session.state = getRandomElem(new_state)
        for word in words:
            yes = checkYes(word)
            no = checkNo(word)
        if no:
            addscore(RAVENCLAW,0.5)
            addscore(HUFFLEPUFF,0.5)
            resp.append(SP_PATHS[F_JUSTICE])
        elif yes:
            addscore(GRYFFINDOR,0.5)
            addscore(SLYTHERIN,1.0)
            resp.append(SP_PATHS[F_BEND_RULES])
        resp.append(SP_PATHS[getRandomElem(STATES[ST_Q_TRANS])])
        session.question = getRandomElem(STATES[session.state])
        if session.question[:2] == "hp" and session.hpknowledge:
            session.question = 0
        resp.append(SP_PATHS[session.question])
    elif session.state == ST_RAVENCLAW:
        if count == 0:
            resp = declare(session)
            return resp 
        new_state = list(set(STATES[ST_STRONG]) - set(session.seen))
        session.state = getRandomElem(new_state)
        others = False
        selfi = False
        for word in words:
            yes = checkYes(word)
            no = checkNo(word)
            if word in ["library","myself","alone","escape","explore","safe"]:
                selfi = True
            if word in ["Quidditch","play","others","friends","warn"]:
                others = True      
        if selfi:
            addscore(RAVENCLAW,1.0)
            addscore(SLYTHERIN,0.5)
            resp.append(SP_PATHS[F_SELF])
        elif others:
            addscore(GRYFFINDOR,0.5)
            addscore(HUFFLEPUFF,0.5)
            resp.append(SP_PATHS[F_OTHERS])
        resp.append(SP_PATHS[getRandomElem(STATES[ST_Q_TRANS])])
        session.question = getRandomElem(STATES[session.state])
        if session.question[:2] == "hp" and session.hpknowledge:
            session.question = 0
        resp.append(SP_PATHS[session.question])
    elif session.state == ST_RANDOM:
        resp.append(SP_PATHS[getRandomElem(STATES[ST_CHOICE])])
        resp += declare(session)

    return resp

def declare(session):
    resp = []
    result = argmax(scores)
    resp.append(SP_PATHS[STATES[ST_RIGHT_THEN][0]])
    resp.append(SP_PATHS[STATES[ST_DECLARE][result]])
    resp.append(SP_PATHS[STATES[ST_I_SORT][0]])
    resp.append(SP_PATHS[result])
    session.endSession()
    return resp

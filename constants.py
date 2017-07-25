#misc constants
START_HAT = 's'
END_HAT = 'e'
RAISE_HAT = 'u'
LOWER_HAT = 'd'
SLEEP_TIME = 0.3

#DEBUG
DEBUG = False

#dialog keys
WELCOME = "welcome"
GOOD_DAY = "good_day"
NEW_STUD = "new_student"

SORT_PERS = "sort_personality"
HOG_STUDY = "study_hogwarts"
SORTING_HAT = "sorting_hat_intro"

PERS_HOUSE = "pers_house"
FIND_HOUSE = "find_house"

FAREWELL = "farewell"

I_VERY_WELL = "very_well"
I_WELL_THEN = "well_then"

I_ALRIGHT = "alright"
I_ANOTHER_Q = "try_another"
I_INTERESTING = "interesting_choice"
I_FINE = "fine_choice"
I_SEE = "i_see"
I_AHGOON = "ah_go_on"
I_FINALLY = "and_finally"
I_RIGHT_THEN = "right_then"

Q_COLOR = "which_color"
Q_ELEMENT = "which_element"
Q_ANIMAL = "which_animal"

WISH_SORTED = "wish_sorted"
HOG_HOUSES = "hogwarts_houses"
WHICH_HOUSE = "which_house"
Q_MAIL = "mail_in_storm"
Q_SHORTCUT_WIN = "dangerous_shortcut"
Q_CAKE = "new_recipe"
Q_TROLL = "troll_save"

F_ADVENTURE = "adventure"
F_SAFE = "safe_than_sorry"

Q_NEW_PATH = "new_path"
Q_DOOR = "do_not_open"
Q_DESSERT = "dessert"
Q_HP_BERTIE = "hp_bertie_botts"

F_UNKNOWN = "seek_unknown"
F_KNOWN = "seek_known"

Q_LIBRARY = "library_or_quidditch"
Q_CHARMS_STUDY = "study_self_or_group"
Q_HP_WARN = "hp_warn_or_run"
Q_EXPLORE = "explore_or_play"

F_SELF = "self"
F_OTHERS = "others"

Q_CHEATING = "exam_cheating"
Q_CHEAT_QUID = "cheat_in_quidditch"
Q_HP_POLYJUICE = "hp_steal_4_polyjuice"

F_BEND_RULES = "bend_rules"
F_JUSTICE = "pro_rule"
#F_FRIENDSHIP = "friendship"
#F_FIGHT = "pro_conflict"

Q_INK = "ink_textbook"
Q_WIZARD_POWERS = "wizard_powers"
Q_BULLY = "bully_stole_wand"
Q_NEW_RULE = "complain_or_comply"
Q_DUEL_CHESS = "duel_or_chess"
Q_HELP_STUD = "help_student_books"
Q_NEW_FASH = "new_fashion"
Q_AVOID = "avoid_new_student"
Q_DIVE = "dive_save_pet"
Q_BORED_JOKE = "bored_joke"
Q_DELAY_GOAL = "explore_delay_goal"
Q_JOB = "job_bored"
Q_HP_CHOC_FROG = "hp_last_choc_frog"
Q_HP_TRIWIZARD = "hp_triwizard_puzzle"
Q_HP_MINMAGIC_AUROR = "hp_minister_auror"
Q_PICK_PERSON = "magic_buddy"
Q_MAGIC_ABILITY = "which_magic_ability"
F_GRYFF = "feedback_gryff"
F_HUFF = "feedback_huff"
F_RAVEN = "feedback_raven"
F_SLYTH = "feedback_slyth"
I_SORT_YOU_INTO = "I_sort_you_into"
HUFFLEPUFF = "hufflepuff"
RAVENCLAW = "ravenclaw"
GRYFFINDOR = "gryffindor"
SLYTHERIN = "slytherin"
ER_SAY_WHAT = "what_did_you_say"

#other keys
YES = "yes"
NO = "no"
SELF = "self"
OTHERS = "others"
TEXT = "text"
PATH = "path"

ST_WELCOME = "ST_WELCOME"
ST_HP_KNOWLEDGE = "ST_HP_KNOWLEDGE"
ST_WELL = "ST_WELL"
ST_BEGIN = "ST_BEGIN"
ST_PREF = "ST_PREF"
ST_ALRIGHT = "ST_ALRIGHT"
ST_STRONG = "ST_STRONG"
ST_GRYFFINDOR = "ST_GRYFFINDOR"
ST_F_GRYFF = "ST_F_GRYFF"
ST_HUFFLEPUFF = "ST_HUFFLEPUFF"
ST_F_HUFF = "ST_F_HUFF"
ST_RAVENCLAW = "ST_RAVENCLAW"
ST_F_RAVEN = "ST_F_RAVEN"
ST_SLYTHERIN = "ST_SLYTHERIN"
ST_F_SLYTH = "ST_F_SLYTH"
ST_Q_TRANS = "ST_Q_TRANS"
ST_GVH = "ST_GVH"
ST_GVR = "ST_GVR"
ST_GVS = "ST_GVS"
ST_HVR = "ST_HVR" 
ST_HVS = "ST_HVS"
ST_RVS = "ST_RVS"
ST_FINALLY = "ST_FINALLY"
ST_RANDOM = "ST_RANDOM"
ST_CHOICE = "ST_CHOICE"
ST_RIGHT_THEN = "ST_RIGHT_THEN"
ST_DECLARE = "ST_DECLARE"
ST_I_SORT = "ST_I_SORT"
ST_HOUSE = "ST_HOUSE"
ST_END = "ST_END"

STATES = {
    ST_WELCOME : [WELCOME,NEW_STUD,GOOD_DAY],
    ST_HP_KNOWLEDGE : [SORT_PERS,HOG_STUDY,SORTING_HAT],
    ST_WELL : [I_VERY_WELL,I_WELL_THEN],
    ST_BEGIN : [PERS_HOUSE,FIND_HOUSE],
    ST_PREF : [Q_ANIMAL,Q_ELEMENT,Q_COLOR],
    ST_ALRIGHT : [I_ALRIGHT],
    ST_STRONG : [ST_HUFFLEPUFF,ST_GRYFFINDOR,ST_RAVENCLAW,ST_SLYTHERIN],
    ST_GRYFFINDOR : [Q_MAIL,Q_CAKE,Q_SHORTCUT_WIN],#Q_TROLL
    ST_F_GRYFF : {YES:F_ADVENTURE,NO:F_SAFE},
    ST_HUFFLEPUFF : [Q_NEW_PATH,Q_DOOR,Q_DESSERT,Q_HP_BERTIE],
    ST_F_HUFF : {YES:F_UNKNOWN,NO:F_KNOWN},
    ST_RAVENCLAW : [Q_LIBRARY,Q_CHARMS_STUDY,Q_HP_WARN,Q_EXPLORE],
    ST_F_RAVEN : {SELF:F_SELF,OTHERS:F_OTHERS},
    ST_SLYTHERIN : [Q_CHEATING,Q_CHEAT_QUID,Q_HP_POLYJUICE],
    ST_F_SLYTH : {YES:F_BEND_RULES,NO:F_JUSTICE},
    ST_Q_TRANS : [I_ALRIGHT,I_VERY_WELL,I_WELL_THEN],#I_ANOTHER_Q
    ST_GVH : [Q_BULLY,Q_NEW_FASH],
    ST_GVR : [Q_INK,Q_WIZARD_POWERS,Q_BULLY,Q_NEW_RULE,Q_DUEL_CHESS,Q_HELP_STUD,Q_HP_CHOC_FROG,Q_HP_TRIWIZARD],
    ST_GVS : [Q_INK,Q_WIZARD_POWERS,Q_HELP_STUD,Q_NEW_FASH,Q_AVOID,Q_DIVE,Q_BORED_JOKE,Q_DELAY_GOAL,Q_HP_CHOC_FROG,Q_HP_MINMAGIC_AUROR], #Q_JOB
    ST_HVR : [Q_INK,Q_WIZARD_POWERS,Q_HP_CHOC_FROG,Q_HELP_STUD,Q_NEW_FASH],
    ST_HVS : [Q_INK,Q_WIZARD_POWERS,Q_HP_CHOC_FROG,Q_BULLY,Q_NEW_RULE,Q_AVOID,Q_HELP_STUD],
    ST_RVS : [Q_BULLY,Q_NEW_RULE,Q_NEW_FASH,Q_DUEL_CHESS,Q_HP_TRIWIZARD,Q_AVOID],
    ST_FINALLY : [I_FINALLY],
    ST_RANDOM : [Q_PICK_PERSON,Q_MAGIC_ABILITY],
    ST_CHOICE : [I_SEE,I_FINE,I_INTERESTING],
    ST_RIGHT_THEN : [I_RIGHT_THEN],
    ST_DECLARE : {GRYFFINDOR: F_GRYFF, HUFFLEPUFF:F_HUFF, RAVENCLAW:F_RAVEN, SLYTHERIN:F_SLYTH},
    ST_I_SORT : [I_SORT_YOU_INTO],
    ST_HOUSE : {GRYFFINDOR:GRYFFINDOR, HUFFLEPUFF:HUFFLEPUFF,RAVENCLAW:RAVENCLAW,SLYTHERIN:SLYTHERIN},
    ST_END : 0
}

SP_TEXTS = {
    ER_SAY_WHAT : "What did you say?",
    F_ADVENTURE : "You like a little adventure I see.",
    FAREWELL : "Farewell Student!",
    F_BEND_RULES : "Not afraid to bend the rules I see.",
    #F_FIGHT : "Never back down from a fight. Good.",
    #F_FRIENDSHIP : "Friendship you seem to value above all else.",
    F_GRYFF : "For your qualities of bravery and friendship.",
    F_HUFF : "For your qualities of loyalty and friendship.",
    FIND_HOUSE : "Let's find out what house you truly belong to!",
    F_JUSTICE : "Justice is a great value to possess.",
    F_KNOWN : "Always better to go with what you know.",
    F_OTHERS : "You value the company of others.",
    F_RAVEN : "You have an open mind and thirst for learning.",
    F_SAFE : "Better safe than sorry.",
    F_SELF : "Company of the self is most precious!",
    F_SLYTH : "You are ambitious and resourceful.",
    F_UNKNOWN : "A thirst for seeking the unknown I see.",
    GOOD_DAY : "Good day, young student!",
    GRYFFINDOR : "Gryffindor",
    # HOG_HOUSES : "What do you know about Hogwarts and its four houses?",
    HOG_STUDY : "Would you like to study at Hogwarts School of Witchcraft and Wizardry?",
    HUFFLEPUFF : "Hufflepuff",
    I_AHGOON : "Ah! Go on.",
    I_ALRIGHT : "Alright", 
    I_ANOTHER_Q : "Let's try another question.", 
    I_FINALLY : "And finally, ",
    I_FINE : "A fine choice!",
    I_INTERESTING : "Interesting choice!",
    I_RIGHT_THEN : "Right then!",
    I_SEE : "Ah! I see.",
    I_SORT_YOU_INTO : "I sort you into ",
    I_VERY_WELL : "Very well.",
    I_WELL_THEN : "Well then.",
    NEW_STUD : "Aha! A new student!",
    PERS_HOUSE : "Your personality decides your house! Let's begin!",
    Q_ANIMAL : "What animal do you choose - Lion, Badger, Eagle or Serpent?",
    Q_AVOID : "Everyone in your class is avoiding the new student because he has a bad reputation. Would you talk to him?",
    Q_BORED_JOKE : "You are bored - would you crack a joke even if you knew it was not funny?",
    Q_BULLY : "A bully has stolen your wand. Do you report him to the Professor or get it back yourself?",
    Q_CAKE : "Would you use the new cake recipe you learnt at the risk of going wrong?",
    Q_CHARMS_STUDY : "Would you rather study in a group or by yourself for your Charms finals?",
    Q_CHEATING : "You see a classmate cheating in the History of Magic exam. Do you report him?",
    Q_CHEAT_QUID : "Would you cheat in the Quidditch final to score winning points for your house?",
    Q_COLOR : "What color do you choose - Blue, Green, Yellow or Red?",
    Q_DELAY_GOAL : "Would you explore an unknown path even if it delays you from your goal?",
    Q_DESSERT : "What do you choose - your favourite dessert or the new dessert?",
    Q_DIVE : "Would you - dive into a smelly pool of slush to save your pet?",
    Q_DOOR : "You see a door with a sign saying 'Do not open'? What do you do?",
    Q_DUEL_CHESS : "How would you prefer to defeat your rival - a duel by wands or a game of wizards chess?",
    Q_ELEMENT : "What element do you choose - Earth, Air, Water or Fire?",
    Q_EXPLORE : "Its a perfect day - would you explore the school grounds on a broomstick or play quidditch on it?",
    Q_HELP_STUD : "You are late for your exam. On your way you hit into a student carrying books. Do you stay to pick up the books?",
    Q_HP_BERTIE : "Bertie Bots came out with a mystery flavor bean that can teach new spells. Do you try it?",
    Q_HP_CHOC_FROG : "Would you share your last chocolate frog with your friend?",
    Q_HP_MINMAGIC_AUROR : "What would you like to be - the Minister for Magic or an Auror?",
    Q_HP_POLYJUICE : "You need to make the Polyjuice potion to save a friend. But it requires you to steal from the Professors cabinets - would you do it?",
    Q_HP_TRIWIZARD : "You are in the triwizard tournament - you see a huge wall with a puzzle on it. Do you solve the puzzle or blast the wall with your wand?",
    Q_HP_WARN : "You just learned that He-who-must-not-be-named is approaching Hogwarts. Would you warn the others or escape to save yourself?",
    Q_INK : "Your friend accidentally drops ink all over your textbook. Do you forgive them?",
    # Q_JOB : "Would you keep a job where you earn a lot but makes you bored?",
    Q_LIBRARY : "Would you rather play a quidditch match on broomsticks or read a book in the library?",
    Q_MAGIC_ABILITY : "If you could have any magical ability, what would it be?",
    Q_MAIL : "Will you fly out in a storm, on your broomstick, to deliver an important mail?",
    Q_NEW_FASH : "Wearing your wizard robes inside out is the new fashion. Would you adopt it?",
    Q_NEW_PATH : "On your way back home through the forest, you see a new path that could take you home - do you take it?",
    Q_NEW_RULE : "Hogwarts has a new rule in place - students are not allowed to play on the grounds! Do you complain or comply",
    Q_PICK_PERSON : "If you could pick one person to study magic with you who would it be?",
    Q_SHORTCUT_WIN : "Would you use a dangerous shortcut to win a competition?",
    Q_TROLL : "Your friend is trapped and a troll is headed her way - do you go and save her?",
    Q_WIZARD_POWERS : "Would you give up your wizard powers to save your best friend from he-who-must-not-be-named?",
    RAVENCLAW : "Ravenclaw",
    SLYTHERIN : "Slytherin",
    SORTING_HAT : "I am the Sorting Hat. Do you wish to get sorted?",
    SORT_PERS : "Did you know I can sort you based on your personality?",
    WELCOME : "Welcome!"
    # WHICH_HOUSE: "Do you know which house you wish to be sorted into?",
}

#TO COMPLETE
SP_PATHS = {
    ER_SAY_WHAT : "raw/Er_say_what.mp3",
    F_ADVENTURE : "raw/F_Adventure.mp3",
    FAREWELL : "raw/Farewell.mp3",
    F_BEND_RULES : "raw/F_Bend_rules.mp3",
    #F_FIGHT : "Never back down from a fight. Good.",
    #F_FRIENDSHIP : "Friendship you seem to value above all else.",
    F_GRYFF : "raw/F_Gryff.mp3",
    F_HUFF : "raw/F_Huff.mp3",
    FIND_HOUSE : "raw/Find_house.mp3",
    F_JUSTICE : "raw/F_Justice.mp3",
    F_KNOWN : "raw/F_known.mp3",
    F_OTHERS : "raw/F_others.mp3",
    F_RAVEN : "raw/F_Raven.mp3",
    F_SAFE : "raw/F_Safe.mp3",
    F_SELF : "raw/F_Self.mp3",
    F_SLYTH : "raw/F_Slyth.mp3",
    F_UNKNOWN : "raw/F_unknown.mp3",
    GOOD_DAY : "raw/Goodday.mp3",
    GRYFFINDOR : "raw/W_Gryffindor.mp3",
    # HOG_HOUSES : "raw/Hogwarts.mp3",
    HOG_STUDY : "raw/Studyhogwarts.mp3",
    HUFFLEPUFF : "raw/W_Hufflepuff.mp3",
    I_AHGOON : "raw/go_on.mp3",
    I_ALRIGHT : "raw/I_Alright.mp3", 
    I_ANOTHER_Q : "raw/I_another_Q.mp3", 
    I_FINALLY : "raw/I_finally.mp3",
    I_FINE : "raw/I_fine.mp3",
    I_INTERESTING : "raw/I_interesting.mp3",
    I_RIGHT_THEN : "raw/I_Right_then.mp3",
    I_SEE : "raw/I_see.mp3",
    I_SORT_YOU_INTO : "raw/Isortyouinto.mp3",
    I_VERY_WELL : "raw/I_Very_Well.mp3",
    I_WELL_THEN : "raw/I_well_then.mp3",
    NEW_STUD : "raw/Newstudent.mp3", 
    PERS_HOUSE : "raw/Letsbegin-extended.mp3",
    Q_ANIMAL : "raw/Q_Animal.mp3",
    Q_AVOID : "raw/Q_avoid.mp3",
    Q_BORED_JOKE : "raw/Q_bored_joke.mp3",
    Q_BULLY : "raw/Q_Bully.mp3",
    Q_CAKE : "raw/Q_Cake.mp3",
    Q_CHARMS_STUDY : "raw/Q_Charms_Study.mp3",
    Q_CHEATING : "raw/Q_Cheating.mp3",
    Q_CHEAT_QUID : "raw/Q_cheat_quid.mp3",
    Q_COLOR : "raw/Q_Color.mp3",
    Q_DELAY_GOAL : "raw/Q_delay_goal.mp3",
    Q_DESSERT : "raw/Q_Dessert.mp3",
    Q_DIVE : "raw/Q_dive.mp3",
    Q_DOOR : "raw/Q_Door.mp3",
    Q_DUEL_CHESS : "raw/Q_duel_chess.mp3",
    Q_ELEMENT : "raw/Q_Element.mp3",
    Q_EXPLORE : "raw/Q_Explore.mp3",
    Q_HELP_STUD : "raw/Q_help_stud.mp3",
    Q_HP_BERTIE : "raw/Q_HP_Bertie.mp3",
    Q_HP_CHOC_FROG : "raw/Q_HP_Choc_frog.mp3",
    Q_HP_MINMAGIC_AUROR : "raw/Q_HP_Minmagic_auror.mp3",
    Q_HP_POLYJUICE : "raw/Q_polyjuice.mp3",
    Q_HP_TRIWIZARD : "raw/Q_HP_Triwizard.mp3",
    Q_HP_WARN : "raw/Q_HP_Warn.mp3",
    Q_INK : "raw/Q_ink.mp3",
    # Q_JOB : "",
    Q_LIBRARY : "raw/Q_Library.mp3",
    Q_MAGIC_ABILITY : "raw/Q_magic_ability.mp3",
    Q_MAIL : "raw/Q_mail.mp3",
    Q_NEW_FASH : "raw/Q_new_fash.mp3",
    Q_NEW_PATH : "raw/Q_new_path.mp3",
    Q_NEW_RULE : "raw/Q_new_rule.mp3",
    Q_PICK_PERSON : "raw/Q_pick_person.mp3",
    Q_SHORTCUT_WIN : "raw/Q_Shortcut_Win.mp3",
    Q_TROLL : "raw/Q_troll .mp3",
    Q_WIZARD_POWERS : "raw/Q_wizard_powers.mp3",
    RAVENCLAW : "raw/W_Ravenclaw.mp3",
    SLYTHERIN : "raw/W_Slytherin.mp3",
    SORTING_HAT : "raw/Sorting_Hat.mp3",
    SORT_PERS : "raw/SortPersonality.mp3",
    WELCOME : "raw/welcome.mp3"
}
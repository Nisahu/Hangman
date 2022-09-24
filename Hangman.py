from random import choice

letters = "abcdefghijklmnopqrstuvwxyz"
words = ["aardvark", "alimony", "ascertain", "about", "absolute", "action", "arduous", "acrid", "acre", "auger", "animalistic", "asystole", "affirmative", "around", "astounding", "affidavit", "awkward", "awry",
        "broken", "balls", "bound", "bracken", "boorish", "butane", "bin", "boffin", "boating", "bashful", "breezy", "buff", "banned", "billable", "berries", "banana", "banter", "barons", "bioengineering",
        "curable", "court", "classless", "colonisation", "colony", "caring", "country", "certain", "channel", "conductivity", "commerce", "consider", "creature", "community", "conservationist", "cardiovascular",
        "deft", "during", "direct", "deputy", "divide", "digest", "domino", "dugout", "deepend", "diverge", "defunct", "diploma", "dubious", "downward", "dreadful", "dinosaur", "demographics", "differentiation",
        "exonerated", "every", "eager", "exude", "ennui", "enema", "escape", "embody", "embryo", "equine", "extort", "episode", "explode", "endemic", "entrant", "environs", "expedite", "eighteen", "education",
        "frightful", "farmhouse", "farm", "furious", "fungible", "farts", "fountain", "futile", "fantastic", "fabulous", "ferric", "fired", "floppy", "filing", "free", "frustrating", "fracking", "fentanyl",
        "gorge", "gigantic", "gulps", "gangrenous", "gorgeous", "globule", "gifted", "gumption", "greatness", "guarded", "grout", "gel", "grandfather", "gruesome", "groundskeepers", "general", "gastroenteritis",
        "hopeless", "horny", "hillbilly", "hairbrush", "historic", "hives", "hutch", "handle", "headed", "however", "harmful", "harvest", "hosiery", "headache", "humorous", "homicidal", "heterochromatic", "hump",
        "impregnable", "imp", "into", "inked", "inern", "isotope", "interact", "irregular", "irritation", "indigestion", "interstellar", "insectivorous", "intellectually", "incompatibility",
        "jokes", "jug", "jobs", "jammy", "jiggle", "jobless", "jewelers", "justified", "journeying", "jackhammers", "jurisdiction", "juxtaposition", "justifications", "judiciousness",
        "kraken", "kid", "kiss", "kneel", "kindly", "keycard", "kerosene", "knackered", "kerfuffles", "keyboardist", "kaleidoscope", "knowledgeable", "kindergartners", "kindheartedness",
        "lime", "law", "lurk", "lemon", "libido", "lampoon", "lockdown", "lethargic", "laceration", "legislation", "lollygagging", "lymphosarcoma", "libertarianism", "lexicographical",
        "monkey", "men", "mojo", "moose", "moment", "massage", "migraine", "mammogram", "meditative", "magnanimity", "microclimate", "magnetosphere",  "mountaineering", "multiplications", 
        "napalm", "new", "newt", "nifty", "neuron", "numeric", "notation", "nosebleed", "newscaster", "nearsighted", "neuroscience", "nightclubbing", "nanotechnology", "notwithstanding",
        "offal", "out", "oxen", "obese", "octave", "outpost", "obsolete", "oblivious", "octahedron", "overdevelop", "obstetrician", "ornamentation", "oceanographers", "oversimplifying",
        "progress", "pet", "pump", "patio", "preach", "popping", "prostate", "proximity", "perfection", "painstaking", "paramilitary", "parliamentary", "proprioception", "personification",
        "queried", "quip", "quiet", "quiver", "queuing", "quincunx", "quarrying", "quaternary", "qualitative", "questionable", "questionnaire", "quintessential", "quantifications",
        "racketeering", "run", "rook", "react", "refine", "reclaim", "regulate", "righteous", "retrograde", "recalculate", "reconstitute", "reconsidering", "rigidification", "ribonucleotides",
        "sloppy", "sad", "soar", "scrap", "symbol", "stomach", "shortage", "situation", "suspicious", "symptomatic", "spirituality", "schadenfreude", "sesquipedalian", "superfluousness",
        "thalassophobia", "toy", "toad", "treat", "thirty", "tactile", "tumbling", "triathlon", "toothpaste", "thunderbolt", "transoceanic", "tessellations", "thermoregulate", "transfiguration",
        "undying", "use", "ugly", "unfit", "uphold", "urinary", "uprising", "unbridled", "underscore", "unforgiving", "unproductive", "underprepared", "uncontrollably", "underprivileged",
        "viceroy", "van", "view", "vault", "vortex", "villain", "vagabond", "vestibule", "volumetric", "volcanology", "veterinarian", "vexillologist", "ventriloquists", "viscoelasticity",
        "washer", "who", "warm", "whack", "wiener", "warlord", "washroom", "wallpaper", "weightless", "withershins", "warmongering", "worthlessness", "whippersnapper", "weatherproofing",
        "xhosa", "xenon", "xylems", "xenophobe", "xenophile", "xenobiology", "xenobotany", "xenophobic", "xenophilic", "xeroradiographically",
        "yearning", "you", "year", "yelps", "yawned", "yoghurt", "yellowed", "youngling", "yourselves", "youthfulness",
        "zealot", "zip", "zoom", "zones", "zombie", "zygotes", "ziggurat", "zestfully", "zoological", "zooplanktons", "zombification"]

lives = ""
livesDisplay = ""

gameOver = False
replay = True

lettersGuessed = ""
wordsGuessed = []

wordsUsed = []
def reset():
    global word
    global wordDisplay
    global lives
    global livesDisplay
    global gameOver
    global lettersGuessed
    global wordsGuessed
    global wordsUsed
    wordDisplay = "_"
    wordFound = False
    while not wordFound:
        wordCandidate = choice(words)
        if wordCandidate not in wordsUsed:
            wordFound = True
            word = wordCandidate
    wordDisplay = "_"
    while len(wordDisplay) < len(word):
        wordDisplay = wordDisplay + "_"
    lives = ""
    livesDisplay = ""
    gameOver = False
    lettersGuessed = ""
    wordsGuessed = []

def badInput(wordGuess, wordActual):
    if wordGuess:
        print(f"The word I'm thinking of has {len(wordActual)} letters, so that can't be it! Don't worry, you haven't lost a life; try again.")
    else:
        print("That wasn't a letter or a word! Don't worry, you haven't lost a life; try again.")

def win(wordArg):
    global gameOver
    gameOver = True
    print(f"Congratulations! You won. The word was {wordArg.upper()}.")

def lose(wordArg):
    global gameOver
    gameOver = True
    print(f"Oops! You lost all your lives. The word was {wordArg.upper()}.")

def addToLettersGuessed(addition, lettersGuessedArg):
    if len(lettersGuessedArg) == 0:
        lettersGuessedArg = lettersGuessedArg + addition.upper()
    else:
        lettersGuessedArg = lettersGuessedArg + ", " + addition.upper()
    return lettersGuessedArg

def addToWordsGuessed(addition, wordsGuessedArg):
    wordsGuessedArg += [addition.upper()]
    return wordsGuessedArg

def printStats():
    print("")
    print(f"{wordDisplay}   Lives: {livesDisplay}   Letters guessed: {lettersGuessed.upper()}   Words guessed: {', '.join(wordsGuessed)}")

def loseLife():
    global lives
    global livesDisplay
    lives -= 1
    livesDisplay = livesDisplay[slice(len(livesDisplay) - 1)]

while replay:
    reset()
    while type(lives) != int:
        print("Do you want to play on Easy, Medium, or Hard mode? This determines your lives per word - 7, 5, or 3.")
        difficulty = input().upper()
        if difficulty == "EASY":
            lives = 7
            livesDisplay = "♥♥♥♥♥♥♥"
        elif difficulty == "MEDIUM":
            lives = 5
            livesDisplay = "♥♥♥♥♥"
        elif difficulty == "HARD":
            lives = 3
            livesDisplay = "♥♥♥"
        else:
            print("That wasn't a valid input, please try again.")
    print(f"You have chosen to play on {difficulty} mode, and are allotted {str(lives)} lives.")
    print(f"I'm thinking of a word. It's {len(word)} letters long.")
    printStats()
    while not gameOver:
        guessCandidate = input("Guess a letter or a word: ").lower()
        if len(guessCandidate) == 1:
            if guessCandidate in letters:
                if guessCandidate.upper() in lettersGuessed:
                    print("You've already guessed that letter! Don't worry, you haven't lost a life; try again.")
                else:
                    lettersGuessed = addToLettersGuessed(guessCandidate, lettersGuessed)
                    if guessCandidate in word:
                        foundLetters = [i for i in range(len(word)) if word[i] == guessCandidate]
                        for i in foundLetters:
                            wordDisplayList = list(wordDisplay)
                            wordDisplayList[i] = guessCandidate.upper()
                            wordDisplay = "".join(wordDisplayList)
                        if "_" not in wordDisplay:
                            win(word)
                        else:
                            print(f"Good job! The letter {guessCandidate.upper()} was found {len(foundLetters)} times.")
                    else:
                        loseLife()
                        print(f"Sorry! {guessCandidate.upper()} isn't in my word. You've lost a life.")
                        if lives == 0:
                            lose(word)
            else:
                badInput(False, word)
        else:
            if len(guessCandidate) != len(word):
                badInput(True, word)
            else:
                if guessCandidate.upper() in wordsGuessed:
                    print("You've already guessed that word! Don't worry, you haven't lost a life; try again.")
                else:
                    wordsGuessed = addToWordsGuessed(guessCandidate, wordsGuessed)
                    if guessCandidate.lower() == word:
                        wordDisplay = word.upper()
                        win(word)
                    else:
                        loseLife()
                        print(f"Sorry! {guessCandidate.capitalize()} isn't the word I'm thinking of! You've lost a life.")
                        if lives == 0:
                            lose(word)
        printStats()
    wordsUsed += [word]
    replay = True if input("Would you like to play again? Y/N ").upper() == "Y" else False
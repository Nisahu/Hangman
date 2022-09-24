from random import choice

letters = "abcdefghijklmnopqrstuvwxyz"
words = ["aardvark", "alimony", "ascertain", "about", "absolute", "action", "arduous", "acrid", "acre", "auger", "animalistic", "asystole", "affirmative", "around", "astounding", "affidavit", "awkward", "awry",
        "broken", "balls", "bound", "bracken", "boorish", "butane", "bin", "boffin", "boating", "bashful", "breezy", "buff", "banned", "billable", "berries", "banana", "banter", "barons", "bioengineering",
        "curable", "court", "classless", "colonisation", "colony", "caring", "country", "certain", "channel", "conductivity", "commerce", "consider", "creature", "community", "conservationist", "cardiovascular",
        "deft", "during", "direct", "deputy", "divide", "digest", "domino", "dugout", "deepend", "diverge", "defunct", "diploma", "dubious", "downward", "dreadful", "dinosaur", "demographics", "differentiation",
        "exonerated", "every", "eager", "exude", "ennui", "enema", "escape", "embody", "embryo", "equine", "extort", "episode", "explode", "endemic", "entrant", "environs", "expedite", "eighteen", "education",
        "frightful",
        "gorge",
        "hopeless",
        "impregnable",
        "jokes",
        "kraken",
        "lime",
        "monkey",
        "napalm",
        "offal",
        "progress",
        "queried",
        "racketeering",
        "sloppy",
        "thalassophobia",
        "undying",
        "viceroy",
        "washer",
        "xhosa",
        "yearning",
        "zealot"]

word = choice(words)
underscore = "_"
wordDisplay = "_"
while len(wordDisplay) < len(word):
    wordDisplay = wordDisplay + underscore

lives = "TBD"
while type(lives) != int:
    print("Do you want to play on Easy, Medium, or Hard mode? This determines your lives per word - 7, 5, or 3.")
    difficulty = input().upper()
    if difficulty == "EASY":
        lives = 7
    elif difficulty == "MEDIUM":
        lives = 5
    elif difficulty == "HARD":
        lives = 3
    else:
        print("That wasn't a valid input, please try again.")
print(f"You have chosen to play on {difficulty} mode, and are allotted {str(lives)} lives.")

gameOver = False
lettersGuessed = ""
wordsGuessed = []

def badInput(wordGuess):
    if wordGuess:
        print(f"The word I'm thinking of has {len(word)} letters, so that can't be it! Don't worry, you haven't lost a life; try again.")
    else:
        print("That wasn't a letter or a word! Don't worry, you haven't lost a life; try again.")

def win():
    global gameOver
    gameOver = True
    print("Congratulations! You won.")

def lose():
    global gameOver
    gameOver = True
    print("Oops! You lost all your lives.")

def addToGuessed(addition):
    global lettersGuessed
    global wordsGuessed
    if len(addition) == 1:
        if len(lettersGuessed) == 0:
            lettersGuessed = lettersGuessed + addition.upper()
        else:
            lettersGuessed = lettersGuessed + ", " + addition.upper()
    else:
        wordsGuessed += [addition.upper()]

def printStats():
    print(f"{wordDisplay}   Lives: {lives}   Letters guessed: {lettersGuessed.upper()}   Words guessed: {', '.join(wordsGuessed)}")

print(f"I'm thinking of a word. It's {len(word)} letters long.")
printStats()

while not gameOver:
    guessCandidate = input("Guess a letter or a word: ").lower()
    if len(guessCandidate) == 1:
        if guessCandidate in letters:
            if guessCandidate.upper() in lettersGuessed:
                print("You've already guessed that letter! Don't worry, you haven't lost a life; try again.")
            else:
                addToGuessed(guessCandidate)
                if guessCandidate in word:
                    foundLetters = [i for i in range(len(word)) if word[i] == guessCandidate]
                    for i in foundLetters:
                        wordDisplayList = list(wordDisplay)
                        wordDisplayList[i] = guessCandidate.upper()
                        wordDisplay = "".join(wordDisplayList)
                    if "_" not in wordDisplay:
                        win()
                    else:
                        print(f"Good job! The letter {guessCandidate.upper()} was found {len(foundLetters)} times.")
                else:
                    lives = lives - 1
                    print(f"Sorry! {guessCandidate.upper()} isn't in my word. You've lost a life.")
                    if lives == 0:
                        lose()
        else:
            badInput(False)
    else:
        if len(guessCandidate) != len(word):
            badInput(True)
        else:
            if guessCandidate.upper() in wordsGuessed:
                print("You've already guessed that word! Don't worry, you haven't lost a life; try again.")
            else:
                addToGuessed(guessCandidate)
                if guessCandidate.lower() == word:
                    wordDisplay = word.upper()
                    win()
                else:
                    lives = lives - 1
                    print(f"Sorry! {guessCandidate.capitalize()} isn't the word I'm thinking of! You've lost a life.")
    printStats()

input()
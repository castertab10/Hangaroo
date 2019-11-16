def isWordGuessed(secretWord, lettersGuessed):

    n = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            n += 1
        else:
            return False
    return True
    

def getGuessedWord(secretWord, lettersGuessed):
    
    n = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            n = n + letter
        else:
           n = n + '_ '
    return n

def getAvailableLetters(lettersGuessed):
    
    import string
    lowerCaseLetters = string.ascii_lowercase
    notInLettersGuessed = ''
    
    for letter in lowerCaseLetters:
        if letter not in lettersGuessed:
            notInLettersGuessed = notInLettersGuessed + letter
    return notInLettersGuessed

def Hangaroo():
    
    guesses = 3
    lettersGuessed =[]
    
    secretWord = input("Input the secret word here: ")


    while guesses > 0:
        if isWordGuessed(secretWord, lettersGuessed):
            return print('Correct! Great Job!')
        
        print('You have ' + str(guesses) + ' guesses left.')
        print('Available Letters: ' + getAvailableLetters(lettersGuessed))
        gameInput = input('Please guess a letter: ')
        gameInput = str(gameInput)
        gameInput = gameInput.lower()

        if gameInput not in lettersGuessed:
            lettersGuessed.append(gameInput)

            if gameInput in secretWord:
                print("Nice! " + getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Wrong letter!: " + getGuessedWord(secretWord, lettersGuessed))
                guesses -= 1
        else:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))

    return print("Sorry, you ran out of guesses. The word was " + str(secretWord))

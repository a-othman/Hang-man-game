import random

WORDLIST_FILENAME = "words.txt"


def loadWords(WORDLIST_FILENAME):
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
#    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
#    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist= loadWords(WORDLIST_FILENAME)
def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    counter = 0
    lstsecretword = list(secretWord)
    for i in range(len(lstsecretword)):
        if lstsecretword[i] in lettersGuessed:
            counter +=1 
            if counter == len(lstsecretword):
                return(True)
        else:
            return(False)

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    lstsecretWord = list(secretWord)
    tobeprnt = ''
    for i in range(0,len(secretWord)):
        if lstsecretWord[i] in lettersGuessed:
            tobeprnt = tobeprnt+lstsecretWord[i]
        else:
            tobeprnt = tobeprnt+ '_ '
    return tobeprnt

def getAvailableLetters(lettersGuessed):
    import string
    chrac =list(string.ascii_lowercase)
    stringleft = ''
    for i in range(0,len(lettersGuessed)):
        if lettersGuessed[i] in chrac:
            chrac.remove(lettersGuessed[i])
    for j in range(0,len(chrac)):
        stringleft = stringleft+chrac[j]
    return stringleft


#test Cases for fun.getAvailableLetters:
#test_cases= [(['e', 'i', 'k', 'p', 'r', 's'], 'abcdfghjlmnoqtuvwxyz'), #(lettersgueesed, expected output)
#             ([], 'abcdefghijklmnopqrstuvwxyz'), 
#             (['q', 'i', 't'], 'abcdefghjklmnoprsuvwxyz'),
#             (['d', 'e', 'b', 'z', 'y', 'a', 'w', 'p'], 'cfghijklmnoqrstuvx'),
#             (['a', 'm', 'x', 'y'], 'bcdefghijklnopqrstuvwz'),
#             (['t', 'u', 'l'], 'abcdefghijkmnopqrsvwxyz')
#             ]
#for case in test_cases:
#    a= getAvailableLetters(case[0])
#    print(a == case[1])
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+ str(len(secretWord))+' letters long')
    print("-----------")
    leftguesses = 8
    lettersGuessedlst = []
    lettersGuessed = ''
    while leftguesses > 0:
        if isWordGuessed(secretWord, lettersGuessedlst) == True:
            print("Congratulations, you won!")
            break
        else:
            print("You have "+ str(leftguesses)+ " guesses left.")
            print("Available Letters: "+getAvailableLetters(lettersGuessedlst))
            lettersGuessed = input("Please guess a letter: ")
            z = lettersGuessed.lower()
            if z in lettersGuessedlst:
                print("Oops! You've already guessed that letter: "+ getGuessedWord(secretWord, lettersGuessedlst))
                print("-----------")
            else:
                lettersGuessedlst.append(z)
                if z in secretWord:
                    print("Good Guess: "+ getGuessedWord(secretWord, lettersGuessedlst))
                    isWordGuessed(secretWord, lettersGuessedlst)
                    print("-----------")
                else:
                    print("Oops! That letter is not in my word: "+ getGuessedWord(secretWord, lettersGuessedlst))
                    print("-----------")
                    leftguesses -=1
                    if leftguesses ==0:
                        print("Sorry, you ran out of guesses. The word was "+ str(secretWord))
                        break


# To try the game out please uncomment the following lines
#secretWord = chooseWord(wordlist).lower()
#hangman(secretWord)




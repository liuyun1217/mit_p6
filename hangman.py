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
    numfl = 0
    lettersGuessed = ''
    lettersGuessedA = '1'
    while numfl <= 8 and lettersGuessedA != secretWord:
        
        print 'You have ' + str(8-numfl) + ' guesses left.'
        allwords = getAvailableLetters(lettersGuessed)
        print 'Available Letters: ' + allwords
        nowWord = raw_input("Please guess a letter: ")
        
        
        
        
                
        if lettersGuessedA != secretWord:
            if allwords.find(nowWord) >= 0:
                lettersGuessed = lettersGuessed + nowWord
                nowresult = getGuessedWord(secretWord, lettersGuessed)
                if secretWord.find(nowWord)<0:
                    print "Oops! That letter is not in my word: " + nowresult                
                elif lettersGuessedA != nowresult:
                    print "Good guess: " + nowresult

                '''elif lettersGuessed == lettersGuessedA:'''
            else:
                print "Oops! You've already guessed that letter: " + nowresult
            
   
        
        lettersGuessedA =nowresult
        numfl += 1 
        print ("------------" )
        
        
    if nowresult == secretWord:
        print "Congratulations, you won!"
         
         
    elif numfl == 9:
        print "Sorry, you ran out of guesses. The word was else. "
         

        
        
        
        
        
        
        
        
        
        
        
   

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    fl = 0
    for element in lettersGuessed:
        if secretWord.count(element)!=0:
            fl = fl + 1
       
    if fl >= len(secretWord):
        return True
    else:
         return False
         
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    newWord = ''
    for element in secretWord:
        fl = 0
        for i in lettersGuessed:
            if element == i:
                newWord = newWord + element
            else:
                fl += 1
        if fl ==len(lettersGuessed):
            newWord = newWord + '_ '
    return newWord




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    lowStr = list(string.ascii_lowercase)
    
    for element in lettersGuessed:
        lowStr.remove(element)
    return ''.join(lowStr)        
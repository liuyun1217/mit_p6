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
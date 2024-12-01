from wonderwords import RandomWord

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\\  | 
      |
     ===''', '''
  +---+
  O   |
 /|\\  |  
 /    |
     ===''', '''
  +---+
  O   |
 /|\\  |  
 / \\  |  
     ===''',]

run = 1
hangcount = 0 
rword = RandomWord()
hangword = list(rword.word(word_max_length=8,word_min_length=8))
userword = []
userstring = ""
for i in range (0,8):
    userword.append("X")


def letterGuess(hcount):

    letter = input('enter the letter that you would like to guess')
    letter = letter.lower()
    check = 0
    for i in range(0,8):
        if letter == hangword[i]:
            userword[i] = letter
            

        else:
            check += 1
    if check == 8 :
        hcount += 1 
        
    return hcount



while run == 1:
    hangcount = letterGuess(hangcount)
    if userword == hangword:
        print("You Win")
        run = 0
    elif hangcount < 7 :
        print(HANGMAN_PICS[hangcount])
    else:
        print("You Lose")
        run = 0
    userstring = ''.join(userword)
    print(userstring)
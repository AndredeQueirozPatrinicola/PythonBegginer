print('*********************************')
print('***Welcome to the Hangman Game***')
print('*********************************')

print('\n \n ')

print('Welcome to the Hangman Game \n \nTry to guess the word by choosing a letter \n \nBe careful or you are gone be hanged :P! \n ')

import random

list_of_words = ['banana', 'orange', 'computer', 'python', 'principle', 'science', 'factory', 'struggle', 'subordination', 'president', 'scramble', 
                 'coverage', 'invasion', 'baseball', 'weight']
secret_word = random.choice(list_of_words)
mistakes = 0 
gaps_number = len(secret_word)
gaps1 = "_" * int(gaps_number)
gaps = list(gaps1)
right_words = gaps

cond = 0

while cond == 0:
    dificulty = input("Type [Easy], [Medium] or [Hard] to set the dificulty: ")
    if dificulty == "Easy" or dificulty == "easy" or dificulty == "e":
        chances = 10
        dif = "easy"
        print(f"You choosed {dif} dificulty")
        cond += 1
    elif dificulty == "Medium" or dificulty == "medium" or dificulty == "m":
        chances = 7
        dif = "medium"
        print(f"You choosed {dif} dificulty")
        cond += 1
    elif dificulty == "Hard" or dificulty == "hard" or dificulty == "hard":
        chances = 4
        dif = "hard"
        print(f"You choosed {dif} dificulty")
        cond += 1
    else:
        print("Type a valid dificulty")
        dificulty = input("Type [Easy], [Medium] or [Hard] to set the dificulty: ")

guessed = False
hanged = False
count_chances = 9


while(not guessed and not hanged):
  guess = input('Try a letter: \nR:')
  
  if guess.isnumeric:
      print("Numbers are not allowed")
  
  if (guess in secret_word):
  
    position = 0
    for letter in secret_word:
      if (guess.upper() == letter.upper()):
        right_words[position] = letter
      position += 1
                
  else:
    mistakes +=1
    counter = print("You have {} chances of {}".format(count_chances, chances))
    counter = count_chances = count_chances - 1

  hanged = mistakes == chances
  guessed = '_' not in gaps
  print('\n')
  print(right_words)
  print('\n')

if hanged:
  print('You lose :(! Try again!')
elif guessed:
  print('Congratulations! You won :)!')
print('Game Over!')

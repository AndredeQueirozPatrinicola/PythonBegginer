print('Rock, Paper, Scissors')


import random

game = ['rock', 'paper', "scissors" ]
points = 0
ai_points = 0
defeat = False
victory = False

cond = 0

while cond == 0:
    lenght = input("Type [Long], [Medium] or [Short] to set match lenght: ")
    if lenght == "Long" or lenght == "long" or lenght == "l":
        rounds = 7
        dif = "long"
        print(f"You choosed a {dif} match")
        cond += 1
    elif lenght == "Medium" or lenght == "medium" or lenght == "m":
        rounds = 5
        dif = "medium"
        print(f"You choosed a {dif} match")
        cond += 1
    elif lenght == "short" or lenght == "Short" or lenght == "s":
        rounds = 3
        dif = "short"
        print(f"You choosed a {dif} match")
        cond += 1
    else:
        print("Type a valid dificulty")
        lenght = input("Type [Long], [Medium] or [Short] to set match lenght: ")

while not defeat and not victory:
    
    play = input('Choose rock, paper or scissors: ')
    
    ai_play = random.choice(game)
    
    if play == 'rock' and ai_play == 'scissors':
        print(f'Ai choosed {ai_play}')
        print('You won this round!')
        points += 1
        print(f'You: {points} - Computer: {ai_points}')
    elif play == 'paper' and ai_play == 'rock':
        print(f'Ai choosed {ai_play}')
        print('You won this round!')
        points += 1
        print(f'You: {points} - Computer: {ai_points}')
    elif play == 'scissors' and ai_play == 'paper':
        print(f'Ai choosed {ai_play}')
        print('You won this round!')
        points += 1
        print(f'You: {points} - Computer: {ai_points}')
    elif ai_play == 'rock' and play == 'scissors':
        print(f'Ai choosed {ai_play}')
        print('You lost this round')
        ai_points += 1
        print(f'You: {points} - Computer: {ai_points}')
    elif ai_play == 'paper' and play == 'rock':
        print(f'Ai choosed {ai_play}')
        print('You lost this round')
        ai_points += 1
        print(f'You: {points} - Computer: {ai_points}')
    elif ai_play == 'scissors' and play == 'paper':
        print(f'Ai choosed {ai_play}')
        print('You lost this round')
        ai_points += 1
        print(f'You: {points} - Computer: {ai_points}')
    elif play == ai_play:
        print(f'AI choosed {ai_play}')
        print('It tied!')
        print(f'You: {points} - Computer: {ai_points}')
    else:
        print('Please, type rock, paper or scissors')
        
    defeat = ai_points == rounds
    victory = points == rounds

else:
    print('Game Over!')
    
if points > ai_points:
    print('You won!')
else:
    print('You lose!')
            

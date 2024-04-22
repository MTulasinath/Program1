'''Rock paper scissors'''
import random
def rps():
    player_points = 0
    computer_points = 0
    for i in range(5):
        player = input('Enter Rock/Paper/Scissors : ')
        ls = ['Rock','Paper','Scissors']
        computer = random.choice(ls)
        if player==computer:
            print('no points')
        elif computer=='Paper' and player=='Rock':
            computer_points+=1
        elif computer=='Scissors' and player=='Rock':
            player_points+=1
        elif computer=='Rock' and player=='Paper':
            player_points+=1
        elif computer=='Scissors' and player=='Paper':
            computer_points+=1
        elif computer=='Paper' and player=='Scissors':
            player_points+=1
        elif computer=='Rock' and player=='Scissors':
            computer_points+=1
        print(f'Player choice is {player} and computer choice is {computer}')
        print(f'computer points is {computer_points} and your points is {player_points}')
        print('-----------'*10)
    if player_points>computer_points:
        print(f'Player points is {player_points} and computer points is {computer_points} player won the match')
    elif computer_points>player_points:
        print(f'Player points is {player_points} and computer points is {computer_points} computer won the match')
    elif player_points==computer_points:
        print('match tie wanna play again')
rps()
playagain = input('Wanna play match ')
if playagain=='Yes':
    rps()
elif playagain=='No':
    print('bye')

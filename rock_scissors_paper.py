import random


def rsp():
    user = (input('Rock, scissors or paper? \n> '))
    computer = random.choice(['rock', 'scissors', 'paper'])
    if user == computer:
        return('Tie!')
    elif is_win(user,computer):
        return 'You won!'
    elif is_win(computer,user):
        return 'You lost! :('
    else:
        return 'Something went wrong! ;('




def is_win(player, opponent):
    if (player == 'rock' and opponent == 'scissors') or \
       (player == 'scissors' and opponent == 'paper') or \
       (player == 'paper' and opponent == 'rock'):
        return True
    else:
        return False
print(rsp())
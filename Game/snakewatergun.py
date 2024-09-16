import random


def swg(comp, mine):
    if(comp == 'snake' and mine == 'gun'):
        return True
    elif(comp == 'water' and mine == 'snake'):
        return True
    elif(comp == 'gun' and mine == 'water'):
        return True
    else:
        return False


choice = ('snake', 'water', 'gun')
comp = random.randint(0, 2)
comp = choice[comp]
mine = input('Enter the snake , water or gun\n')

win = swg(comp, mine)
if win:
    print('you won')
else:
    print('you loose')

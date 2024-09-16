import random
from tokenize import Number

Number = random.randint(1, 100)
attempt = 1
guess = int(input('Enter the Number :\n'))

while(True):
    if(guess > Number):
        guess = int(
            input('enter another number bcz the number is too large : '))
        attempt += 1
    elif(guess < Number):
        guess = int(input('enter another number bcz the number is too small: '))
        attempt += 1
    else:
        print(
            f"yeah that's the number! you guessed  it right in {attempt} attempts")
        break

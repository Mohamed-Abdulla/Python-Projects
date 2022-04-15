
import random

def Guess(x):
    random_number =random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input('Guess the Random Number :'))
        if guess<random_number:
            print("Oops..Number is too low")
        elif guess>random_number:
            print("Oops..Number is too high")
    print(f"Congratulations you found the Random Number {random_number} successfully 🚀")
Guess(10)
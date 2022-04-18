
import random
#?We Guess
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

#?Computer Guess 
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low!=high:
            guess=random.randint(low, high)
        else:
            guess=low #it could be high also
        feedback=input(f'Is {guess} too high (H), too low (L) or correct (C) : ').lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f'Yay!!,Computer guess the number {guess}, correctly 🙌')
computer_guess(100) 
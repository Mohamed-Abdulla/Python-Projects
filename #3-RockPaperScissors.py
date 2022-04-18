
import random

def play():
    user=input("Enter your Choice 'r' for rock, 's' for scissors , 'p' for papers : ").lower()
    computer=random.choice(['r','p','c'])

    if user==computer:
        return "It's a tie ‼"
    
    if is_win(user,computer):
        return "You won 🚀"
    
    return "You lost 😓"

def is_win(user,computer):
    #r>s,s>p,p>r
    if (user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r'):
        return True
print(play())
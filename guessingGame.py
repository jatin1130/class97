import random

ran = random.randint(1,9)
chances = 0

print("- Number Guessing Game -")
print("Guess number between 1-9")

while chances < 5 :

    Guess = int(input("Enter your guess :- "))

    if Guess == ran:
        print("Conguratulations you 'WON'")
        break
    elif Guess < ran:
        print("your guess was too low,guess number higher than" ,Guess)

    else :
        print("your guess was too high,guess number lower than" ,Guess)
    chances += 1

if not chances<5:
    print("you lose. The number is ",ran)
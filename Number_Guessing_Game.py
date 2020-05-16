import random
number=random.randint(1,25)
chances=0
print("Guess a number between 1 and 25 :")
while chances<5:
    guess = int(input("Enter your Guess :"))

    if  guess ==number:
        print("Congratulation YOU WON!!")
        break
    elif guess<number:
        print("Your guess was too low")
    else:
        print("Your guess was too High")
    chances+=1
    print("Chances Left :",5-chances)
else:
    print("You Lose!!! The number is : ", number)

import random

def welcome():
    print('This is a number guessing game')
    i=int(input("Enter the number of times you want to guess"))
    x=int(input("Enter your guess"))
    r=random.randint(0,3)
    game(i,x,r)


def game(i,x,r):
    while i>1:
        if x==r:
            print("Your guess is correct")
            end(r)
            break
        elif(x!=r):
            print("Your guess is incorrect")
            x=int(input("Guess again"))
            i-=1
            if i==0:
                print("Sorry you could not get it right")
                end(r)
        else:
            print("Please input valid number")
        return x

def end(r):
    redo=input("Do you want to play again(y/n)")
    if redo=="y":
        welcome()
    elif(redo=="n"):
        print("The number to be guessed was:",r)
        print("Thank you for playing")
    else:
        print("Please enter valid input")
        end(r)

welcome()

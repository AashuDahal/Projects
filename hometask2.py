def welcome():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=input("Press yes for multiplication and no for power: ")
    multi(a,b,c)
    return a,b,c

def multi(a,b,c):
    if c=="yes":
        for x in range(a,b+1):
            for y in range(a,b+1):
                print('{:3}'.format(x*y), end=' ')
            print()
    elif(c=="no"):
        for x in range(a,b+1):
            for y in range(a,b+1):
                print('{:3}'.format(x**y), end=' ')
            print()
    else:
        print("Enter valid input")
    end()

def end():
    again=input("Do you want to try again(y/n) ")
    if again=="y":
        welcome()
    else:
        print("Thank you so much")

welcome()

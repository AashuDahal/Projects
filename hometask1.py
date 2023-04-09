def eat():
    print("Hell yeah mf eat it")

def donteat():
    print("No mf dont eat")
    
def yourcall():
    print("Your call dumbasss")

def conditions():
    a=input("Did anyone see you?")
    if a=="yes":
        b=input("Was it boss/lover/parent?")
        if b=="yes":
            d=input("Was it expensive?")
            if d=="yes":
                e=input("Can you cutt of the part that touched the floor?")
                if e=="yes":
                    eat()
                else:
                    yourcall()
            else:
                f=input("Is it bacon?")
                if f=="yes":
                    eat()
                else:
                    donteat()
        else:
            donteat()
    else:
        c=input("Was it sticky?")
        if c=="yes":
            g=input("Is it raw steak?")
            if g=="yes":
                i=input("Are you puma?")
                if i=="yes":
                    eat()
                else:
                    donteat()
            else:
                j=input("Did the cat lick it?")
                if j=="yes":
                    k=input("Is your cat healthy?")
                    if k=="yes":
                        eat()
                    else:
                        yourcall()
                else:
                    eat()
        else:
            h=input("Is it emawsaruus?")
            if h=="yes":
                l=input("Are you megalosaurus?")
                if l=="yes":
                    eat()
                else:
                    donteat()
            else:
                j=input("Did the cat lick it?")
                if j=="yes":
                    k=input("Is your cat healthy?")
                    if k=="yes":
                        eat()
                    else:
                        yourcall()
                else:
                    eat()
    end()

def end():   
    again=input("Do you wanna test again?(y/n)")
    if again!="n":
        conditions()
    else:
        print("Thank you for playing")

conditions()
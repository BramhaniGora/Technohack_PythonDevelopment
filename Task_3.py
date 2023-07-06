import random
def game1(comp,user):
    comp1=comp
    user1=user
    s=random.choice(comp1).lower()
    print("\nUser Selected:  ",user1)
    print("Computer Selected:  ",s)
    if s==user1:
        print("-------Tie------")
    if s=="rock":
        if user=="paper":
            print("----------User won the Game----------")
        elif user=="scissors":
            print("----------Computer won the Game----------")
    if s=="paper":
        if user=="scissors":
            print("----------User won the Game----------")
        elif user=="rock":
            print("----------Computer won the Game----------")
    if s=="scissors":
        if user=="rock":
            print("----------User won the Game----------")
        elif user=="paper":
            print("----------Computer won the Game----------")
                            

def taking_input():
    comp=['Rock','Paper','Scissors']
    i=1
    while(i==1):
        user=input("\nEnter your choice Rock----Paper----Scissors:  ")
        game1(comp,user)
        print("\nWant to continue the game \nif yes (type-1)   if no(type other than-1)")
        i=int(input("Enter the choice:  "))
print("\n\n====================ROCK PAPER SCISSORS=================================")
taking_input()
print("\n====================GAME FINISHED============================")
import random
import string
def ran_gen(password):
    leng=int(input("Enter the length of the password:  "))
    passw=password
    print("The generated password is:  ",end="")
    for j in range(0,leng):
        print(random.choice(passw),end="")
def taking_input():
    print("Select the special characters for your password")
    print("1: Alphabets\n2: Digits\n3: Special Characters\n4: None")
    password=""
    i=int(input("Enter the choice:  "))
    while(i>=0):
        if i==1:
            password+=string.ascii_letters
            i=int(input("Enter the choice:  "))
        elif i==2:
            password+=string.digits
            i=int(input("Enter the choice:  "))
        elif i==3:
            password+=string.punctuation
            i=int(input("Enter the choice:  "))
        elif i==4:
            ran_gen(password)
            break
        else:
            print("choose the correct choice")
            i=int(input("Enter the choice:  "))
print("\n\n=======================RANDOM PASSWORD GENERATOR================================")
taking_input()

 